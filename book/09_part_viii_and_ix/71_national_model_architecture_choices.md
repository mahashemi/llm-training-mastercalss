# Chapter 71 — National Model Architecture Choices

**Part:** Part VIII

## Core concepts
1. **Dense vs MoE** — Compare operational simplicity, capacity, active compute, and distributed complexity.
2. **Context length** — Long context increases memory/compute and changes evaluation needs.
3. **Tokenizer ownership** — A national program may need to optimize representation for local languages.
4. **Open weights** — Consider reproducibility, deployment, and governance implications.

## Formal view
Architecture should be selected jointly with data, compute, serving, and objective. No architecture metric should be optimized in isolation.

## Practice
Produce an auditable artifact, not only a narrative: baseline, experiment, result, resource accounting, risks, and next action.

## Laboratory
[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## Critical thinking
**Question:** What would convince a skeptical reviewer?  
**Answer:** A clearly defined claim, appropriate baseline, reproducible procedure, quantitative evidence, failure analysis, and limitations.

**Question:** What should be published even when the result is negative?  
**Answer:** The hypothesis, experimental setup, observed outcome, and explanation of what the evidence does and does not support.

## Research prompt
Turn this chapter into a one-page experiment or proposal suitable for peer review.

## References
https://cs336.stanford.edu/
