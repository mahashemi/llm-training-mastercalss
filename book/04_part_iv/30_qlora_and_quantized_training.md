# Chapter 30 — QLoRA and Quantized Training

**Part:** Part IV

## Core concepts
1. **4-bit weights** — Store base weights in low precision.
2. **Compute dtype** — Dequantized computation can occur in BF16 or another supported dtype.
3. **NF4** — A quantization format designed for normally distributed weights.
4. **Memory savings** — Lower weight storage can make larger models trainable on limited hardware.

## Formal view
Quantization reduces weight storage; the actual training footprint still includes adapter parameters, activations, temporary tensors, and optimizer states for trainable weights.

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
https://arxiv.org/abs/2305.14314
