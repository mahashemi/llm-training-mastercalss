# Chapter 72 — Training Data Governance

**Part:** Part VIII

## Core concepts
1. **Provenance** — Track where data came from and what transformations were applied.
2. **Access rights** — Document why data can be used for training.
3. **Sensitive data** — Minimize collection and apply appropriate controls.
4. **Versioning** — Freeze dataset versions for comparable experiments.

## Formal view
Treat each dataset as a versioned artifact with an immutable identifier. A result without a dataset version is difficult to reproduce scientifically.

## Practice
Produce an auditable artifact, not only a narrative: baseline, experiment, result, resource accounting, risks, and next action.

## Laboratory
[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## Critical thinking
**Question:** What would convince a skeptical reviewer?  
**Answer:** A clearly defined claim, appropriate baseline, reproducible procedure, quantitative evidence, failure analysis, and limitations.

**Question:** What should be published even when the result is negative?  
**Answer:** The hypothesis, experimental setup, observed outcome, and explanation of what the evidence does and does not support.

## Research prompt
Turn this chapter into a one-page experiment or proposal suitable for peer review.

## References
https://arxiv.org/abs/2402.00159
