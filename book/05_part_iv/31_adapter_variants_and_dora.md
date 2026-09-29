# Chapter 31 — Adapter Variants and DoRA

**Part:** Part IV

## 1. Why adapter variants exist

LoRA constrains the update to a low-rank subspace:

W' = W + BA

Other adapter methods change the parameterization, initialization, or capacity of that update.

The engineering question is not “which variant is newest?” It is:

**Does the variant deliver a measurable quality/resource benefit on the target workload?**

## 2. Comparison matrix

| Method | Main idea | Extra complexity | What to measure |
|---|---|---|---|
| LoRA | low-rank update | low | quality vs rank |
| DoRA | separates magnitude/direction | higher | quality vs compute |
| Other adapters | alternative parameterization | varies | task + memory |

Reference for DoRA and related adapter methods should be the exact paper/docs version used in the experiment.

## 3. Rank and capacity

Increasing rank increases trainable parameters:

P_LoRA = r(d_in + d_out)

This raises:

- optimizer memory;
- checkpoint size;
- training compute.

It may improve adaptation only until the task no longer benefits from extra capacity.

## 4. Adapter targeting

Compare:

| Experiment | Attention | MLP | Rank |
|---|---|---|---:|
| A | yes | no | 16 |
| B | yes | yes | 16 |
| C | yes | yes | 32 |

Keep data, epochs, learning rate, and evaluation fixed.

## 5. Composability

Adapters can represent different specializations.

Example:

**base model + language adapter + domain adapter**

This can be operationally attractive, but composition can introduce:

- interference;
- incompatible assumptions;
- memory overhead;
- harder evaluation.

Therefore evaluate the composed system, not just each adapter independently.

## 6. Worked decision

Suppose:

| Configuration | Target score | Peak memory | Training time |
|---|---:|---:|---:|
| LoRA r16 | 84 | 18 GB | 2 h |
| LoRA r32 | 85 | 20 GB | 2.5 h |
| DoRA r16 | 85 | 21 GB | 3 h |

The differences are small.

Now include:

- run-to-run variance;
- serving path;
- adapter size;
- deployment complexity.

A seemingly better score may not justify the extra system cost.

## 7. Research exercise

Compare LoRA and one adapter variant under identical:

- model;
- data;
- training tokens;
- evaluation;
- hardware.

Report:

**quality → trainable parameters → peak memory → GPU-hours → adapter size → serving latency**

Then determine whether the observed difference is large enough to warrant a follow-up study.

## Laboratory

[lora_qlora_comparison.ipynb](../../notebooks/lora_qlora_comparison.ipynb)

## Deepening: adapter variants change the update parameterization

Different adapter methods impose different constraints on how the update is represented.

The correct comparison is not:

> “Which adapter is newest?”

It is:

**same task + same base + same data + comparable budget → which parameterization changes the measured frontier?**

### Experiment

Compare:

- LoRA;
- a second adapter parameterization;
- optionally DoRA.

Measure:

**trainable parameters + peak memory + throughput + quality + checkpoint size**

### Failure mode

An adapter variant can improve a benchmark while adding implementation or serving complexity that the workload does not need.

### Decision

Keep the simplest update parameterization that closes the measured gap under the actual resource constraint.
