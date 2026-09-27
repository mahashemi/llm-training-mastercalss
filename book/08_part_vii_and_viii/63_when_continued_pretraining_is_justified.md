# Chapter 63 — When Continued Pretraining Is Justified

**Part:** Part VII

## Core concepts
1. **Domain language** — Vocabulary, style, and domain distributions may differ substantially.
2. **Corpus size** — Enough high-quality domain tokens are needed to change the model meaningfully.
3. **General capability** — Mix general data or evaluate retention if broad ability matters.
4. **Compute** — Continued pretraining is more expensive than a small SFT run.

## Formal view
Continued pretraining changes the base language-model distribution. It is attractive when the domain shift is fundamental enough that examples alone do not provide sufficient signal.

## Practice
Start with a baseline, define measurable outcomes, change one major variable, and document quality, compute, latency, risk, and reproducibility.

## Laboratory
[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Critical thinking
**Question:** What assumption matters most?  
**Answer:** Identify the assumption whose failure would change the decision. Test that one first.

**Question:** What makes the output reusable?  
**Answer:** Explicit definitions, sources, versioned experiments, and limitations.

## Research prompt
Design the cheapest experiment that could invalidate the recommendation.

## References
https://arxiv.org/abs/2402.00159
