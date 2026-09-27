# Chapter 58 — RAG Architecture

**Part:** Part VII

## Core concepts
1. **Indexing** — Turn documents into retrievable units and representations.
2. **Retrieval** — Select evidence for a query.
3. **Generation** — Condition the model on retrieved evidence.
4. **Evaluation** — Measure retrieval recall separately from generation quality.

## Formal view
RAG performance is a composition of retrieval recall, context quality, model use of evidence, and response evaluation. Diagnose each stage.

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
