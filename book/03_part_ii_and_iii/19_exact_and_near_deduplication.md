# Chapter 19 — Exact and Near Deduplication

**Part:** Part III

## 1. Why duplicate data matters

If the same document appears repeatedly, the training distribution overweights it.

That can:

- waste compute;
- increase memorization;
- distort source mixture;
- increase contamination risk;
- reduce effective diversity.

Deduplication is therefore both a **data-quality operation** and a **compute-allocation decision**.

## 2. Two forms of deduplication

| Method | Detects | Cost | Typical use |
|---|---|---|---|
| Exact hash | identical bytes/text | low | obvious duplicates |
| Normalized hash | equivalent after normalization | low | formatting variants |
| Near-duplicate fingerprints | similar text | medium | syndicated/reposted content |
| Semantic similarity | meaning-level similarity | high | paraphrased copies |

Use the least expensive method that detects the relevant duplication mechanism.

## 3. Example

Suppose raw corpus:

10B tokens

After exact dedup:

8.5B

After near dedup:

7.2B

You have removed 2.8B tokens.

But the relevant question is not “did we delete tokens?”

It is:

**Did the remaining 7.2B tokens preserve or improve useful diversity and downstream quality?**

## 4. Deduplication trade-offs

Aggressive near-dedup can remove:

- useful repeated canonical formulations;
- legitimate parallel-language examples;
- legal or policy versions where repetition is meaningful;
- high-quality training examples.

Therefore compare multiple thresholds.

| Threshold | Usable tokens | Validation loss | Target score |
|---|---:|---:|---:|
| loose | 8.0B | 2.70 | 78 |
| medium | 7.2B | 2.68 | 80 |
| aggressive | 5.8B | 2.75 | 77 |

The middle setting may be worth investigating further, but the conclusion requires actual experiments.

## 5. Contamination connection

Maintain exclusion sets for:

- evaluation benchmarks;
- protected tests;
- known copyrighted/restricted sources where applicable;
- sensitive datasets.

Run overlap checks before training.

## 6. Research exercise

Create three deduplication policies.

Measure:

- duplicate removal;
- corpus diversity;
- language balance;
- validation loss;
- downstream score;
- processing cost.

Then estimate quality improvement per billion tokens processed.

## Laboratory

[dedup_and_data_mixing.ipynb](../../notebooks/dedup_and_data_mixing.ipynb)

## Reference

https://cs336.stanford.edu/

## Deepening: deduplication changes information density

Exact deduplication removes byte-identical or normalized duplicates.

Near-dedup attempts to identify highly similar documents.

### Why it matters

Duplicates can:

- waste token budget;
- bias sampling;
- increase memorization pressure;
- contaminate evaluation;
- reduce effective diversity.

But aggressive dedup can remove legitimate repeated text.

### Controlled experiment

Create three corpora:

| Corpus | Transformation |
|---|---|
| A | no dedup |
| B | exact dedup |
| C | exact + near dedup |

Keep model, training tokens, and evaluation fixed.

Measure:

**validation loss + memorization/contamination indicators + target slices**

### Failure mode

A near-dedup threshold that is too aggressive merges semantically distinct documents.

The threshold must be measured, not assumed.
