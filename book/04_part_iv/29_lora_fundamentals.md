# Chapter 29 — LoRA Fundamentals

**Part:** Part IV

## 1. What LoRA changes

Instead of updating a full weight matrix W directly, LoRA keeps W frozen and learns a low-rank update:

W' = W + BA

where:

- B has shape d_out × r;
- A has shape r × d_in;
- r is much smaller than the original dimensions.

Trainable parameters:

r(d_in + d_out)

instead of:

d_in × d_out

Reference: https://arxiv.org/abs/2106.09685

## 2. Parameter savings

For a 4096 × 4096 matrix:

Full matrix parameters = 16.8M.

At rank r = 16:

LoRA parameters = 16 × (4096 + 4096) = 131k.

That is roughly 128× fewer trainable parameters for that matrix.

This is why PEFT can dramatically reduce optimizer and gradient memory.

## 3. What rank controls

| Rank | Adapter capacity | Train memory | Risk |
|---:|---|---|---|
| 4 | low | very low | underfitting |
| 8 | modest | low | possible capacity limit |
| 16 | medium | low | common pilot |
| 32 | higher | higher | diminishing returns possible |
| 64+ | high | higher | may add cost without useful gain |

These are experiment points, not universal optimal values.

## 4. Which modules?

Common candidate targets include:

- attention query/key/value/output projections;
- MLP projections.

Do not assume “more target modules = better.”

Run a controlled comparison.

| Run | Target modules | Rank | Quality | Train memory |
|---|---|---:|---:|---:|
| A | attention | 16 | measure | measure |
| B | attention + MLP | 16 | measure | measure |
| C | attention + MLP | 32 | measure | measure |

## 5. LoRA vs full fine-tuning

| Dimension | LoRA | Full FT |
|---|---|---|
| Trainable parameters | small fraction | most/all |
| Optimizer memory | lower | much higher |
| Checkpoint size | small adapters | large |
| Multiple specializations | convenient | heavier |
| Base model fixed | yes | no |
| Best use | efficient adaptation | broad adaptation hypothesis |

Neither is automatically better; the task and resource constraints determine the useful comparison.

## 6. Worked example — 7B adaptation

Suppose the full model requires large training memory and available hardware is limited.

Run:

**QLoRA/LoRA pilot → evaluate target task → compare with larger-rank adapter**

Only if the adapter saturates and the capability gap remains should full fine-tuning become the next experiment.

## 7. Merging and deployment

Adapters can be:

- loaded separately;
- combined with a base model for deployment;
- maintained as separate specialization artifacts.

The serving choice affects:

- latency;
- memory;
- operational complexity;
- ability to host many adapters.

Therefore record the deployment mode in experiments.

## 8. Failure modes

### Rank too small
Target behavior underfits.

### Dataset too narrow
Model over-specializes.

### Wrong target modules
Training signal cannot alter the required behavior effectively.

### Evaluation contamination
Apparent gains are not trustworthy.

### Catastrophic regression
Target improves while general capabilities decline.

## Research exercise

Run:

rank 8 → 16 → 32

with fixed data and training budget.

Report:

- trainable parameters;
- peak memory;
- GPU-hours;
- target score;
- retained capability;
- serving latency.

Plot quality vs adapter cost.

## Laboratory

[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## Reference

https://arxiv.org/abs/2106.09685


## Deepening: LoRA is a constrained hypothesis about the update

LoRA assumes that the useful weight update can be represented approximately in a low-rank subspace.

That is a modeling hypothesis, not merely a memory trick.

### Rank experiment

Run ranks:

4, 8, 16, 32, 64

while holding constant:

- base checkpoint;
- dataset;
- train steps;
- sequence length;
- learning rate;
- evaluation.

Report:

| Rank | Trainable params | Peak memory | Tokens/sec | Target score | Regression |
|---:|---:|---:|---:|---:|---:|
| 4 | measure | measure | measure | measure | measure |
| 8 | measure | measure | measure | measure | measure |
| 16 | measure | measure | measure | measure | measure |
| 32 | measure | measure | measure | measure | measure |
| 64 | measure | measure | measure | measure | measure |

The desired output is a **quality/resource frontier**, not a favorite rank.

### Target-module experiment

Compare attention-only against attention + MLP targets. This tests whether the required behavior is representable through the selected modules.

### H100 bridge

Repeat the same rank sweep on a larger model. Students should discover that the mathematical rule stays the same while the resource consequences change.
