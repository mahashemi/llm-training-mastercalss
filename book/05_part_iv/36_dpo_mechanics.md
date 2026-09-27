# Chapter 36 — DPO Mechanics

**Part:** Part IV

## Core concepts
1. **Reference model** — Defines a baseline preference relationship.
2. **Log-probability differences** — Preference learning uses relative likelihoods.
3. **Temperature/beta** — Controls the strength of preference optimization.
4. **Failure modes** — Preference labels can be noisy or narrow.

## Formal view
A common DPO objective uses log σ(β[(logπ(y_w|x)-logπ_ref(y_w|x))-(logπ(y_l|x)-logπ_ref(y_l|x))]).

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
https://arxiv.org/abs/2305.18290
