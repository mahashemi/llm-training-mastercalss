# Chapter 48 — Hallucination and Groundedness

**Part:** Part V

## Core concepts
1. **Factuality** — Whether a claim matches the relevant evidence/world.
2. **Groundedness** — Whether the answer is supported by supplied context.
3. **Abstention** — Know when evidence is insufficient.
4. **Retrieval coupling** — Poor retrieval can cause apparent model hallucination.

## Formal view
Define groundedness relative to a context C: a claim is grounded if it is entailed or supported by C under a stated criterion. Do not confuse this with global factuality.

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
https://cs336.stanford.edu/
