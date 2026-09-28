# Chapter 22 — Contamination and Leakage

**Part:** Part III

## 1. What contamination does

If evaluation examples or near-duplicates appear in training data, measured performance can be inflated.

Let E_train be training examples and E_eval evaluation examples.

If overlap is substantial:

E_train ∩ E_eval ≠ ∅

then the evaluation no longer cleanly estimates generalization.

## 2. Contamination types

| Type | Example | Detection |
|---|---|---|
| Exact | same text | hash |
| Normalized | punctuation/case changes | normalized hash |
| Near duplicate | copied with edits | fingerprint/similarity |
| Semantic | paraphrase | embedding/similarity |
| Temporal | future test data in training | timestamp/source audit |
| Benchmark leakage | public test included in corpus | source exclusion |

## 3. Why random splits are insufficient

Randomly splitting documents can put nearly identical material in train and test.

Prefer:

- source-based splits;
- document-family splits;
- temporal splits;
- organization/domain holdouts.

The correct split matches the generalization claim.

## 4. Worked example

Suppose benchmark score is:

**before overlap removal: 86%**

After removing overlapping sources:

**82%**

The four-point decrease is not necessarily a model regression. It may reveal that the original measurement was contaminated.

## 5. Contamination checklist

Before a major experiment:

- scan exact overlap;
- scan near duplicates;
- inspect public benchmark sources;
- check temporal metadata;
- freeze evaluation data;
- record exclusion rules.

## 6. Leakage beyond training

Leakage can also happen through:

- prompt engineering using test examples;
- evaluator tuning on the test set;
- repeated human review of the same benchmark;
- model selection based on hidden test feedback.

Protect the test process, not only the dataset.

## 7. Research exercise

Take a small corpus and benchmark.

Create:

1. random split;
2. source-based split;
3. temporal split.

Measure the score difference.

Then run lexical and similarity overlap checks.

Explain which split supports which generalization claim.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Reference

https://cs336.stanford.edu/
