# Chapter 7 — Feed-Forward Networks and SwiGLU

**Part:** Part I

## Core idea

This chapter turns the topic into an engineering concept: what problem it solves, what assumptions it makes, what changes in the model or system, and what evidence is needed before trusting it.

## Concepts

1. **MLP block** — Provides token-wise nonlinear transformation after attention.
2. **Gating** — Controls information flow through multiplicative interactions.
3. **SwiGLU** — A gated MLP variant used in many modern LLMs.

## Formal view

A typical gated block is y = W2(SiLU(W1x) ⊙ W3x). Parameter count and intermediate width strongly affect compute.

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

https://arxiv.org/abs/2002.05202
