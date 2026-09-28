# Chapter 17 — Pretraining Corpus Design

**Part:** Part III

## 1. A corpus is a training program encoded as data

Before collecting documents, define:

- target languages;
- target domains;
- time coverage;
- quality threshold;
- licensing constraints;
- contamination exclusions;
- desired data mixture.

The question is not “How many tokens can we collect?”

It is:

**How many useful, lawful, diverse tokens can we train on for this objective?**

## 2. Corpus inventory

| Dimension | Example |
|---|---|
| source | books / web / code / government |
| language | L1 / L2 / L3 |
| domain | general / healthcare / law |
| time | historical / current |
| quality | curated / filtered / noisy |
| license | permitted / restricted / unresolved |
| synthetic | human/source / generated |

Keep these dimensions in the dataset manifest.

## 3. Usable-token accounting

Suppose raw corpus = 50B tokens.

Quality filter retains 70%:

35B

Near dedup retains 80%:

28B

Contamination removal removes 2B:

26B usable tokens.

This is the number relevant to training planning.

## 4. Data mixture

The final corpus is sampled from source families.

Track:

**raw share → usable share → sampled share**

These can differ dramatically.

Example:

| Source | Raw | Usable | Sampled |
|---|---:|---:|---:|
| Web | 80% | 65% | 55% |
| Books | 10% | 20% | 25% |
| Code | 10% | 15% | 20% |

The sampled distribution is the actual training distribution.

## 5. Temporal design

If freshness matters, include time-based evaluation.

For example:

**training through 2024 → validation 2025 → test 2026**

This can reveal whether a model genuinely generalizes to newer information.

## 6. Data quality tests

At minimum:

- duplicate rate;
- language identification accuracy;
- source balance;
- average document length;
- malformed-document rate;
- benchmark overlap;
- sensitive-data indicators;
- license coverage.

## 7. Worked experiment

Compare:

A. raw mixture  
B. filtered mixture  
C. filtered + rebalanced multilingual mixture

Hold model/training constant.

Measure:

- validation loss;
- per-language score;
- target-domain score;
- duplicate rate;
- contamination;
- compute.

## Research exercise

Build a 10-source corpus plan.

For each source estimate:

**raw tokens → usable tokens → sampled tokens → quality → rights → expected value**

Then identify the three sources that deserve the most acquisition/processing effort.

## Laboratory

[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## Reference

https://cs336.stanford.edu/
