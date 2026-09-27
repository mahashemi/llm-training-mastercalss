# Chapter 51 — Inference Graphs and Prefill

**Part:** Part VI

## Core concepts
1. **Prefill** — Process the existing prompt to build hidden states and KV cache.
2. **Decode** — Generate one or more new tokens step by step.
3. **Batching** — Combine compatible requests to improve hardware utilization.
4. **Prompt length** — Long inputs can dominate time-to-first-token.

## Formal view
Total latency can be decomposed into prefill and decode components. Their scaling differs with prompt length, output length, and batching.

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
