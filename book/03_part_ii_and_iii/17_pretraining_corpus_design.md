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

## Deepening: corpus composition is a model hyperparameter

A pretraining corpus should be specified by:

**source family × language × domain × time × quality × rights**

### Example composition

Suppose a corpus contains:

- 70% general web;
- 20% books/curated text;
- 10% target domain.

That composition is not merely descriptive. It determines the probability that a training token comes from each distribution.

### Experiment

Construct two equal-token mixtures with different source proportions.

Hold model, optimizer, and total tokens constant.

Measure:

- validation loss;
- domain slices;
- language slices;
- memorization/contamination indicators.

### Failure mode

A large source can dominate the mixture even when it is not the highest-value source.

### Decision

Report both raw corpus size and the **effective training mixture actually sampled**.



## Real Dataset Track

Do not complete this chapter using only fabricated examples. Use the [Real Dataset Bench](../../notebooks/real_dataset_corpus_bench.ipynb) and the [Real Dataset Registry](../../data/REAL_DATASET_REGISTRY.md).

The first experiment should inspect at least **FineWeb, FineWeb-Edu, Wikipedia, OpenWebMath, and Aya**. Then compare at least one Kaggle source such as **Tashkeela** or **RUFND**.

For each source, record:

**dataset ID → config/subset → split → sample size → schema → language → source/domain → license/access basis → preprocessing → filtering → dedup → final mixture share**

The goal is to make the corpus itself an auditable experimental object.