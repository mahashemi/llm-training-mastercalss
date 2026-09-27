# Chapter 2 — Tokenization as a Modeling Decision

**Part:** Part I

## Core idea

This chapter turns the topic into an engineering concept: what problem it solves, what assumptions it makes, what changes in the model or system, and what evidence is needed before trusting it.

## Concepts

1. **Discrete interface** — Text must be converted to IDs before the neural network can process it.
2. **BPE** — Merge frequent byte/character sequences to create reusable subword units.
3. **Vocabulary tradeoff** — Larger vocabularies can shorten sequences but increase embedding/output parameters.
4. **Fertility** — Tokens per word or semantic unit gives a practical multilingual efficiency measure.

## Formal view

Let V be vocabulary size and D the embedding dimension. The embedding table contains V×D parameters, so vocabulary design changes both model size and sequence length.

## Practical method

1. Establish a baseline.
2. Change one major variable.
3. Measure the target metric and relevant resource metrics.
4. Inspect representative failures.
5. Repeat only when the result justifies the additional cost.

## Laboratory

[tokenizer_design_and_measurement.ipynb](../../notebooks/tokenizer_design_and_measurement.ipynb)

## Critical thinking

**Question:** What is the tempting but wrong shortcut here?

**Answer:** Applying the technique without identifying the bottleneck it is meant to address. A method can improve a proxy while making the actual application worse.

**Question:** What evidence should be recorded?

**Answer:** Configuration, data/model versions, hardware, evaluation protocol, metrics, runtime/resource observations, and limitations.

## Research question

What controlled experiment would distinguish the mechanism described here from a simpler explanation?

## References

https://cs336.stanford.edu/
