# Chapter 11 — Multi-Head Attention Shapes

**Part:** Part I

## Core idea
1. **Head partitioning** — Split the hidden dimension into multiple attention subspaces.
2. **Projection matrices** — Q/K/V projections are learned linear maps.
3. **Concatenation** — Head outputs are merged and projected back to the model dimension.

## Formal view
For model width d and h heads, common designs use d_head=d/h. Attention cost is driven by B·h·T²·d_head.

## Practical method
Start with a baseline, change one major variable, measure quality and resource impact, inspect failures, and only then scale the experiment.

## Laboratory
[build_a_tiny_transformer.ipynb](../../notebooks/build_a_tiny_transformer.ipynb)

## Critical-thinking questions
**What is the tempting shortcut?** Apply the method before identifying the real bottleneck.  
**What is the answer?** Diagnose whether the limiting factor is data, objective, capacity, optimization, hardware, inference, or evaluation.  
**What evidence is required?** Versioned configuration, controlled comparison, target-specific metrics, representative failures, and explicit limitations.

## Research prompt
Design one controlled experiment that could falsify the central claim of this chapter.

## References
https://arxiv.org/abs/1706.03762
