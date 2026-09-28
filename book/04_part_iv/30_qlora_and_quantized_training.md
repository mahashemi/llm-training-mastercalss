# Chapter 30 — QLoRA and Quantized Training

**Part:** Part IV

## 1. The resource problem

Full fine-tuning can require large amounts of:

- model memory;
- gradients;
- optimizer state;
- activations.

QLoRA combines a quantized frozen base model with trainable low-rank adapters.

The central objective is:

**reduce training memory enough to make adaptation feasible on constrained hardware.**

Reference:
https://arxiv.org/abs/2305.14314

## 2. LoRA vs QLoRA

| Property | LoRA | QLoRA |
|---|---|---|
| Base weights | frozen | frozen + quantized |
| Adapter | trainable | trainable |
| Training memory | low | lower in many configurations |
| Quantization error | none from base quantization | present |
| Main risk | under-capacity | quality/kernel/quantization effects |
| Best use | enough memory | memory-constrained training |

The exact memory saving depends on model, quantization format, optimizer, sequence length, and runtime.

## 3. Memory accounting

Approximate raw base-weight storage:

BF16: 2 bytes/parameter

4-bit: 0.5 bytes/parameter before metadata.

For 7B parameters:

BF16 raw weights ≈ 14 GB decimal

4-bit raw weights ≈ 3.5 GB decimal

But training still requires:

**adapter weights + gradients + optimizer state + activations + runtime/metadata**

So raw weight memory is only one line item.

## 4. Rank is still a capacity knob

For a matrix:

P_adapter = r(d_in+d_out)

Higher rank:

- adds parameters;
- increases memory;
- can increase quality.

Run a rank sweep rather than assuming r=16 or 32 is optimal.

## 5. Quantization-aware evaluation

Compare:

| Run | Base precision | Rank | Target quality | Peak memory |
|---|---|---:|---:|---:|
| A | BF16 | 16 | measure | measure |
| B | 4-bit | 16 | measure | measure |
| C | 4-bit | 32 | measure | measure |

This separates:

**precision effect** from **adapter-capacity effect**.

## 6. Worked deployment constraint

Suppose available training memory = 16 GB.

Full FT requires 70 GB in a hypothetical setup.

LoRA requires 20 GB.

QLoRA requires 14 GB.

Then only QLoRA fits the stated constraint without changing hardware.

The next question is whether its quality is acceptable.

## 7. Failure modes

### OOM
Check sequence length, batch, activations, optimizer, and quantization configuration.

### Quality drop
Compare against LoRA on the same data.

### Slow training
Profile dequantization and kernels.

### Instability
Check precision paths and optimizer settings.

## 8. Research exercise

Run a small 3-arm experiment:

**LoRA/BF16 → QLoRA rank 16 → QLoRA rank 32**

Measure:

- peak memory;
- GPU-hours;
- target score;
- retained capability;
- tokens/sec.

Plot quality against training memory.

## Laboratory

[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## References

- QLoRA: https://arxiv.org/abs/2305.14314
- LoRA: https://arxiv.org/abs/2106.09685
