# Chapter 31 — Adapter Variants and DoRA

**Part:** Part IV

## Core concepts
1. **Adapters** — Add trainable modules while freezing most base weights.
2. **DoRA** — Separates magnitude and direction components of weight adaptation.
3. **Initialization** — Adapter initialization affects convergence.
4. **Composability** — Separate adapters can encode different behaviors.

## Formal view
LoRA writes ΔW as a low-rank update. DoRA and other variants alter the parameterization or initialization of that update; compare them under identical evaluation.

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
https://huggingface.co/docs/peft/
