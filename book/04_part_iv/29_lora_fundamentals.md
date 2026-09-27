# Chapter 29 — LoRA Fundamentals

**Part:** Part IV

## Core concepts
1. **Low-rank update** — Approximate ΔW with A B where rank r is small.
2. **Frozen base** — Base parameters remain unchanged.
3. **Target modules** — Choose which projections receive adapters.
4. **Rank** — Higher rank increases adapter capacity and resource use.

## Formal view
ΔW=BA where B∈R^{d_out×r}, A∈R^{r×d_in}; trainable parameters = r(d_in+d_out), far fewer than d_in d_out when r is small.

## Engineering workflow
Establish a baseline → define one intervention → measure target metrics → measure resource metrics → inspect failures → decide whether to iterate.

## Laboratory
[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## Critical thinking
**Challenge:** What could make an apparent improvement misleading?  
**Answer:** Leakage, evaluation contamination, changed data mixture, changed decoding, implementation differences, cherry-picked examples, or an unmeasured regression.

**Challenge:** What should be measured next?  
**Answer:** The smallest experiment that most reduces uncertainty about the engineering decision.

## Research prompt
Write a falsifiable hypothesis and a minimum experiment that could disprove it.

## References
https://arxiv.org/abs/2106.09685
