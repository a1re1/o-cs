#!/usr/bin/env python3
"""Search-quality eval harness for the oasis CLI.

Runs `oasis` once per query, computes recall@k / MRR / nDCG@3 (overall and
per section), prints an aligned table, and appends one JSON line to
evals/results/history.jsonl.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

HISTORY_PATH = Path("evals/results/history.jsonl")

METRIC_KEYS = ("recall@1", "recall@3", "recall@5", "recall@10", "mrr", "ndcg@3")


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def recall_at_k(relevant: Sequence[str], ranked_paths: Sequence[str], k: int) -> float:
    """1.0 if any relevant path appears in the top-k results, else 0.0."""
    if not relevant:
        return 0.0
    top = set(ranked_paths[:k])
    return 1.0 if top & set(relevant) else 0.0


def mrr(relevant: Sequence[str], ranked_paths: Sequence[str]) -> float:
    """Reciprocal rank of the first relevant hit; 0.0 if none."""
    rel = set(relevant)
    for rank, path in enumerate(ranked_paths, start=1):
        if path in rel:
            return 1.0 / rank
    return 0.0


def ndcg_at_k(relevant: Sequence[str], ranked_paths: Sequence[str], k: int = 3) -> float:
    """nDCG@k with binary document-level relevance.

    Oasis returns chunk-level hits, so the same path may appear several times;
    a path is credited only at its first occurrence.
    """
    rel = set(relevant)
    dcg = 0.0
    seen: set[str] = set()
    for rank, path in enumerate(ranked_paths[:k], start=1):
        if path in rel and path not in seen:
            dcg += 1.0 / math.log2(rank + 1)
            seen.add(path)
    ideal = sum(1.0 / math.log2(rank + 1) for rank in range(1, min(len(rel), k) + 1))
    return dcg / ideal if ideal > 0.0 else 0.0


# ---------------------------------------------------------------------------
# Oasis driver
# ---------------------------------------------------------------------------

def run_oasis(root: str, query: str, k: int, mode: str) -> List[Dict[str, Any]]:
    """Run `oasis search` for one query; return the parsed hit list."""
    cmd = ["oasis", "--root", root, "search", query, "--json", "-k", str(k)]
    if mode == "lexical":
        cmd.append("--lexical-only")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"oasis failed ({proc.returncode}): {proc.stderr.strip()}")
    return json.loads(proc.stdout)


def eval_query(query: str, relevant: Sequence[str], k: int, mode: str,
               root: str) -> Dict[str, Any]:
    """Run one query; return per-query metrics and details."""
    hits = run_oasis(root, query, k, mode)
    ranked = [str(h.get("path", "")) for h in hits]
    rel = set(relevant)
    rank_found = next((r for r, p in enumerate(ranked, start=1) if p in rel), None)
    return {
        "query": query,
        "rank_found": rank_found,
        "top_paths": ranked[:3],
        "recall@1": recall_at_k(relevant, ranked, 1),
        "recall@3": recall_at_k(relevant, ranked, 3),
        "recall@5": recall_at_k(relevant, ranked, 5),
        "recall@10": recall_at_k(relevant, ranked, 10),
        "mrr": mrr(relevant, ranked),
        "ndcg@3": ndcg_at_k(relevant, ranked),
    }


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------

def aggregate(results: List[Dict[str, Any]]) -> Dict[str, float]:
    """Mean of each per-query metric."""
    n = len(results)
    if n == 0:
        return {key: 0.0 for key in METRIC_KEYS}
    return {key: sum(float(r[key]) for r in results) / n for key in METRIC_KEYS}


def aggregate_by_section(rows: List[Dict[str, Any]],
                         results: List[Dict[str, Any]]) -> Dict[str, Dict[str, float]]:
    """Aggregate metrics per section label."""
    buckets: Dict[str, List[Dict[str, Any]]] = {}
    for row, result in zip(rows, results):
        buckets.setdefault(str(row.get("section", "?")), []).append(result)
    return {sec: aggregate(sub) for sec, sub in sorted(buckets.items())}


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_table(metrics: Dict[str, float],
                per_section: Dict[str, Dict[str, float]],
                results: List[Dict[str, Any]],
                verbose: bool) -> None:
    """Print the aligned summary table (and misses when verbose)."""
    print()
    print(f"{'metric':<12} {'value':>8}")
    print("-" * 22)
    for key in METRIC_KEYS:
        print(f"{key:<12} {metrics[key]:>8.3f}")
    if per_section:
        print()
        print(f"{'section':<12} {'recall@3':>9} {'mrr':>7} {'ndcg@3':>8}")
        print("-" * 40)
        for sec, m in per_section.items():
            print(f"{sec:<12} {m['recall@3']:>9.3f} {m['mrr']:>7.3f} {m['ndcg@3']:>8.3f}")
    if verbose:
        misses = [r for r in results if r["rank_found"] is None]
        if misses:
            print()
            for r in misses:
                print(f"MISS query={r['query']!r} top3={r['top_paths']}")


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------

def get_git_sha() -> str:
    """Short sha of HEAD, or 'unknown' outside a git repo."""
    try:
        out = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=False)
        return out.stdout.strip() if out.returncode == 0 else "unknown"
    except OSError:
        return "unknown"


def count_pages(root: str) -> int:
    """Count *.md files under the wiki root."""
    return sum(1 for p in Path(root).rglob("*.md") if p.is_file())


def sha1_file(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()


def append_history(root: str, mode: str, k: int, n_queries: int,
                   metrics: Dict[str, float],
                   per_section: Dict[str, Dict[str, float]],
                   queries_file: Path) -> None:
    """Append one history line; single write + flush so it lands atomically."""
    entry = {
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "git_sha": get_git_sha(),
        "mode": mode,
        "k": k,
        "n_queries": n_queries,
        "n_pages": count_pages(root),
        "metrics": metrics,
        "per_section": per_section,
        "queries_file_sha": sha1_file(queries_file),
    }
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, sort_keys=True) + "\n")
        f.flush()


def load_previous_metrics(mode: str) -> Optional[Dict[str, float]]:
    """Most recent history entry's metrics for this mode, if any."""
    if not HISTORY_PATH.exists():
        return None
    prev: Optional[Dict[str, float]] = None
    for line in HISTORY_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get("mode") == mode and isinstance(entry.get("metrics"), dict):
            prev = entry["metrics"]
    return prev


