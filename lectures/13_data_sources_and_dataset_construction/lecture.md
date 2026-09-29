# Lecture 13 — Data Sources and Dataset Construction

**Duration:** 25 minutes  
**Lab:** [Dataset Curation Pipeline](../../notebooks/dataset_curation_pipeline.ipynb)

## Outcome

Students learn to treat a dataset as an engineered artifact with provenance, transformations, rights, composition, and measurable quality.

## 0–4 — Same source, different corpus

Start with a web crawl.

Ask:

> Is the raw crawl the training set?

No. Parsing, filtering, deduplication, language identification, rights review, and sampling transform it.

## 4–9 — Source inventory

For each source record:

- source ID;
- acquisition date;
- language/domain;
- provenance;
- rights basis;
- raw size;
- processing version.

## 9–14 — Transformation accounting

Example:

**20B raw → 12B after filtering → 9B after dedup → 7B after final selection**

The learner must be able to explain every reduction.

## 14–19 — Laboratory

Build a mini dataset pipeline and calculate survival rates after each stage.

Produce:

| Stage | Docs | Tokens | Survival |
|---|---:|---:|---:|
| raw | measure | measure | 100% |
| parsed | measure | measure | measure |
| filtered | measure | measure | measure |
| deduped | measure | measure | measure |
| final | measure | measure | measure |

## 19–22 — Break it

Introduce a filter that removes one target language disproportionately.

Detect the failure with per-language accounting.

## 22–24 — Engineering decision

Dataset readiness means:

**provenance + rights + quality + distribution + version + evaluation implications**

not “we have many tokens.”

## 24–25 — Exit challenge

What is the smallest metadata set you need to reproduce the exact corpus?

## Research bridge

Use current data-processing documentation from the referenced implementation ecosystem and compare it with the simplified classroom pipeline.
