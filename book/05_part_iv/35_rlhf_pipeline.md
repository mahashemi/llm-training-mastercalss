# Chapter 35 — RLHF Pipeline

**Part:** Part IV

## Core concepts
1. **SFT seed model** — Start alignment training from a useful supervised model.
2. **Reward model** — Predict human preference from rankings.
3. **Policy optimization** — Update the model toward higher reward while constraining drift.
4. **Operational complexity** — Online sampling and reward loops raise engineering cost.

## Formal view
Classic RLHF can be decomposed into supervised initialization, reward modeling, and policy optimization. Each component introduces its own data and stability failure modes.

## Engineering workflow
Baseline → intervention → evaluation → profiling → failure analysis → decision.

## Laboratory
[dpo_and_distillation_concepts.ipynb](../../notebooks/dpo_and_distillation_concepts.ipynb)

## Critical thinking
**Question:** What could make the method appear to work while the real objective gets worse?

**Answer:** Proxy optimization, data leakage, benchmark contamination, distribution shift, or resource-side regressions can all produce misleading gains.

**Question:** What should the next experiment be?

**Answer:** The cheapest experiment that tests the highest-impact uncertainty.

## Research prompt
State a falsifiable claim and design a minimum-cost test that could reject it.

## References
https://arxiv.org/abs/2203.02155
