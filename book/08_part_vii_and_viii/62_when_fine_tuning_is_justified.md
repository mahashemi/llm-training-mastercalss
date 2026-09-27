# Chapter 62 — When Fine-Tuning Is Justified

**Part:** Part VII

## Core concepts
1. **Stable behavior** — A repeated behavioral pattern is a candidate for adaptation.
2. **Prompt ceiling** — First establish the best prompt/tool baseline you can.
3. **Data efficiency** — Use a focused dataset with clear targets.
4. **Regression risk** — Evaluate retained capabilities after adaptation.

## Formal view
A fine-tuning decision should be based on Δquality / Δcost and whether the intervention addresses a stable, learnable behavior rather than constantly changing facts.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[sft_with_a_small_open_model.ipynb](../../notebooks/sft_with_a_small_open_model.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://huggingface.co/docs/trl/sft_trainer
