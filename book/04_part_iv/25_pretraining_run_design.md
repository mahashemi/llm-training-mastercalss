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
