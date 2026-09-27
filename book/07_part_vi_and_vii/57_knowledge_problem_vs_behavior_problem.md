# Chapter 57 — Knowledge Problem vs Behavior Problem

**Part:** Part VII

## Core concepts
1. **Knowledge** — Facts or documents that may change over time.
2. **Behavior** — How the model responds, formats, reasons, or follows a stable procedure.
3. **Retrieval** — Provides external knowledge at inference time.
4. **Training** — Changes parameters and learned behavior.

## Formal view
A useful diagnostic asks whether the desired change is in p(y|x) given fixed weights and external context, or whether the weights themselves must change.

## Practice
Define the operational objective, freeze the baseline, run the smallest informative experiment, record resource use, inspect failures, and decide whether the next intervention is justified.

## Laboratory
[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## Critical thinking
**Question:** What can a benchmark or metric hide?  
**Answer:** Distribution shift, severe but rare failures, cost/latency regressions, and behavior outside the tested task.

**Question:** What makes this research-grade?  
**Answer:** Clear hypothesis, controlled comparison, versioned inputs, reproducible procedure, quantitative evidence, uncertainty/limitations, and enough detail for another team to repeat it.

## Research prompt
Propose one ablation and one failure-analysis experiment.

## References
https://docs.vllm.ai/en/stable/
