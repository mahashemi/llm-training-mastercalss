# Chapter 8 — Causal Self-Attention

**Part:** Part I

## Core idea

This chapter turns the topic into an engineering concept: what problem it solves, what assumptions it makes, what changes in the model or system, and what evidence is needed before trusting it.

## Concepts

1. **Q/K/V** — Queries seek relevant information, keys describe what is available, values carry content.
2. **Causal mask** — Prevents a position from attending to future tokens.
3. **Heads** — Multiple attention subspaces process different interaction patterns.
4. **Quadratic sequence term** — The naive score matrix scales with T².

## Formal view

Attention(Q,K,V)=softmax(QKᵀ/√d_k)V. A causal mask sets forbidden logits to negative infinity before softmax.

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
