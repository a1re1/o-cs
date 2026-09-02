---
title: ML systems, MLOps and data engineering — Huyen's Designing Machine Learning Systems and Stanford CS329S, CMU 10-714 Deep Learning Systems (build a framework from scratch), Full Stack Deep Learning, MIT 6.5940 TinyML & Efficient Deep Learning (Han), Made With ML, Burkov's ML Engineering (free), Reis & Housley's Fundamentals of Data Engineering; Sculley et al. "Hidden Technical Debt", TensorFlow, PyTorch, TVM, Megatron-LM, ZeRO, pipeline parallelism, vLLM/PagedAttention, GPTQ, QLoRA
type: source
section: "6.9"
level: 400
tags: [huyen, designing-machine-learning-systems, cs329s, 10-714, deep-learning-systems, kolter, zico, full-stack-deep-learning, 6-5940, tinyml, efficient-deep-learning, song-han, made-with-ml, burkov, machine-learning-engineering, reis-housley, fundamentals-of-data-engineering, sculley, hidden-technical-debt, tensorflow, abadi, pytorch, paszke, tvm, chen, megatron-lm, shoeybi, zero, rajbhandari, deepspeed, pipeline-parallelism, narayanan, gpipe, vllm, kwon, pagedattention, gptq, frantar, qlora, dettmers]
sources: []
authors: [Chip Huyen, Zico Kolter, Tianqi Chen, Song Han, Andriy Burkov, Joe Reis, Matt Housley, D. Sculley, Martín Abadi, Adam Paszke, Mohammad Shoeybi, Samyam Rajbhandari, Deepak Narayanan, Woosuk Kwon, Elias Frantar, Tim Dettmers]
year: 2022
institution: Stanford / CMU / MIT
url: https://stanford-cs329s.github.io/syllabus.html
license: mixed (CS329S notes, 10-714, FSDL, 6.5940, Made With ML, Burkov free)
format: html
summary: Stanford CS329S (Huyen; notes open) and her book Designing Machine Learning Systems teach ML as a production system — understanding ML in production, ML and data systems fundamentals, training data (sampling, labelling, class imbalance, augmentation), feature engineering (leakage, scaling, feature stores), model development and training, offline evaluation, deployment (batch vs online, edge vs cloud), diagnosing failures, data distribution shifts and monitoring, continual learning and test in production, infrastructure and tooling, and responsible AI; CMU 10-714 (Kolter & Chen) has students build a full deep-learning framework — autodiff, tensors, GPU kernels, optimizers, modules, data loaders — from scratch (needle); Full Stack Deep Learning covers the lifecycle tooling (experiment tracking, data management, testing, deployment, monitoring); MIT 6.5940 (Han) is efficient deep learning — pruning, quantization, neural architecture search, knowledge distillation, efficient transformers/LLMs, on-device training, TinyML; Made With ML and Burkov's ML Engineering are the practitioner playbooks and Reis & Housley the data-engineering lifecycle (ingestion, storage, transformation, serving, with data quality and orchestration); and the seminal papers are Sculley et al.'s "Hidden Technical Debt in ML Systems" (2015 — the ML code is the small box in the middle; entanglement, hidden feedback loops, pipeline jungles, configuration debt), the TensorFlow (2016) and PyTorch (2019) framework designs (static dataflow graphs vs define-by-run imperative autograd), TVM (2018 — an end-to-end compiler stack with learned schedule search), Megatron-LM (tensor parallelism inside transformer layers), ZeRO (2020 — partitioning optimizer state, gradients and parameters across data-parallel workers), GPipe/PipeDream pipeline parallelism, vLLM's PagedAttention (2023), GPTQ post-training quantization and QLoRA.
---
# ML systems, MLOps, and data engineering: sources

