# Chapter 21 — Synthetic Data

**Part:** Part III

## Core concepts
1. **Synthetic generation** — Generate additional training examples using another model or rule system.
2. **Teacher quality** — Synthetic data inherits biases and errors from its generator.
3. **Filtering** — Generated examples require validation and quality control.
4. **Diversity** — Naive generation can collapse variety and amplify artifacts.

## Formal view
Synthetic dataset quality can be modeled as generator quality × selection quality × diversity. No single scalar fully captures it.

## Engineering workflow
Establish a baseline → define one intervention → measure target metrics → measure resource metrics → inspect failures → decide whether to iterate.

## Laboratory
[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## Critical thinking
**Challenge:** What could make an apparent improvement misleading?  
**Answer:** Leakage, evaluation contamination, changed data mixture, changed decoding, implementation differences, cherry-picked examples, or an unmeasured regression.

**Challenge:** What should be measured next?  
**Answer:** The smallest experiment that most reduces uncertainty about the engineering decision.

## Research prompt
Write a falsifiable hypothesis and a minimum experiment that could disprove it.

## References
https://arxiv.org/abs/2402.00159
