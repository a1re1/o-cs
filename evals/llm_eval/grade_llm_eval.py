#!/usr/bin/env python3
"""Grade an LLM's answers to evals/llm_eval/questions.jsonl.

The model (lci/GLM-5.3-Flash) is asked to answer each question USING oasis and to
output one JSON object per question: {"id","answer","pages_cited":[...],"used_oasis":bool}.
This script joins those answers to the gold questions and scores, per question:
  - used_oasis:   did it call the search tool at all?
  - citation_hit: did pages_cited include at least one expected page?
  - point_recall: fraction of expected key points present (substring, case-insensitive)
                  in the answer text.
Overall it prints tool-use rate, citation hit rate, and mean point recall.

Usage: grade_llm_eval.py <answers.jsonl|answers.json>
answers may be a JSON array or one JSON object per line.
"""
import json, sys, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GOLD = os.path.join(HERE, "questions.jsonl")

def load_any(path):
    txt = open(path).read().strip()
    try:
        d = json.loads(txt)
        return d if isinstance(d, list) else [d]
    except json.JSONDecodeError:
        out = []
        for line in txt.splitlines():
            line = line.strip()
            if line:
                try: out.append(json.loads(line))
                except json.JSONDecodeError: pass
        return out

def slug(p):
    return os.path.splitext(os.path.basename(str(p)))[0]

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    gold = {json.loads(l)["id"]: json.loads(l) for l in open(GOLD)}
    ans = {a.get("id"): a for a in load_any(sys.argv[1]) if a.get("id")}

    rows, tool_used, cite_hit, precisions = [], 0, 0, []
    for qid, g in gold.items():
        a = ans.get(qid)
        if not a:
            rows.append((qid, "NO-ANSWER", 0, 0.0)); continue
        used = bool(a.get("used_oasis"))
        cited = {slug(p) for p in (a.get("pages_cited") or [])}
        expect = {slug(p) for p in g["expect_pages"]}
        hit = bool(cited & expect)
        text = (a.get("answer") or "").lower()
        pts = g.get("expect_points") or []
        pr = sum(1 for p in pts if p.lower() in text) / len(pts) if pts else 0.0
        tool_used += used; cite_hit += hit; precisions.append(pr)
        rows.append((qid, "cite:%s" % ("Y" if hit else "n"), int(used), round(pr, 2)))

    n = len(gold)
    print(f"{'id':<6}{'used_oasis':<12}{'citation':<10}{'point_recall'}")
    for qid, cite, used, pr in rows:
        print(f"{qid:<6}{('yes' if used else 'no'):<12}{cite:<10}{pr}")
    print("-" * 42)
    print(f"tool-use rate     {tool_used}/{n} = {tool_used/n:.2f}")
    print(f"citation hit rate {cite_hit}/{n} = {cite_hit/n:.2f}")
    print(f"mean point recall {sum(precisions)/n:.2f}")

if __name__ == "__main__":
    main()
