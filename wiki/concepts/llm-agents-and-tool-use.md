---
title: LLM Agents and Tool Use
type: concept
section: "6.4"
level: 400
tags: [llm-agents, tool-use, react, function-calling, rag, planning, agentic]
sources: [nlp-and-llm-courses-texts-and-seminal-papers]
summary: Turning a language model into an agent that acts — tool/function calling, the reason-act (ReAct) loop, retrieval augmentation, planning and memory, and the failure modes of multi-step autonomy.
---

# LLM Agents and Tool Use
**In one sentence.** An LLM agent is a language model placed in a loop where it can call
external tools (search, code execution, APIs), observe the results, and decide the next
action — extending a text predictor into a system that takes actions in the world.

## Why it matters
A bare LLM only emits text and is frozen at its training cutoff; giving it tools lets it
fetch current information, do exact computation, and change external state — the basis of
coding assistants, research agents, and this project's own delegation to
[[large-language-models]]. It is also where reliability and safety concerns sharpen.

## How it works
**Tool / function calling.** The model is given tool schemas (name, description,
arguments). Instead of answering directly, it emits a structured call; a harness executes
the tool and returns the result as an observation the model reads on the next turn. This
grounds the model in real computation rather than its parametric guesses.

**The reason-act loop (ReAct).** Interleave **reasoning** ("I should look up X") with
**acting** (call a tool) and **observing** (read the result), repeating until done:

```
Thought → Action(tool, args) → Observation → Thought → … → Answer
```

Explicit intermediate reasoning ([[large-language-models]]-style chain-of-thought) plus
grounded observations reduce hallucination versus answering in one shot.

**Retrieval augmentation (RAG).** Fetch relevant documents with
[[dense-retrieval-and-embeddings]] / [[hybrid-search-and-rank-fusion]] and put them in
the context, so the model answers from retrieved facts rather than memory — the most
reliable tool pattern and the reason search engines like [[oasis-search-engine]] pair
with LLMs.

**Planning & memory.** For multi-step tasks the agent may plan (decompose into subgoals),
keep **memory** (scratchpad, or external store for long horizons), and sometimes
**reflect** (critique and retry). Multi-agent setups assign roles and let agents call
each other.

## Complexity & trade-offs
- Tools trade latency and complexity for grounding and capability; each tool call is a
  round trip and a place to fail.
- More autonomy (longer loops, more tools) increases capability but compounds error and
  cost — a small per-step error rate becomes large over many steps.
- RAG is cheaper and more controllable than fine-tuning for injecting knowledge, but
  depends entirely on retrieval quality (see [[evaluation-of-ir-systems]]).

## Pitfalls & gotchas
- **Error compounding** — an agent that is 95% reliable per step is ~60% over 10 steps;
  keep loops short, verify, and checkpoint.
- **Hallucinated tool calls / arguments** — validate against schemas; never trust an
  unverified action, especially destructive ones.
- **Prompt injection** — tool results and retrieved documents are untrusted input that can
  hijack the agent; isolate and sanitize (a [[security-principles]] problem).
- **Unbounded loops / cost** — cap iterations and budget; agents can spin.
- **Over-agentization** — many tasks are better as a single grounded call than a
  multi-step agent.

## Worked example
"What changed in this repo's auth code and is it tested?" A one-shot LLM would guess. An
agent instead calls a search tool for the auth files, reads them (observation), calls a
test-runner tool, observes failures, and only then answers with grounded specifics —
each step's output feeding the next decision in a ReAct loop.

## Related
- [[large-language-models]] — the model at the agent's core.
- [[dense-retrieval-and-embeddings]] — retrieval augmentation (RAG).
- [[hybrid-search-and-rank-fusion]] — the retrieval an agent calls.
- [[oasis-search-engine]] — a search tool an agent can use on this corpus.
- [[security-principles]] — prompt injection and untrusted tool output.

## Sources
Distilled from [[nlp-and-llm-courses-texts-and-seminal-papers]] (ReAct; Toolformer;
RAG; agent literature).
