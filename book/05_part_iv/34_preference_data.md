# Chapter 34 — Preference Data

**Part:** Part IV

## Core concepts
1. **Chosen/rejected pairs** — Provide relative quality information.
2. **Annotator agreement** — Measure whether preferences are reliable.
3. **Position bias** — Randomize presentation when possible.
4. **Preference scope** — Define what “better” means for the deployment objective.

## Formal view
Preference data estimates relative desirability rather than an absolute reward. Quality depends on task definition, annotator instructions, consistency, and sample diversity.

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
