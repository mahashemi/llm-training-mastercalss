# Lecture 13 — Data Sources and Dataset Construction

**Lab:** [Dataset Curation Pipeline](./lab.ipynb)

## Outcome

You learn to treat a dataset as an engineered artifact with provenance, transformations, rights, composition, and measurable quality.

## Same source, different corpus

Start with a web crawl.

Ask:

> Is the raw crawl the training set?

No. Parsing, filtering, deduplication, language identification, rights review, and sampling transform it.

## Source inventory

For each source record:

- source ID;
- acquisition date;
- language/domain;
- provenance;
- rights basis;
- raw size;
- processing version.

## Transformation accounting

Example:

**20B raw → 12B after filtering → 9B after dedup → 7B after final selection**

The learner must be able to explain every reduction.

## Break it

Introduce a filter that removes one target language disproportionately.

Detect the failure with per-language accounting.

## Engineering decision

Dataset readiness means:

**provenance + rights + quality + distribution + version + evaluation implications**

not “we have many tokens.”

## Exit challenge

What is the smallest metadata set you need to reproduce the exact corpus?

## Research bridge

Use current data-processing documentation from the referenced implementation ecosystem and compare it with the simplified classroom pipeline.



## Required real-data laboratory

Do not substitute the four-row toy dataset for the real exercise. Run the [Real Dataset Corpus Bench](./lab.ipynb).

You must inspect multiple source schemas, normalize them into a common schema, measure distributions, run filtering, check cross-source exact duplicates, and construct two competing mixtures.

Minimum sources:

- FineWeb
- FineWeb-Edu
- Wikipedia
- OpenWebMath
- Aya

Then inspect one Kaggle source such as Tashkeela or RUFND.

### Evidence

Produce:

**source registry + schema map + source statistics + filter survival + dedup report + mixture A/B + downstream hypothesis**.


## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 05 — Attention Alternatives and MoE](../05_attention_alternatives_and_moe/lecture.md) · [Next: Lecture 07 — Filtering, Deduplication, Mixing and Synthetic Data →](../14_filtering_deduplication_mixing_and_synthetic_data/lecture.md)

</div>
## Video companions

[Video companions: LLM dataset construction](https://www.youtube.com/results?search_query=LLM+dataset+construction+data+curation+lecture)

## Navigation

[← Previous](../12_evaluation/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../14_filtering_deduplication_mixing_and_synthetic_data/lecture.md)
