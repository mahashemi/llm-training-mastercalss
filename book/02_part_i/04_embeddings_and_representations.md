# Chapter 4 — Embeddings and Representations

**Part:** Part I

## Core idea

This chapter turns the topic into an engineering concept: what problem it solves, what assumptions it makes, what changes in the model or system, and what evidence is needed before trusting it.

## Concepts

1. **Embedding table** — Maps discrete token IDs to dense vectors.
2. **Representation geometry** — Similarity in vector space can reflect learned relationships.
3. **Weight tying** — The input embedding matrix and output projection can share parameters in some architectures.

## Formal view

For token ID i, e_i=E[i]. If E∈R^{V×d}, each token receives a d-dimensional learned representation.

## Practical method

1. Establish a baseline.
2. Change one major variable.
3. Measure the target metric and relevant resource metrics.
4. Inspect representative failures.
5. Repeat only when the result justifies the additional cost.

## Laboratory

[build_a_tiny_transformer.ipynb](../../notebooks/build_a_tiny_transformer.ipynb)

## Critical thinking

**Question:** What is the tempting but wrong shortcut here?

**Answer:** Applying the technique without identifying the bottleneck it is meant to address. A method can improve a proxy while making the actual application worse.

**Question:** What evidence should be recorded?

**Answer:** Configuration, data/model versions, hardware, evaluation protocol, metrics, runtime/resource observations, and limitations.

## Research question

What controlled experiment would distinguish the mechanism described here from a simpler explanation?

## References

https://arxiv.org/abs/1706.03762
