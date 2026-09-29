# Chapter 25 — Pretraining Run Design

**Part:** Part III

## 1. A pretraining run is an experiment specification

Before launching, freeze:

- model architecture;
- tokenizer;
- dataset version;
- data mixture;
- sequence length;
- optimizer;
- learning-rate schedule;
- precision;
- batch size;
- training tokens;
- evaluation protocol;
- checkpoint policy.

A long run should be reproducible before it is expensive.

## 2. Compute estimate

A common first-order dense-LM heuristic:

FLOPs ≈ 6ND

where N is parameter count and D is training tokens.

Example:

7B parameters × 100B tokens

≈ 4.2e21 FLOPs

This is a planning approximation.

## 3. Translate to wall time

Use measured effective throughput:

time ≈ total FLOPs / effective FLOPs per second

Then:

compute cost ≈ accelerator-hours × blended rate

Never use accelerator count alone as a training estimate.

## 4. Pre-launch gates

| Gate | Evidence |
|---|---|
| Data | versioned manifest + quality report |
| Tokenizer | fertility/coverage test |
| Model | shape/unit tests |
| Training loop | tiny overfit test |
| Numerical stability | no NaN/Inf in stress test |
| Throughput | measured tokens/sec |
| Checkpoint | save/resume test |
| Evaluation | baseline scorecard |

A failed gate should block the long run.

## 5. Pilot scaling

Run a small controlled pilot first.

Measure:

- loss curve;
- throughput;
- GPU utilization;
- memory;
- communication;
- validation;
- checkpoint time.

The pilot should validate assumptions used by the large-run budget.

## 6. Worked scale plan

| Stage | Tokens | Main question |
|---|---:|---|
| smoke | 1M | does code work? |
| pilot | 100M | does learning work? |
| scale test | 1B | does trend persist? |
| program run | 100B | does the target justify the cost? |

The token values are illustrative.

## 7. Checkpointing

Choose cadence from:

- expected failure rate;
- recovery time;
- checkpoint size;
- acceptable recomputation.

Record RTO and RPO targets.

## 8. Evaluation during training

At intervals, evaluate:

- validation loss;
- target domain;
- target languages;
- safety;
- task benchmarks.

If a critical curve is wrong, stopping early can save large amounts of compute.

## Research exercise

Write a complete pretraining run card:

**model → tokenizer → data → tokens → FLOPs → hardware → measured throughput → wall time → checkpoint → evaluation → stop conditions**

## Laboratory

[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## Reference

https://cs336.stanford.edu/


## Deepening: design the run before launching it

A pretraining run should begin as a written experiment specification.

### Run specification

Record:

| Item | Example |
|---|---|
| model | exact config/revision |
| tokenizer | exact revision |
| training tokens | target + tolerance |
| sequence length | 2k/4k/8k |
| global batch tokens | calculated |
| optimizer | exact implementation |
| learning rate | value + schedule |
| precision | BF16/FP8/etc. |
| checkpoint interval | tokens or time |
| evaluation interval | tokens |
| data mixture | versioned |
| failure recovery | checkpoint policy |
| stopping rule | validation/compute budget |

### Batch-token accounting

Global batch tokens are approximately:

micro_batch × gradient_accumulation × sequence_length × data_parallel_world_size

This is a critical quantity because two runs can have the same micro-batch but radically different effective training throughput.

### Smoke test

Before the real run:

1. initialize model;
2. consume a tiny number of batches;
3. run forward/backward;
4. verify loss;
5. save checkpoint;
6. kill the process;
7. resume from checkpoint;
8. verify the training state continues.

A run that cannot recover is not ready for expensive compute.

### H100 bridge

The first H100 experiment should be deliberately short. Its purpose is to measure:

- tokens/sec;
- peak memory;
- communication if distributed;
- checkpoint bandwidth;
- evaluation overhead.

Only then should wall-clock projections be made.
