# Chapter 65 — National-Language Strategy

**Part:** Part VIII

## Core concepts
1. **Language inventory** — Map scripts, varieties, domains, and data availability.
2. **Tokenizer allocation** — Measure token efficiency per language.
3. **Mixture design** — Avoid accidental language collapse through training imbalance.
4. **Evaluation** — Build native-language benchmarks and human review.

## Formal view
A multilingual objective is not the same as concatenating corpora. Sampling, tokenizer capacity, domain coverage, and evaluation define the effective learning allocation.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://arxiv.org/abs/2402.00159
