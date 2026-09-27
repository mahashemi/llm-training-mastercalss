# Chapter 66 — Low-Resource Data Acquisition

**Part:** Part VIII

## Core concepts
1. **Digitization** — Books and documents may require OCR and quality control.
2. **Community data** — Experts can contribute valuable domain/language examples.
3. **Licensing** — Permission must be documented.
4. **Synthetic augmentation** — Use cautiously and track generated versus human-origin data.

## Formal view
Let D_h and D_s be human/source and synthetic tokens. Track both explicitly because their error and diversity distributions differ.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://arxiv.org/abs/2402.00159
