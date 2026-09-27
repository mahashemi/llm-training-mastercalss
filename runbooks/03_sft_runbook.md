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
