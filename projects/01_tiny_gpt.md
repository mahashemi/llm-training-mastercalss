# Project 1 — Tiny GPT From Scratch

## Mission

Build a minimal decoder-only language model from first principles so every major tensor, loss, gradient, and generation step can be inspected.

## Required implementation

- tokenizer or tiny vocabulary;
- embedding;
- positional mechanism;
- causal self-attention;
- multi-head attention;
- MLP;
- residual connections;
- normalization;
- output projection;
- cross-entropy;
- optimizer;
- generation;
- checkpoint save/load.

## Required experiments

### Experiment A — Baseline

Train the reference configuration and record:

**parameters, training tokens, validation loss, step time, tokens/sec, peak memory**

### Experiment B — Break one assumption

Choose exactly one:

- remove causal masking;
- change sequence length;
- change depth;
- change learning rate.

Predict the failure before running.

### Experiment C — Resource experiment

Change model width or sequence length and measure the resource consequence.

## Deliverables

1. source code;
2. learning curves;
3. tensor-shape audit;
4. parameter-count worksheet;
5. experiment card;
6. failure analysis;
7. generated examples;
8. checkpoint artifact;
9. reproduction instructions.

## Mastery defense

Be able to explain one training step without referring to a framework abstraction.

## Extension

Compare two architecture/tokenizer choices and write a short hypothesis-driven research note.
