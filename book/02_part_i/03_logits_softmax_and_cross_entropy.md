# Chapter 3 — Logits, Softmax, and Cross-Entropy

**Part:** Part I

## Core idea

This chapter turns the topic into an engineering concept: what problem it solves, what assumptions it makes, what changes in the model or system, and what evidence is needed before trusting it.

## Concepts

1. **Logits** — Unnormalized scores produced by the model.
2. **Softmax** — Maps a logit vector to a probability distribution.
3. **Cross-entropy** — Penalizes assigning low probability to the observed target.
4. **Numerical stability** — Use log-sum-exp implementations instead of naive exponentiation.

## Formal view

p_i=exp(z_i)/Σ_j exp(z_j). For target y, L=-log p_y. Minimizing average negative log-likelihood is maximum-likelihood estimation.

## Practical method

1. Establish a baseline.
2. Change one major variable.
3. Measure the target metric and relevant resource metrics.
4. Inspect representative failures.
5. Repeat only when the result justifies the additional cost.

## Laboratory

[01_next_token_prediction_and_a_tiny_language_model.ipynb](../../notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb)

## Critical thinking

**Question:** What is the tempting but wrong shortcut here?

**Answer:** Applying the technique without identifying the bottleneck it is meant to address. A method can improve a proxy while making the actual application worse.

**Question:** What evidence should be recorded?

**Answer:** Configuration, data/model versions, hardware, evaluation protocol, metrics, runtime/resource observations, and limitations.

## Research question

What controlled experiment would distinguish the mechanism described here from a simpler explanation?

## References

https://huggingface.co/docs/transformers/main/tasks/language_modeling
