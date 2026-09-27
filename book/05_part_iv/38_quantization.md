# Chapter 38 — Quantization

**Part:** Part IV

## Core concepts
1. **Post-training quantization** — Compress an existing model for inference.
2. **Quantization-aware training** — Train with quantization effects in the loop.
3. **Calibration** — Representative data can affect quantization quality.
4. **Accuracy-resource tradeoff** — Lower precision is not automatically free.

## Formal view
Quantization approximates a high-precision weight w by a lower-bit representation q(w). The error distribution should be measured on target tasks.

## Engineering workflow
Baseline → intervention → evaluation → profiling → failure analysis → decision.

## Laboratory
[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## Critical thinking
**Question:** What could make the method appear to work while the real objective gets worse?

**Answer:** Proxy optimization, data leakage, benchmark contamination, distribution shift, or resource-side regressions can all produce misleading gains.

**Question:** What should the next experiment be?

**Answer:** The cheapest experiment that tests the highest-impact uncertainty.

## Research prompt
State a falsifiable claim and design a minimum-cost test that could reject it.

## References
https://huggingface.co/docs/peft/developer_guides/quantization
