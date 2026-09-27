# Chapter 54 — Quantized Inference

**Part:** Part VI

## Core concepts
1. **Weight compression** — Reduce memory footprint of stored weights.
2. **Kernel support** — Quantization helps only if the hardware/software path can exploit it.
3. **Calibration** — Representative inputs can influence quantization error.
4. **Quality testing** — Evaluate target tasks after quantization.

## Formal view
Quantization trades representation precision for storage/bandwidth savings. Measure end-to-end tokens/sec and task quality, not compression ratio alone.

## Practice
Define the operational objective, freeze the baseline, run the smallest informative experiment, record resource use, inspect failures, and decide whether the next intervention is justified.

## Laboratory
[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## Critical thinking
**Question:** What can a benchmark or metric hide?  
**Answer:** Distribution shift, severe but rare failures, cost/latency regressions, and behavior outside the tested task.

**Question:** What makes this research-grade?  
**Answer:** Clear hypothesis, controlled comparison, versioned inputs, reproducible procedure, quantitative evidence, uncertainty/limitations, and enough detail for another team to repeat it.

## Research prompt
Propose one ablation and one failure-analysis experiment.

## References
https://docs.vllm.ai/en/stable/
