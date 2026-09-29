# Lecture 18 — LoRA, QLoRA, and PEFT

**Duration:** 25 minutes  
**Lab:** [lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)
**Primary anchors:** https://arxiv.org/abs/2106.09685 · https://arxiv.org/abs/2305.14314

## Outcome

Understand why parameter-efficient fine-tuning changes the training resource equation and how to choose rank, target modules, and quantization experimentally.

## 0–4 — The resource problem

Suppose a 7B model fits for inference but does not fit for full fine-tuning.

Ask:

**Do we need to update all 7B parameters?**

Introduce PEFT:

**freeze base → learn small update → preserve base weights**

## 4–8 — LoRA mechanics

For W:

W' = W + BA

where the adapter rank r is much smaller than the original matrix dimensions.

Parameter count:

r(d_in+d_out)

For 4096×4096:

full = 16.8M parameters

rank 16 LoRA:

16×8192 = 131k

That is roughly 128× fewer trainable parameters for that matrix.

## 8–12 — Rank is a capacity/resource knob

| Rank | Adapter capacity | Memory | Experiment |
|---:|---|---|---|
| 4 | low | low | underfit test |
| 8 | modest | low | small pilot |
| 16 | medium | low | baseline |
| 32 | higher | higher | capacity test |
| 64 | high | higher | saturation test |

Do not assume a higher rank improves quality enough to pay for itself.

## 12–16 — What should be adapted?

Compare:

| Run | Attention | MLP | Rank |
|---|---|---|---:|
| A | yes | no | 16 |
| B | yes | yes | 16 |
| C | yes | yes | 32 |

Hold data, training tokens, and evaluation constant.

## 16–19 — QLoRA

QLoRA combines adapter training with a quantized frozen base.

Potential benefit:

**lower training memory**

But measure:

- quality;
- memory;
- throughput;
- stability.

Do not assume quantization is free.

## 19–22 — Worked decision

| Method | Target score | Peak memory | GPU-hours | Adapter/checkpoint |
|---|---:|---:|---:|---|
| Full FT | 86 | 70 GB | 12 | large |
| LoRA | 84 | 20 GB | 3 | small |
| QLoRA | 83 | 14 GB | 3.5 | small |

If the hardware budget is 24 GB, full FT is infeasible in this example.

The next question is whether 84/83 quality is enough. If not, increase adapter capacity or reconsider the task.

## 22–24 — Failure analysis

**Target task underfits:** rank/data coverage may be insufficient.

**General capability regresses:** adaptation too strong or dataset too narrow.

**QLoRA slower than expected:** kernels or quantization path may dominate.

## 24–25 — Exit challenge

State:

**task → resource constraint → LoRA/QLoRA hypothesis → measured evidence → next experiment**

### References

LoRA: https://arxiv.org/abs/2106.09685  
QLoRA: https://arxiv.org/abs/2305.14314


## Lab contract

Complete the linked laboratory before treating the lecture as mastered. Record a baseline, one intervention, at least one failure, and the next experiment. See [Book ↔ Lecture ↔ Laboratory Map](../../BOOK_LAB_MAP.md).

## Deepening — make the PEFT decision quantitative

For a matrix with dimensions d_in × d_out:

**full parameters = d_in × d_out**

**LoRA parameters = r(d_in + d_out)**

Have students calculate both for several layers and sum across the architecture.

### Controlled matrix

| Run | Base | Precision | Rank | Target modules | Measure |
|---|---|---|---:|---|---|
| A | 0.6B | BF16 | 8 | attention | quality/memory |
| B | 0.6B | BF16 | 16 | attention | quality/memory |
| C | 0.6B | BF16 | 32 | attention+MLP | quality/memory |
| D | 0.6B | 4-bit | 16 | attention+MLP | quality/memory |

The objective is to produce a **quality/resource frontier**.

### H100 transfer

Repeat one arm on a 7B/8B model.

Compare what scales with model size:

- base weights;
- adapter weights;
- optimizer state;
- activations;
- throughput.

Students should explain why adapter parameter savings do not imply zero activation or runtime cost.

