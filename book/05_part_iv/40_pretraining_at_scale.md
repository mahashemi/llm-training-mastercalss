# Chapter 40 — Pretraining at Scale

**Part:** Part III

## Core concepts
1. **Token budget** — Total training tokens are a first-order driver of compute.
2. **Throughput** — Measured tokens/sec converts compute into wall time.
3. **Utilization** — Peak hardware specs are not delivered performance.
4. **Fault tolerance** — Large runs require restart and recovery planning.

## Formal view
A first-order dense-model training estimate is C≈6ND FLOPs, where N is parameters and D is training tokens. Actual compute depends on architecture and implementation.

## Engineering workflow
Baseline → intervention → evaluation → profiling → failure analysis → decision.

## Laboratory
[resource_accounting_flops_memory.ipynb](../../notebooks/resource_accounting_flops_memory.ipynb)

## Critical thinking
**Question:** What could make the method appear to work while the real objective gets worse?

**Answer:** Proxy optimization, data leakage, benchmark contamination, distribution shift, or resource-side regressions can all produce misleading gains.

**Question:** What should the next experiment be?

**Answer:** The cheapest experiment that tests the highest-impact uncertainty.

## Research prompt
State a falsifiable claim and design a minimum-cost test that could reject it.

## References
https://arxiv.org/abs/2203.15556
