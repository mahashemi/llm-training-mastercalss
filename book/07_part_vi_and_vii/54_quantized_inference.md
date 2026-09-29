# Chapter 54 — Quantized Inference

**Part:** Part VI

## 1. Quantization changes the serving envelope

The main potential benefits are:

- lower weight memory;
- lower memory bandwidth;
- ability to fit a larger model on a given GPU;
- potentially higher throughput when optimized kernels are available.

The main risks are:

- quality degradation;
- unsupported hardware/kernel path;
- calibration mismatch;
- changed latency characteristics.

## 2. Precision comparison

| Format | Ideal weight storage | Typical purpose | Main question |
|---|---:|---|---|
| FP32 | 32 bits/parameter | reference | can it fit? |
| BF16/FP16 | 16 bits/parameter | standard serving | baseline quality/speed |
| INT8 | 8 bits/parameter | memory/bandwidth reduction | quality + kernel support |
| 4-bit | 4 bits/parameter | aggressive compression | quality + throughput |

Actual memory includes scales, metadata, runtime buffers, KV cache, and framework overhead.

## 3. Fit calculation

For a 13B model:

BF16 raw weights ≈ 13B × 2 bytes ≈ 26 GB decimal

4-bit raw weights ≈ 13B × 0.5 bytes ≈ 6.5 GB decimal

This does not mean a 4-bit model needs only 6.5 GB total GPU memory.

Add:

**KV cache + activations + runtime + quantization metadata**

## 4. Compression is not speed

A quantized model can use much less memory but gain little throughput if:

- the kernel is poorly optimized;
- dequantization dominates;
- the workload is compute-bound elsewhere;
- batching is limited by another resource.

Therefore measure end to end.

## 5. Calibration

If the method uses calibration, calibration data should represent deployment.

Example mismatch:

calibration = short English prompts

deployment = long multilingual RAG requests

The quantization error profile may differ.

## 6. Evaluation matrix

| Metric | BF16 | 8-bit | 4-bit |
|---|---:|---:|---:|
| Target quality | measure | measure | measure |
| Safety | measure | measure | measure |
| TTFT p95 | measure | measure | measure |
| Output tok/s | measure | measure | measure |
| Peak memory | measure | measure | measure |
| Cost/task | measure | measure | measure |

## 7. Worked deployment example

Suppose:

- BF16 weights = 30 GB;
- available GPU memory = 24 GB.

BF16 deployment does not fit.

A 4-bit version may fit after accounting for metadata and runtime.

But the release gate should be:

**fit + quality + latency + throughput + reliability**

not simply “4-bit fits.”

## 8. When quantization is especially useful

Evaluate quantization when:

- model weights dominate memory;
- hardware is memory-constrained;
- serving cost is high;
- quality tolerance allows small degradation;
- optimized kernels exist.

## Research exercise

Quantize a small open model.

Compare BF16 vs two lower-precision configurations.

Report:

- memory;
- throughput;
- TTFT;
- target score;
- safety score;
- cost per successful task.

Calculate the quality loss per unit cost saved.

## Laboratory

[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## Reference

https://docs.vllm.ai/en/stable/

## Deepening: quantization is a quality/resource trade-off

Quantization changes numerical representation of the stored/computed weights.

Potential benefits:

- lower weight memory;
- larger model on a fixed GPU;
- potentially higher throughput.

Potential costs:

- quantization error;
- kernel constraints;
- dequantization overhead;
- changed latency.

### Experiment

Compare BF16 and a supported quantized path on the same model and workload.

Measure:

**memory + throughput + latency + target quality**

### Failure mode

A smaller weight footprint can still have poor end-to-end performance if the kernel path is inefficient.

### Decision

Quantization must be evaluated at the system level, not only by bits/parameter.
