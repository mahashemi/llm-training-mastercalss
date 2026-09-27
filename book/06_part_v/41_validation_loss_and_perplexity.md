# Chapter 41 — Validation Loss and Perplexity

**Part:** Part V

## Core concepts
1. **Validation loss** — Estimate generalization on held-out token sequences.
2. **Perplexity** — exp(average negative log-likelihood) for token-level language modeling.
3. **Task mismatch** — Lower perplexity does not guarantee better downstream behavior.
4. **Checkpoint selection** — Choose based on predeclared evaluation criteria.

## Formal view
PPL=exp(L) where L is average negative log-likelihood in nats/token. Use validation loss for training monitoring and task metrics for application decisions.

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