## What they are
- **Huyen, Designing ML Systems / CS329S** (syllabus read: understanding ML production; ML
  and data systems fundamentals — with a Twitter trending-hashtags design exercise; training
  data; feature engineering; model selection, development and training; offline evaluation;
  deployment; diagnosis of failures, distribution shifts and monitoring; continual learning
  and test in production; infrastructure and tooling; responsible AI; guest lectures on
  MLOps in practice). The book's thesis: ML systems are data systems whose requirements
  (reliability, scalability, maintainability, adaptability) dominate model choice, and
  the iterative loop (project scoping → data → model → deploy → monitor → back to data) never
  ends. **Burkov, ML Engineering** (free): the same lifecycle compressed. **Made With ML**
  (Goku Mohandas): a full MLOps project (design, data, modelling, testing, serving, CI/CD)
  with code. **Full Stack Deep Learning** (Berkeley/UW): ML teams and projects, data
  management, training and debugging, experiment management, deployment, monitoring,
  "LLM bootcamp". **Reis & Housley, Fundamentals of Data Engineering** (2022): the data-
  engineering lifecycle (generation → ingestion → storage → transformation → serving) and
  its undercurrents (security, data management, DataOps, architecture, orchestration,
  software engineering); batch vs streaming, lakehouses, dbt/Airflow-style tooling.
- **CMU 10-714, Deep Learning Systems** (Kolter & Chen; free): ML refresher, manual and
  automatic differentiation (reverse-mode, the `needle` framework), hardware acceleration
  (CPU/GPU, matmul tiling), NN library abstractions (modules, optimizers, initialization),
  data loading and normalization, CNN/RNN/transformer implementations, generative
  models, model deployment (compilation, TVM/Relay) — students write the whole stack.
  **MIT 6.5940 TinyML & Efficient DL** (Han): basics of NN efficiency (MACs, latency,
  memory), **pruning** and sparsity, **quantization** (PTQ, QAT, INT8/INT4, mixed precision,
  AWQ/SmoothQuant), **neural architecture search** and once-for-all networks, **knowledge
  distillation**, efficient transformers and LLMs (KV-cache compression, speculative
  decoding), on-device training, TinyML on microcontrollers (MCUNet), diffusion/video
  efficiency. **Berkeley CS294 AI-Sys**: the reading list (frameworks, compilers,
  distributed training, serving, autoML, RL systems).
- **Seminal**: Sculley et al. 2015 (**hidden technical debt**: boundary erosion/entanglement
  — CACE, "changing anything changes everything"; correction cascades; undeclared consumers;
  data dependencies costing more than code dependencies; hidden feedback loops; glue code
  and pipeline jungles; dead experimental codepaths; configuration debt; the ML code is a
  small box surrounded by data collection, verification, feature extraction, serving,
  monitoring); Abadi et al. 2016 (**TensorFlow**: dataflow graphs, device placement, XLA);
  Paszke et al. 2019 (**PyTorch**: imperative, define-by-run, tape-based autograd, C++ core,
  usability as the design goal); Chen et al. 2018 (**TVM**: graph-level and operator-level
  optimization, learned cost models for schedule search, portable to CPUs/GPUs/accelerators);
  Shoeybi et al. 2019 (**Megatron-LM**: intra-layer tensor parallelism splitting attention
  heads and MLP columns/rows with two all-reduces per layer); Rajbhandari et al. 2020 (**ZeRO**:
  stages 1–3 shard optimizer states, gradients, parameters — memory per GPU falls by the
  data-parallel degree; FSDP is PyTorch's version); Huang et al. 2019 (GPipe) and Narayanan
  et al. 2019/2021 (PipeDream, interleaved 1F1B — **pipeline parallelism**, bubbles, and the
  3D-parallel recipe for trillion-parameter training); Kwon et al. 2023 (**vLLM**: PagedAttention
  — KV-cache blocks managed like virtual memory, near-zero fragmentation, 2–4× throughput);
  Frantar et al. 2022 (**GPTQ**: one-shot 4-bit weight quantization via approximate second-order
  information); Dettmers et al. 2023 (**QLoRA** — [[llm-post-training-sft-rlhf-dpo]]).

## Key ideas → pages
[[mlops-and-ml-systems]], [[distributed-training-and-ml-systems]],
[[llm-inference-and-serving]]; existing: [[large-language-models]],
[[neural-network-training]], [[gpu-programming-cuda]], [[deep-learning-basics]].

## What they add
Huyen for the lifecycle and the failure modes nobody puts in ML courses (skew, drift,
feedback loops); 10-714 for the framework internals every practitioner should have built
once; Han for the efficiency toolkit that decides whether a model ships; the paper list for
how frontier-scale training and serving actually work (3D parallelism, ZeRO, paged KV).
