# Chapter 38 — Quantization

**Part:** Part IV

## 1. Quantization is a resource trade

Quantization maps higher-precision values to fewer bits.

The immediate benefits can be:

- lower weight memory;
- lower memory bandwidth;
- larger models fitting on smaller hardware.

The risks include:

- accuracy degradation;
- unsupported kernels;
- calibration sensitivity;
- numerical instability.

## 2. Precision trade matrix

| Precision | Relative storage | Potential benefit | Main concern |
|---|---|---|---|
| FP32 | 1× reference | numerical robustness | memory |
| BF16/FP16 | ~0.5× FP32 | strong general tradeoff | numerical details |
| INT8 | ~0.25× FP32 | memory/bandwidth savings | calibration/error |
| 4-bit | ~0.125× FP32 | very large compression | higher quantization error |

Real memory is larger because scales, zero-points, metadata, activations, and framework overhead remain.

## 3. Weight memory example

For 7B parameters:

FP16/BF16 weights ≈ 14 GB decimal, about 13 GiB.

A 4-bit representation has an ideal raw weight footprint near 3.5 GB decimal before metadata and runtime overhead.

This is why quantization can turn an otherwise impossible deployment into a feasible one.

## 4. Compression is not speed automatically

A quantized model may use less memory but run at the same speed if the hardware/kernel path cannot exploit the representation.

Therefore benchmark:

- tokens/sec;
- time-to-first-token;
- p95 latency;
- memory;
- energy if relevant.

## 5. Quality evaluation

Compare:

**original model vs quantized model**

on:

- target tasks;
- long-context tasks;
- multilingual tasks;
- safety;
- numerical/reasoning tasks.

Report absolute degradation, not just “model still works.”

## 6. Calibration

Calibration data should approximate the deployment distribution.

Bad calibration set:

only short English prompts

Deployment:

long multilingual healthcare queries

A quantization method validated on the first distribution may degrade unexpectedly on the second.

## 7. Worked deployment example

Suppose a model requires 30 GB of weight memory in BF16.

A server has 24 GB usable memory.

A 4-bit quantized version may fit.

But the engineering question is:

**Does the quantized model meet the quality and latency SLA?**

Run a target benchmark and load test before declaring the deployment feasible.

## 8. Training vs inference quantization

| Objective | Technique to evaluate |
|---|---|
| smaller deployment | post-training quantization |
| quantization-aware training | QAT |
| low-memory adaptation | QLoRA-style training |
| maximum numerical stability | higher precision |

The techniques are related but not interchangeable.

## Research exercise

Quantize a small open model into two precisions.

Measure:

- memory;
- tokens/sec;
- p50/p95 latency;
- target-task score.

Calculate:

cost_saving = baseline_inference_cost - quantized_inference_cost

Then determine the quality loss per unit cost saved.

## Laboratory

[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## Reference

https://huggingface.co/docs/peft/developer_guides/quantization

## Deepening: quantization has multiple error surfaces

Quantization can affect:

- weights;
- activations;
- KV cache;
- optimizer state during training;
- communication payloads.

These are different interventions.

### Controlled comparison

Separate:

**weight storage precision**

from

**activation/compute precision**

and, for training,

**optimizer/base-state precision**.

Measure quality and resource usage separately.

### Failure mode

A label such as “4-bit model” can hide different storage, compute, kernel, and runtime paths.

### Decision

Always record the exact quantization method, storage format, compute dtype, kernel/runtime, and model revision.