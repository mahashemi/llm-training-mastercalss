# Open-Weight Case Study — Qwen3.8-27B and the H100

**Last checked:** 2026-09-29

This document anchors the curriculum to a current open-weight family while keeping the teaching method model-agnostic.

## 1. Current model references

The official Qwen Hugging Face organization currently lists:

- Qwen/Qwen3-0.6B — classroom-scale checkpoint;
- Qwen/Qwen3.8-27B — approximately 28B in the Hugging Face model listing;
- Qwen/Qwen3.8-27B-FP8 — corresponding FP8 checkpoint;
- Qwen/Qwen3.8-2.4T-A95B and FP8 variants for a much larger MoE case study.

Official organization:
https://huggingface.co/Qwen

## 2. Why start with 0.6B

Current Hugging Face TRL documentation uses Qwen3-0.6B as a quick SFT example, making it a natural educational checkpoint for this course.

TRL SFT guide:
https://huggingface.co/docs/trl/sft_trainer

Students learn:

**load → inspect → baseline → SFT → evaluate → save/reload**

before moving to larger models.

## 3. Why use 27B as the H100 case

A dense 27B model in BF16 requires approximately:

**27 × 10^9 parameters × 2 bytes ≈ 54 GB**

of raw weight storage.

The NVIDIA H100 SXM has 80 GB of GPU memory:
https://www.nvidia.com/en-eu/data-center/h100/

This makes 27B BF16 weight loading/inference plausible on a single 80 GB H100, but usable memory also depends on runtime allocation, context length, KV cache, and other buffers.

It does not imply one-H100 full fine-tuning.

## 4. Five distinct experiments

| Experiment | Main resource problem |
|---|---|
| 27B BF16 inference | weights + KV cache + runtime |
| 27B quantized inference | lower weight memory / serving trade-offs |
| 27B QLoRA | adapter training with quantized frozen base |
| 27B BF16 LoRA | adapter training without base quantization |
| 27B full FT | full training state + activations + distributed memory |

For the QLoRA path, official PEFT documentation describes 4-bit loading, NF4, nested quantization, BF16 compute, and the all-linear target configuration:
https://huggingface.co/docs/peft/developer_guides/quantization

## 5. H100 lab sequence

### Lab 1 — Model audit

Record checkpoint/revision, parameter count, architecture, context, tokenizer, precision, and license.

### Lab 2 — Resource prediction

Before loading, calculate expected weight memory and expected runtime/KV overhead. After loading, measure allocated and reserved memory and explain the gap.

### Lab 3 — Inference envelope

Vary context, concurrency, and generation length. Measure TTFT, inter-token latency, output tokens/sec, and peak memory.

### Lab 4 — QLoRA

Run a tiny controlled adaptation and measure trainable parameters, peak memory, tokens/sec, quality, and adapter size.

### Lab 5 — BF16 LoRA

Repeat the same experiment. Ask what quantization saved and what it cost.

### Lab 6 — Full FT feasibility

Do not launch a large job. Build the memory budget first:

**weights + gradients + optimizer + activations + runtime**

Then decide whether sharding or additional GPUs are required.

## 6. Scale to multi-GPU

Once a single-GPU experiment is understood:

**1 GPU → 2 → 4 → 8**

Measure scaling efficiency:

**throughput(k) / [k × throughput(1)]**

Then add communication time, checkpoint time, data-loader wait, and restart/recovery behavior.

## 7. Why this belongs in the course

The objective is not to memorize one Qwen release.

The student should be able to take a future open-weight checkpoint and repeat:

**model audit → resource model → baseline → training hypothesis → controlled experiment → evaluation → failure analysis → scale decision**

That remains valid as model families, frameworks, quantization methods, and hardware change.
