# Chapter 5 — Positional Information and RoPE

**Part:** Part I

## Core idea

This chapter turns the topic into an engineering concept: what problem it solves, what assumptions it makes, what changes in the model or system, and what evidence is needed before trusting it.

## Concepts

1. **Position** — Self-attention alone is permutation-equivariant without position information.
2. **Absolute position** — Adds an explicit positional representation.
3. **Rotary position embeddings** — Rotate query/key coordinates as a function of position, affecting attention scores.
4. **Context extension** — Changing context length requires careful validation; position encoding behavior matters.

## Formal view

Attention uses q·k. RoPE applies position-dependent rotations R_t to q and k, so relative positional structure enters their dot product.

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

https://arxiv.org/abs/2104.09864
