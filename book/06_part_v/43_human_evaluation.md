# Chapter 43 — Human Evaluation

**Part:** Part V

## Core concepts
1. **Rubrics** — Turn vague preference into explicit criteria.
2. **Pairwise comparison** — Often easier for annotators than absolute scores.
3. **Agreement** — Measure consistency and ambiguous cases.
4. **Sampling** — Use representative prompts, not only spectacular examples.

## Formal view
For pairwise preference, the observed rate can be summarized with confidence intervals; avoid interpreting a small difference without uncertainty.

## Practice
Use a controlled baseline. Change one principal variable. Measure both the target metric and resource metrics. Inspect failures before interpreting the aggregate.

## Laboratory
[failure_analysis_and_safety_eval.ipynb](../../notebooks/failure_analysis_and_safety_eval.ipynb)

## Critical thinking
**Question:** What would falsify the conclusion?  
**Answer:** A controlled experiment in a different regime, an evaluation correction, a failure bucket hidden by aggregation, or a resource/regression tradeoff can overturn an apparent result.

**Question:** What should a learner leave with?  
**Answer:** A reusable decision rule plus the ability to explain its assumptions and boundaries.

## Research prompt
Design a minimally sufficient experiment that separates cause from correlation.

## References
https://arxiv.org/abs/2203.02155
