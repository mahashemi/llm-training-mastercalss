# Chapter 53 — Serving with vLLM

**Part:** Part VI

## Core concepts
1. **PagedAttention** — Manage KV cache in blocks rather than contiguous allocations.
2. **Continuous batching** — Admit new requests while others are decoding.
3. **Throughput** — Measure output tokens/sec at a specified concurrency.
4. **Latency** — Track time-to-first-token and inter-token latency separately.

## Formal view
A serving benchmark is a function of request distribution, prompt/output length, concurrency, model, precision, hardware, and scheduling policy.

## Practice
Define the operational objective, freeze the baseline, run the smallest informative experiment, record resource use, inspect failures, and decide whether the next intervention is justified.

## Laboratory
[inference_and_kv_cache.ipynb](../../notebooks/inference_and_kv_cache.ipynb)

## Critical thinking
**Question:** What can a benchmark or metric hide?  
**Answer:** Distribution shift, severe but rare failures, cost/latency regressions, and behavior outside the tested task.

**Question:** What makes this research-grade?  
**Answer:** Clear hypothesis, controlled comparison, versioned inputs, reproducible procedure, quantitative evidence, uncertainty/limitations, and enough detail for another team to repeat it.

## Research prompt
Propose one ablation and one failure-analysis experiment.

## References
https://docs.vllm.ai/en/stable/