def compare_with_history(mode: str, metrics: Dict[str, float]) -> int:
    """Regression gate: exit 1 if recall@3 dropped by more than 0.02."""
    prev = load_previous_metrics(mode)
    if prev is None:
        print("compare: no previous history entry for this mode")
        return 0
    prev_r3 = float(prev.get("recall@3", 0.0))
    delta = metrics["recall@3"] - prev_r3
    print(f"compare: recall@3 {prev_r3:.3f} -> {metrics['recall@3']:.3f} (delta {delta:+.3f})")
    if delta < -0.02:
        print(f"REGRESSION: recall@3 dropped by more than 0.02", file=sys.stderr)
        return 1
    return 0


def write_latest(root: str, mode: str, k: int, rows: List[Dict[str, Any]],
                 results: List[Dict[str, Any]], metrics: Dict[str, float],
                 per_section: Dict[str, Dict[str, float]]) -> None:
    """Write per-query details to evals/results/latest-<mode>.json."""
    payload = {
        "mode": mode,
        "k": k,
        "root": root,
        "n_queries": len(rows),
        "n_pages": count_pages(root),
        "metrics": metrics,
        "per_section": per_section,
        "per_query": [
            {
                "id": row.get("id", ""),
                "query": row.get("query", ""),
                "relevant": row.get("relevant", []),
                "section": row.get("section", ""),
                "rank_found": result["rank_found"],
                "top_paths": result["top_paths"],
                "metrics": {key: result[key] for key in METRIC_KEYS},
            }
            for row, result in zip(rows, results)
        ],
    }
    out_path = HISTORY_PATH.parent / f"latest-{mode}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_queries(queries_path: Path, section: Optional[str]) -> List[Dict[str, Any]]:
    """Load JSONL query rows, optionally filtered by section substring."""
    rows: List[Dict[str, Any]] = []
    for line in queries_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        row = json.loads(line)
        if section is not None and section not in str(row.get("section", "")):
            continue
        rows.append(row)
    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="run_eval.py",
        description="Search-quality eval harness for the oasis CLI")
    parser.add_argument("--root", default="wiki", help="wiki root directory (default wiki)")
    parser.add_argument("--queries", default="evals/queries.jsonl",
                        help="queries JSONL file (default evals/queries.jsonl)")
    parser.add_argument("-k", type=int, default=10, help="top-k cutoff (default 10)")
    parser.add_argument("--mode", choices=["hybrid", "lexical"], default="hybrid",
                        help="hybrid (dense+lexical) or lexical-only search (default hybrid)")
    parser.add_argument("--section", default=None,
                        help="only evaluate rows whose section contains this substring")
    parser.add_argument("--verbose", action="store_true",
                        help="print each miss with its top-3 paths")
    parser.add_argument("--compare", action="store_true",
                        help="compare with the most recent history entry of the same mode; "
                             "exit 1 if recall@3 dropped by more than 0.02")
    parser.add_argument("--no-history", action="store_true",
                        help="do not append to evals/results/history.jsonl")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    queries_path = Path(args.queries)
    if not queries_path.exists():
        print(f"error: queries file not found: {queries_path}", file=sys.stderr)
        return 2
    if not Path(args.root).is_dir():
        print(f"error: wiki root not found: {args.root}", file=sys.stderr)
        return 2

    rows = load_queries(queries_path, args.section)
    if not rows:
        print("error: no queries to evaluate (check --section filter)", file=sys.stderr)
        return 2

    print(f"running {len(rows)} queries (mode={args.mode}, k={args.k}, root={args.root})")
    results: List[Dict[str, Any]] = []
    for row in rows:
        results.append(eval_query(row["query"], row.get("relevant", []),
                                  args.k, args.mode, args.root))

    metrics = aggregate(results)
    per_section = aggregate_by_section(rows, results)
    print_table(metrics, per_section, results, args.verbose)
    write_latest(args.root, args.mode, args.k, rows, results, metrics, per_section)

    if not args.no_history:
        append_history(args.root, args.mode, args.k, len(rows), metrics,
                       per_section, queries_path)

    if args.compare:
        return compare_with_history(args.mode, metrics)
    return 0


if __name__ == "__main__":
    sys.exit(main())
