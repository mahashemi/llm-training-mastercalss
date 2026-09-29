# Open-Weight Model Runbook

## Objective

Take an unfamiliar open-weight model from repository artifact to a reproducible training decision.

## Gate 1 — Identify the artifact

Record model ID, exact revision, license, base/instruct status, architecture, parameter count, active parameters for MoE, tokenizer/revision, context, and available precision/checkpoint variants.

## Gate 2 — Estimate resources

Before loading: weights + expected runtime/KV + training-state estimate if adaptation is planned.

Do not infer training feasibility from checkpoint file size alone.

## Gate 3 — Load and audit

Measure load time, parameter count, allocated/reserved memory, tokenizer behavior, baseline generation, prompt/output token counts, and throughput.

## Gate 4 — Establish baseline

Freeze prompts, chat template, decoding, model revision, and evaluation set. Save baseline outputs before training.

## Gate 5 — Smoke-test adaptation

Run a tiny dataset for a few steps. Verify finite loss/gradients, checkpoint save/load, and changed generation.

## Gate 6 — Choose training method

Separate the learning objective (SFT, continued pretraining, preference, RL) from the update strategy (full FT, LoRA, QLoRA, other PEFT).

Select the smallest method supported by the measured failure.

## Gate 7 — Evaluate

Compare target capability, retained capability, safety/robustness, latency, memory, throughput, and checkpoint/adapter size.

## Gate 8 — Scale

Move from 0.6B → larger single-GPU model → H100 → multi-GPU only when the prior experiment demonstrates why additional scale is useful.

## Required artifact

model audit + baseline + resource sheet + experiment card + evaluation + failure analysis + next-scale decision

## Related resources

- notebooks/open_weight_model_audit.ipynb
- notebooks/sft_with_a_small_open_model.ipynb
- docs/OPEN_WEIGHT_TRAINING_LADDER.md
- docs/OPEN_WEIGHT_QWEN_H100_CASE_STUDY.md
- templates/EXPERIMENT_CARD.md