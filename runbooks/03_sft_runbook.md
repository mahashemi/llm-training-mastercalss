# SFT Runbook

## Objective

Adapt an existing causal language model to a defined instruction/behavior distribution.

## Before training

Establish:
- base-model identifier and revision;
- target behavior;
- best prompt/tool baseline;
- dataset schema;
- chat template;
- train/validation split;
- evaluation suite;
- expected regressions.

## Dataset audit

For each sample check:
- valid roles;
- correct formatting;
- answer correctness;
- duplication;
- unsafe/private content;
- answer length;
- ambiguity;
- domain coverage.

## Training choices

Decide separately:
| Axis | Examples |
|---|---|
| objective | SFT / completion loss |
| update strategy | full FT / LoRA / QLoRA |
| precision | BF16 / FP16 / quantized base |
| sequence handling | truncation / packing |
| schedule | learning rate / warmup / decay |

## Smoke test

Overfit a tiny subset. Verify:
- loss decreases;
- generated behavior changes;
- evaluation pipeline works;
- checkpoint resumes.

## Real run

Log dataset version, base revision, trainable parameter count, hyperparameters, hardware, wall time, and evaluation.

## Post-training

Compare:
base vs tuned on target AND retained capabilities.

Do not report only the best examples.


## Step-by-step execution

### Gate A — Dataset

Verify chat-template compatibility and label semantics. Print representative examples after formatting, not only before formatting.

### Gate B — Baseline

Run the untuned base model on the held-out evaluation set. Save outputs.

### Gate C — Smoke test

Use a tiny subset and a few steps. Verify:

- loss moves;
- gradients are finite;
- generation changes;
- save/load works.

### Gate D — Controlled run

Freeze:

- model revision;
- tokenizer;
- dataset split;
- evaluation prompts.

Sweep only the selected variable.

### Data-quality experiment

Compare a narrow repeated dataset with a broad representative dataset at similar training-token budgets. Evaluate both target and retained capability.

### Acceptance report

Include:

**baseline → trained result → confidence/uncertainty → regressions → peak memory → throughput → checkpoint → failure analysis**

A few attractive generations are not evidence of a successful SFT run.
