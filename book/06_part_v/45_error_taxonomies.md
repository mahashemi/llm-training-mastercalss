# Chapter 45 — Error Taxonomies

**Part:** Part V

## Core concepts
1. **Capability failure** — Model lacks the required skill or knowledge.
2. **Format failure** — Correct content but invalid structure.
3. **Grounding failure** — Claims lack evidence or contradict supplied evidence.
4. **Safety failure** — Unacceptable behavior under defined policy.

## Formal view
Partition total errors into mutually interpretable buckets so interventions can be targeted. A taxonomy is an engineering model of failure causes.

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
