# Resource Estimation

Resource planning is taught as a measured estimation problem.

## 1. Parameter memory

For N parameters stored at b bytes/parameter:

`memory_weights = N × b`

Examples:

| Model | FP16/BF16 weights, approximate |
|---:|---:|
| 135M | 0.25 GiB |
| 360M | 0.67 GiB |
| 1B | 1.86 GiB |
| 7B | 13.0 GiB |
| 70B | 130.4 GiB |

These figures exclude all training overhead.

## 2. Training-state memory

A simplified planning model:

`M ≈ weights + gradients + optimizer states + activations + temporary/framework overhead`

For Adam-style training, optimizer state can be a major fraction of the training footprint. Exact coefficients depend on precision and implementation.

## 3. First-order training compute

A common dense-LM planning heuristic is:

`C ≈ 6ND`

where:
- N = trainable parameter count;
- D = number of training tokens.

This is a planning approximation, not a universal law.

## 4. Convert compute to time

Use measured effective throughput:

`time ≈ total_FLOPs / effective_FLOPs_per_second`

Do not divide by the GPU's theoretical peak unless you clearly label the result as an optimistic upper bound.

## 5. Convert time to cost

`compute_cost ≈ accelerator_hours × hourly_rate`

Then add:
- storage;
- network;
- checkpoint overhead;
- orchestration;
- experiment/retry budget;
- personnel;
- evaluation;
- data acquisition/curation;
- security/governance.

## 6. Current price examples

Stanford CS336's Spring 2026 self-study page listed example rates as of March 28, 2026 including RunPod H100 SXM at $4.99/hour, Lambda H100 at $6.69/hour, Modal B200 at $6.25/hour, and Nebius H100 at $5.50/hour (preemptible $3.05/hour). Treat these as dated examples, not current quotes; vendor pricing and availability can change.

Source:
https://cs336.stanford.edu/

## 7. Free-first planning

For free Colab:
- use tiny models for end-to-end training;
- use analytical calculators for large-scale estimates;
- measure throughput on the hardware you actually have;
- extrapolate only after controlled experiments.

## 8. Scenario table

| Scenario | Purpose | Typical output |
|---|---|---|
| Minimum viable | prove feasibility | one experiment |
| Target | meet defined capability | pilot model |
| Expansion | improve scale/reliability | production/national program |

## 9. Funding rule

Never write “we need 1,000 GPUs” without showing:

target capability → model/data assumptions → compute estimate → measured throughput → parallel strategy → wall time → checkpoint/storage → staffing → contingency.
