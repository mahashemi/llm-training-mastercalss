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


## Memory-first feasibility gate

Before training, calculate:

**weights + gradients + optimizer + activations + temporary/runtime**

Then perform a short profiler run to calibrate the activation/runtime estimate.

### Compare against PEFT

Unless there is a documented reason not to, run a LoRA baseline using:

- same base;
- same data;
- same evaluation;
- similar training-token budget.

### Full-FT smoke test

Run a tiny job and inspect:

- loss;
- gradient norms;
- memory;
- checkpoint size;
- checkpoint restore.

### Regression guard

Keep a protected capability suite separate from the adaptation set.

Report a matrix:

| Metric | Base | LoRA | Full FT |
|---|---:|---:|---:|
| target | measure | measure | measure |
| retained | measure | measure | measure |
| safety | measure | measure | measure |
| latency | measure | measure | measure |
| training memory | measure | measure | measure |

### Stop rule

If full FT adds substantial resource cost without a meaningful target gain under the agreed gates, stop and investigate the bottleneck rather than simply increasing epochs.
