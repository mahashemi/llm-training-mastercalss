# Full Fine-Tuning Runbook

## Objective

Update all or most model parameters when the problem warrants broad adaptation.

## Use only after a baseline

Compare prompt-only and PEFT approaches first unless there is a documented reason not to.

## Preflight

Estimate:
- weight memory;
- gradient memory;
- optimizer state;
- activation memory;
- checkpoint size;
- expected GPU count;
- recovery interval.

Test the complete state checkpoint.

## Training

Keep:
- lower-risk learning rates than from-scratch pretraining;
- explicit validation;
- retained-capability evaluation;
- gradient monitoring;
- checkpointing.

## Watch for

- catastrophic forgetting;
- overfitting;
- unstable gradients;
- unexpected token/template mismatch;
- excessive checkpoint storage;
- cost growth without target quality gain.

## Acceptance

Full fine-tuning is justified only by measured evidence that its additional capacity changes the target objective enough to warrant the additional resource and regression risk.
