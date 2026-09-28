# Resource Estimation

Resource planning is taught as a measured estimation problem.

## 1. Parameter memory

For N parameters stored at b bytes/parameter:

memory_weights = N × b

Approximate BF16/FP16 weight memory:

| Model | Weight memory |
|---:|---:|
| 135M | 0.25 GiB |
| 360M | 0.67 GiB |
| 1B | 1.86 GiB |
| 7B | 13.0 GiB |
| 70B | 130.4 GiB |

These values exclude gradients, optimizer state, activations, framework overhead, and KV cache.

## 2. Training-state memory

A planning decomposition is:

M_total =
weights
+ gradients
+ optimizer states
+ activations
+ temporary buffers
+ framework/communication overhead

For Adam-style optimization, optimizer state can be a major memory component. Exact coefficients depend on precision and implementation.

Use an actual memory profiler for final sizing.

## 3. Activation memory

Activation memory depends on:

- sequence length;
- batch size;
- hidden size;
- number of layers;
- checkpointing;
- attention implementation.

This is why “7B model = 13 GiB” is not equivalent to “7B model fits in a 16 GiB training GPU.”

## 4. First-order pretraining compute

A common dense-LM planning heuristic is:

FLOPs ≈ 6ND

where:

N = trainable parameter count  
D = training tokens

This is an approximation. Architecture, optimizer, sequence length, recomputation, and implementation affect actual work.

## 5. Convert compute to time

Use measured delivered throughput:

time = total_FLOPs / effective_FLOPs_per_second

Do not divide by theoretical peak unless explicitly labeling the result as an optimistic upper bound.

## 6. Convert time to cost

compute_cost =
accelerator_hours × blended_accelerator_rate

Then add:

- storage;
- networking;
- checkpoint overhead;
- orchestration;
- experiment/retry budget;
- evaluation;
- personnel;
- data acquisition/curation;
- security/governance.

## 7. Worked example

Suppose:

- N = 7B;
- D = 100B tokens.

FLOPs ≈ 6 × 7e9 × 100e9 = 4.2e21

If the actual system delivers 5e15 effective FLOP/s:

time ≈ 8.4e5 seconds ≈ 9.7 days

If the full-cluster blended rate is 160 currency units/hour:

compute ≈ 9.7 × 24 × 160 ≈ 37.2k currency units

The cost is illustrative. It is not a vendor quote.

## 8. Scenario planning

Never produce one estimate.

| Scenario | Model | Tokens | Main purpose |
|---|---:|---:|---|
| Feasibility | 1B | 100B | test pipeline |
| Pilot | 7B | 100B | test capability |
| Larger study | 7B | 1T | test data/scale |
| Program | project-specific | project-specific | production/foundation |

Then compute wall time and cost using measured throughput.

## 9. GPU count is derived, not guessed

Given:

required wall time T  
total compute F  
effective throughput per GPU f  
scaling efficiency e

Approximate GPU count:

GPUs ≈ F / (T × f × e)

The efficiency term matters.

At 90% scaling efficiency:

64 GPUs behave like 57.6 ideal GPUs.

At 50%:

64 GPUs behave like 32.

Measure e on your workload.

## 10. Storage

Estimate:

raw data
+ processed shards
+ checkpoints
+ optimizer states
+ logs
+ evaluation
+ replicas

For checkpoint size S and K retained checkpoints:

storage_checkpoints ≈ S × K

Add failed/experimental versions according to the retention policy.

## 11. Free-first planning

For free Colab/CPU environments:

- use tiny models end-to-end;
- measure throughput;
- validate training loops;
- estimate larger runs analytically;
- do not claim large-scale performance from tiny hardware.

This creates a realistic bridge from free education to professional planning.

## 12. Current price examples

Vendor pricing changes frequently. When using price examples, record:

**provider → accelerator → pricing mode → region → date captured → source URL**

The repository's earlier examples from Stanford CS336 are historical planning references and should not be presented as current quotes.

## 13. Funding rule

Never write:

“We need 1,000 GPUs.”

Write:

**target capability → model/data assumptions → FLOPs → measured throughput → scaling efficiency → wall time → accelerator cost → storage → staffing → contingency**

## Research exercise

For a hypothetical 7B model, create low/medium/high resource scenarios.

For each calculate:

- training FLOPs;
- GPU count;
- wall time;
- accelerator hours;
- compute cost;
- checkpoint storage;
- staffing;
- contingency.

Then vary one assumption at a time.
