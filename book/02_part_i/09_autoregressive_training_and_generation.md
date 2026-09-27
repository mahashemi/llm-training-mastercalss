# Chapter 9 — Autoregressive Training and Generation

**Part:** Part I

## Core idea

This chapter turns the topic into an engineering concept: what problem it solves, what assumptions it makes, what changes in the model or system, and what evidence is needed before trusting it.

## Concepts

1. **Teacher forcing** — Training conditions each prediction on known preceding tokens.
2. **Parallel training** — All sequence positions can be evaluated together under a causal mask.
3. **Autoregressive generation** — At inference, each new token depends on the tokens already generated.
4. **Sampling** — Temperature/top-k/top-p alter the effective decoding distribution.

## Formal view

Training computes p(x_t|x_<t) at many positions simultaneously; generation repeatedly samples or selects x_t and appends it to the context.

## Practical method

1. Establish a baseline.
2. Change one major variable.
3. Measure the target metric and relevant resource metrics.
4. Inspect representative failures.
5. Repeat only when the result justifies the additional cost.

## Laboratory

[10_inference_and_kv_cache.ipynb](../../notebooks/10_inference_and_kv_cache.ipynb)

## Critical thinking

**Question:** What is the tempting but wrong shortcut here?

**Answer:** Applying the technique without identifying the bottleneck it is meant to address. A method can improve a proxy while making the actual application worse.

**Question:** What evidence should be recorded?

**Answer:** Configuration, data/model versions, hardware, evaluation protocol, metrics, runtime/resource observations, and limitations.

## Research question

What controlled experiment would distinguish the mechanism described here from a simpler explanation?

## References

https://huggingface.co/docs/transformers/main/tasks/language_modeling
