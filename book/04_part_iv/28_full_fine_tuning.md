# Chapter 28 — Full Fine-Tuning

**Part:** Part IV

## Core concepts
1. **All-parameter update** — Every trainable parameter can move.
2. **Optimizer state** — Training memory includes gradients and optimizer statistics.
3. **Domain shift** — Broad changes may justify broader parameter updates.
4. **Checkpoint storage** — Each full model checkpoint is large.

## Formal view
For N parameters, training-state memory includes weights + gradients + optimizer state + activations + framework overhead. The coefficient depends on precision and optimizer.

## Engineering workflow
Establish a baseline → define one intervention → measure target metrics → measure resource metrics → inspect failures → decide whether to iterate.

## Laboratory
[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Critical thinking
**Challenge:** What could make an apparent improvement misleading?  
**Answer:** Leakage, evaluation contamination, changed data mixture, changed decoding, implementation differences, cherry-picked examples, or an unmeasured regression.

**Challenge:** What should be measured next?  
**Answer:** The smallest experiment that most reduces uncertainty about the engineering decision.

## Research prompt
Write a falsifiable hypothesis and a minimum experiment that could disprove it.

## References
https://huggingface.co/docs/transformers/main/trainer
