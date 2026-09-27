# Chapter 44 — Model-as-Judge Evaluation

**Part:** Part V

## Core concepts
1. **Scalable judging** — Use another model to score outputs.
2. **Judge bias** — The judge can share biases with the candidate.
3. **Calibration** — Compare judge decisions with human labels.
4. **Prompt sensitivity** — Judge instructions influence outputs.

## Formal view
Let J(x,y) be a judge score. Reliability depends on correlation with human judgments under the same evaluation distribution; it is not self-validating.

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
