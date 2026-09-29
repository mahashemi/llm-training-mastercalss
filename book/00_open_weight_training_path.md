# Chapter 00 — The Open-Weight Training Path

**Purpose:** establish the practical workflow used throughout this textbook.

## 1. Training systems, not API usage

An LLM engineer must understand:

**weights → tokenizer → data → objective → optimizer → hardware → evaluation → checkpoint → deployment**

The checkpoint is only one artifact.

A student who can call an API has learned model consumption.

A student who can download a checkpoint, inspect it, train an adapter, diagnose an OOM, evaluate regression, and reproduce the run has learned model engineering.

## 2. Four meanings of “train the model”

| Operation | What changes? | Typical purpose | Resource profile |
|---|---|---|---|
| Inference | nothing | use capability | weights + KV cache |
| SFT | weights/adapter | teach behavior | moderate |
| Continued pretraining | weights | change learned distribution | high |
| Pretraining from scratch | foundation parameters | create a model | extremely high |

Then add the update strategy:

| Update strategy | Meaning |
|---|---|
| Full FT | update most/all parameters |
| LoRA | update low-rank adapters |
| QLoRA | quantized frozen base + LoRA |
| Distillation | train a student from teacher signals |

Objective and update strategy are separate decisions.

## 3. Why students start with a small real model

A small model is valuable when it teaches the same mechanics as a larger model.

The course therefore uses:

- a tiny GPT for mathematical understanding;
- Qwen3-0.6B for the real open-weight workflow;
- larger Qwen models for resource scaling;
- Qwen3.8-27B as a large-model case study;
- H100 experiments for professional-scale adaptation;
- multi-GPU experiments for distributed training.

The exact model may evolve; the workflow should not.

## 4. Reproducibility chain

Never record only a model name.

Record:

**repository + revision + tokenizer + data revision + configuration + hardware + software environment**

A moving branch is not the same artifact as a fixed revision.

## 5. First resource calculation

For N parameters and b bytes/parameter:

weight_memory = N × b

| Parameters | BF16 weights | Approximate decimal GB |
|---:|---:|---:|
| 0.6B | 1.2 GB | 1.2 |
| 1.7B | 3.4 GB | 3.4 |
| 8B | 16 GB | 16 |
| 27B | 54 GB | 54 |

These are raw weight estimates, not training-memory requirements.

Ask:

> What else must fit?

## 6. Training-memory decomposition

A useful model is:

M_total = weights + gradients + optimizer + activations + temporary + runtime

For inference:

M_inference = weights + KV_cache + runtime

Therefore:

> “The model fits”

does not imply:

> “I can fine-tune it.”

## 7. Universal training loop

Every training experiment is:

1. load batch;
2. tokenize/prepare;
3. forward;
4. compute loss;
5. backward;
6. accumulate gradients if needed;
7. optimizer update;
8. scheduler update;
9. log;
10. checkpoint;
11. evaluate.

Frameworks automate these operations; they do not remove the engineering responsibility to understand them.

## 8. Experiment ladder

### Level 1 — Environment

- GPU visible;
- imports succeed;
- model loads;
- forward pass works.

### Level 2 — Training loop

- tiny dataset;
- few steps;
- loss changes;
- checkpoint saves.

### Level 3 — Learning

- controlled dataset;
- baseline;
- evaluation;
- regression checks.

### Level 4 — Reproduction

- fixed revision;
- configuration;
- dataset version;
- seed where meaningful;
- artifact metadata.

### Level 5 — Scaling

- throughput;
- memory;
- quality;
- marginal gain;
- cost.

Only then increase model, data, context, or GPU count.

## 9. Free-Colab rule

Free Colab resources are dynamic and not guaranteed. Labs therefore cannot assume a specific accelerator, session duration, unlimited local storage, or persistent runtime.

A notebook should detect hardware and adapt or fail with a useful explanation.

## 10. H100-ready notebooks

A notebook is H100-ready when:

- model ID is configurable;
- batch size is configurable;
- sequence length is configurable;
- precision is configurable;
- device is detected;
- memory is measured;
- checkpoints are resumable;
- evaluation is independent;
- metadata is saved.

H100-ready does not mean the same configuration should be run unchanged at every scale.

## 11. Central engineering question

At every stage ask:

> **What is the smallest experiment that can distinguish my hypotheses?**

Examples:

**Hypothesis:** the model lacks domain knowledge.

Test RAG, controlled domain evaluation, and a continued-pretraining pilot.

**Hypothesis:** the model knows the answer but follows the wrong format.

Test structured prompting and SFT/LoRA.

**Hypothesis:** training is too expensive.

Test QLoRA, sequence-length reduction, activation checkpointing, and rank.

This prevents unnecessary scaling.

## 12. Exit standard

A student has mastered the practical core when they can take an unfamiliar open-weight model and produce:

**model card → resource estimate → baseline → smoke test → training run → evaluation → checkpoint → failure analysis → next experiment**

Later chapters add distributed systems, scaling laws, inference, economics, research, and program design.
