# Chapter 47 — Statistical Thinking for LLM Evaluation

**Part:** Part V

## Core concepts
1. **Sampling error** — Observed benchmark scores are estimates.
2. **Paired tests** — Use paired examples when comparing models on the same items.
3. **Bootstrap** — Estimate uncertainty without strong distributional assumptions.
4. **Practical significance** — A statistically detectable change may still be operationally irrelevant.

## Formal view
For paired evaluation, calculate per-example differences and bootstrap their mean/median to obtain an empirical uncertainty interval.

## Practice
Use a controlled baseline. Change one principal variable. Measure both the target metric and resource metrics. Inspect failures before interpreting the aggregate.

## Laboratory
[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Critical thinking
**Question:** What would falsify the conclusion?  
**Answer:** A controlled experiment in a different regime, an evaluation correction, a failure bucket hidden by aggregation, or a resource/regression tradeoff can overturn an apparent result.

**Question:** What should a learner leave with?  
**Answer:** A reusable decision rule plus the ability to explain its assumptions and boundaries.

## Research prompt
Design a minimally sufficient experiment that separates cause from correlation.

## References
https://cs336.stanford.edu/
