# Chapter 4 — Embeddings and Representations

**Part:** Part I

## 1. From token ID to vector

A token ID is an integer. The Transformer needs a continuous representation.

An embedding table:

E ∈ R^(V×d)

maps token IDs to vectors in R^d.

For vocabulary V and width d:

embedding_parameters = V × d

## 2. Why embeddings are learned

Early in training, vectors are not guaranteed to have semantic structure.

Gradient descent updates them so that token representations become useful for predicting context.

Similar contexts can therefore produce useful relationships in representation space.

## 3. Vocabulary-size trade-off

| Vocab | Width | Embedding parameters |
|---:|---:|---:|
| 32k | 4096 | ~131M |
| 64k | 4096 | ~262M |
| 128k | 4096 | ~524M |

A larger vocabulary can shorten sequences but consumes more parameters.

## 4. Input/output tying

Some language models reuse the input embedding matrix for the output projection.

Benefits:

- fewer parameters;
- consistent input/output representation;
- lower memory.

If tied:

output logits can use E^T h

instead of a separate matrix.

## 5. Representation geometry

Useful diagnostics include:

- nearest neighbors;
- cosine similarity;
- cluster structure;
- language/domain separation;
- token frequency effects.

But geometric similarity does not prove semantic equivalence.

## 6. Worked example

Suppose:

V=50k, d=2048

Embedding parameters:

50,000 × 2,048 = 102.4M

At BF16, raw storage is about 205 MB decimal.

A 128k vocabulary at the same width would exceed 524M parameters and about 1.05 GB raw BF16 storage.

Vocabulary therefore affects architecture economics.

## 7. Failure modes

- poorly represented rare tokens;
- excessive vocabulary size;
- tokenizer/embedding mismatch;
- accidental untied output matrix increasing parameters;
- embedding drift during domain adaptation.

## Research exercise

Compute embedding parameter/memory costs for:

V = 32k, 64k, 128k

at d = 1024, 2048, 4096.

Then connect the result to tokenizer fertility and total model size.

## Laboratory

[build_a_tiny_transformer.ipynb](../../notebooks/build_a_tiny_transformer.ipynb)

## Reference

https://arxiv.org/abs/1706.03762

## Deepening: embeddings determine the interface to the Transformer

A token ID is an integer. The embedding table maps:

**token ID → vector in R^d**

For vocabulary V and model width d:

**embedding parameters = V × d**

This can be a major fraction of parameters in smaller models.

### Worked calculation

For V=32,000 and d=4,096:

**32,000 × 4,096 ≈ 131M parameters**

At BF16, that is roughly 262 MB of raw weights.

### Experiment

Compare two hypothetical vocabulary sizes while holding d fixed.

Measure:

- embedding parameters;
- checkpoint size;
- logits size;
- tokens/sec.

Then ask why larger vocabulary affects both input embeddings and the final output projection when weights are not tied.

### Failure mode

Randomly permute the embedding table.

The model can still execute every tensor operation, but token semantics are destroyed. This demonstrates why numerical correctness of the graph is not equivalent to semantic correctness of the model.
