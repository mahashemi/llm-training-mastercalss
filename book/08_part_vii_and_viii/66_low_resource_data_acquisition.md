# Chapter 66 — Low-Resource Data Acquisition

## 1. The real bottleneck

For a low-resource language or domain, the first problem is often not GPUs. It is **usable data**.

A data-acquisition program should move through:

**discover → verify rights → digitize → clean → deduplicate → classify → quality-score → version → train/evaluate**

## 2. Source inventory

| Source type | Value | Main risk | Processing |
|---|---|---|---|
| Public websites | broad coverage | licensing/quality | crawl + filter |
| Government documents | authoritative | sensitive/legal | permission + metadata |
| Books | high quality | copyright | rights + OCR |
| Newspapers | current/domain-rich | licensing | archive + cleanup |
| Community writing | language coverage | noise | quality model |
| Human-authored QA | behavior/value | expensive | annotation |
| Synthetic | scale | correlated errors | provenance + filtering |

Do not rank sources by prestige. Measure their downstream value.

## 3. Acquisition economics

For a source family:

C_data =
acquisition
+ rights/verification
+ storage
+ OCR/transcription
+ cleaning
+ deduplication
+ annotation
+ quality control

A cheap corpus can become expensive after processing.

Example:

10M page images × 0.02 currency units/page for OCR = 200k currency units before validation, storage, and filtering.

The number is illustrative. The lesson is to expose processing economics.

## 4. Digitization quality

OCR errors can create systematic language noise.

Track:

- character error rate;
- word error rate;
- script confusion;
- punctuation quality;
- table preservation;
- reading order;
- confidence distribution.

Sample human QA by source and OCR confidence.

## 5. Community data

Community experts can contribute:

- terminology;
- explanations;
- examples;
- dialect coverage;
- domain-specific questions;
- safety edge cases.

Use explicit schemas for:

- contributor;
- source;
- license/permission;
- review status;
- domain;
- language/variety;
- version.

## 6. Synthetic data

Synthetic generation can expand sparse categories, but it creates correlated errors.

Recommended protocol:

**source data → teacher generation → automatic filters → semantic/quality checks → human sample review → deduplication → training**

Track synthetic fraction explicitly.

Example:

| Dataset | Human/source | Synthetic |
|---|---:|---:|
| A | 100% | 0% |
| B | 75% | 25% |
| C | 50% | 50% |

Compare model quality and failure diversity rather than assuming more synthetic data helps.

## 7. Data value is not token count

A useful data-quality card reports:

- total documents;
- total tokens;
- unique tokens/types;
- language distribution;
- domain distribution;
- source distribution;
- duplicate rate;
- quality score;
- contamination risk;
- synthetic fraction;
- temporal coverage;
- license coverage.

Then connect it to downstream performance.

## 8. Acquisition prioritization

Prioritize sources using:

value per processing cost

where value can be estimated from:

- target-domain coverage;
- linguistic diversity;
- benchmark improvement;
- factual authority;
- uniqueness.

This creates a feedback loop:

**acquire → train small model → evaluate → revise acquisition priorities**

## 9. Worked example — 5B-token target language

Suppose the goal is 5B high-quality tokens.

Inventory:

- 1.5B books;
- 1.0B government/public documents;
- 0.8B news;
- 0.5B community text;
- 2.0B noisy web.

After filtering/deduplication, assume only 60% survives.

Expected usable total:

5.8B × 0.6 = 3.48B

The gap is about 1.52B tokens.

That informs acquisition directly. Without this accounting, teams routinely overestimate usable corpus size.

## 10. Data governance

For every source preserve:

source ID, acquisition date, transformation version, license status, permitted use, processing pipeline, quality checks.

A future researcher should be able to answer:

**“Why is this document in the training corpus?”**

## Research exercise

Build a source inventory for one low-resource language with at least 10 source families.

Estimate:

- raw tokens;
- survival rate;
- usable tokens;
- processing cost;
- legal confidence;
- expected downstream value.

Then select the next three acquisition actions based on explicit assumptions.

## Laboratory

[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
