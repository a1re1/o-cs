#!/usr/bin/env python3
"""Tests for the eval harness: metric functions + one end-to-end fixture run.

Unit tests import the metric functions from evals/run_eval.py (hand-computed
cases). The integration test runs evals/run_eval.py as a subprocess in
--mode lexical against tests/fixtures/wiki with --no-history and asserts the
JSON summary shows recall@10 == 0.75 (3 of the 4 fixture queries hit; the
fourth is a deliberate hard miss).
"""

from __future__ import annotations

import json
import math
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Make evals/run_eval.py importable as a plain module.
sys.path.insert(0, str(REPO_ROOT / "evals"))

import run_eval  # noqa: E402


class RecallAtKTests(unittest.TestCase):
    def test_hit_in_top_k(self) -> None:
        self.assertEqual(run_eval.recall_at_k(["a"], ["a", "b", "c"], 1), 1.0)

    def test_miss_at_k1_hit_at_k3(self) -> None:
        self.assertEqual(run_eval.recall_at_k(["a"], ["b", "c", "a"], 1), 0.0)
        self.assertEqual(run_eval.recall_at_k(["a"], ["b", "c", "a"], 3), 1.0)

    def test_empty_relevant_is_zero(self) -> None:
        self.assertEqual(run_eval.recall_at_k([], ["a", "b"], 3), 0.0)

    def test_empty_results_is_zero(self) -> None:
        self.assertEqual(run_eval.recall_at_k(["a"], [], 3), 0.0)

    def test_any_relevant_hit_counts_binary(self) -> None:
        self.assertEqual(run_eval.recall_at_k(["x", "c"], ["a", "b", "c"], 3), 1.0)

    def test_hit_below_cutoff_is_miss(self) -> None:
        self.assertEqual(run_eval.recall_at_k(["d"], ["a", "b", "c"], 3), 0.0)


class MrrTests(unittest.TestCase):
    def test_first_rank(self) -> None:
        self.assertEqual(run_eval.mrr(["a"], ["a", "b", "c"]), 1.0)

    def test_second_rank(self) -> None:
        self.assertEqual(run_eval.mrr(["b"], ["a", "b", "c"]), 0.5)

    def test_third_rank(self) -> None:
        self.assertAlmostEqual(run_eval.mrr(["c"], ["a", "b", "c"]), 1.0 / 3.0)

    def test_no_hit_is_zero(self) -> None:
        self.assertEqual(run_eval.mrr(["z"], ["a", "b", "c"]), 0.0)
        self.assertEqual(run_eval.mrr(["a"], []), 0.0)

    def test_uses_first_relevant_hit(self) -> None:
        self.assertEqual(run_eval.mrr(["b", "c"], ["a", "c", "b"]), 0.5)


class NdcgAtKTests(unittest.TestCase):
    def test_perfect_ranking(self) -> None:
        self.assertEqual(run_eval.ndcg_at_k(["a", "b"], ["a", "b", "c"], 3), 1.0)

    def test_relevant_at_rank_one(self) -> None:
        self.assertEqual(run_eval.ndcg_at_k(["a"], ["a", "b", "c"], 3), 1.0)

    def test_relevant_at_rank_two(self) -> None:
        # DCG = 1/log2(2+1); IDCG = 1/log2(1+1) = 1.
        self.assertAlmostEqual(
            run_eval.ndcg_at_k(["b"], ["a", "b", "c"], 3), 1.0 / math.log2(3))

    def test_relevant_at_rank_three(self) -> None:
        # DCG = 1/log2(3+1) = 0.5; IDCG = 1.
        self.assertAlmostEqual(run_eval.ndcg_at_k(["c"], ["a", "b", "c"], 3), 0.5)

    def test_miss_is_zero(self) -> None:
        self.assertEqual(run_eval.ndcg_at_k(["z"], ["a", "b", "c"], 3), 0.0)

    def test_duplicate_chunk_credited_once(self) -> None:
        # Same path twice in the ranking counts only at its first occurrence.
        self.assertEqual(run_eval.ndcg_at_k(["a"], ["a", "a", "b"], 3), 1.0)

    def test_more_relevant_docs_than_k(self) -> None:
        # DCG = 1/log2(3); IDCG = 1/log2(2) + 1/log2(3) over min(3 relevant, k=2).
        expected = (1.0 / math.log2(3)) / (1.0 + 1.0 / math.log2(3))
        self.assertAlmostEqual(
            run_eval.ndcg_at_k(["a", "b", "c"], ["d", "a", "e"], 2), expected)

    def test_default_k_is_three(self) -> None:
        self.assertEqual(run_eval.ndcg_at_k(["c"], ["a", "b", "c"]), 0.5)


@unittest.skipUnless(shutil.which("oasis"), "oasis CLI not found on PATH")
class IntegrationTests(unittest.TestCase):
    def test_fixture_run_recall_at_10_is_075(self) -> None:
        """Lexical eval over the fixture wiki: 3 of 4 queries hit, one hard miss."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            proc = subprocess.run(
                [
                    sys.executable, str(REPO_ROOT / "evals" / "run_eval.py"),
                    "--root", str(REPO_ROOT / "tests" / "fixtures" / "wiki"),
                    "--queries", str(REPO_ROOT / "tests" / "fixtures" / "queries.jsonl"),
                    "--mode", "lexical",
                    "--no-history",
                ],
                cwd=tmp,
                capture_output=True,
                text=True,
                timeout=300,
            )
            self.assertEqual(
                proc.returncode, 0,
                f"run_eval.py exited {proc.returncode}\nstdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}")
            latest = tmp_path / "evals" / "results" / "latest-lexical.json"
            self.assertTrue(
                latest.exists(),
                f"latest-lexical.json not written\nstdout:\n{proc.stdout}")
            payload = json.loads(latest.read_text(encoding="utf-8"))
            self.assertEqual(payload["n_queries"], 4)
            self.assertEqual(payload["metrics"]["recall@10"], 0.75)


if __name__ == "__main__":
    unittest.main()
