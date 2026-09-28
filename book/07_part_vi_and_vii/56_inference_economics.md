# Chapter 56 — Inference Economics

**Part:** Part VI

## 1. Define the unit of economics

For an LLM product, “cost per token” is often the wrong unit.

Better units include:

- cost per successful task;
- cost per 1,000 completed conversations;
- cost per million useful output tokens;
- cost per user/month.

A useful definition is:

cost_per_successful_task =
total serving cost / successful tasks

where success includes the product's quality and latency requirements.

## 2. Serving cost anatomy

C_serving =
GPU/compute
+ storage
+ network
+ orchestration
+ observability
+ redundancy
+ idle capacity

For hosted APIs, replace GPU capacity with provider request charges plus application infrastructure.

## 3. Utilization matters

Suppose a GPU costs 4 currency units/hour.

### 25% useful utilization

Useful compute delivered = 0.25 × capacity.

Effective compute cost per unit work is much higher than at 75% utilization.

Therefore compare:

**cost/hour** and **useful throughput/hour**

not price alone.

## 4. Request-shape effects

Two systems with the same requests/sec can have very different economics.

| Workload | Prompt | Output | Main pressure |
|---|---:|---:|---|
| Short chat | 200 | 100 | scheduling/overhead |
| RAG | 3,000 | 300 | prefill/context |
| Coding | 1,000 | 2,000 | decode |
| Long conversation | 8,000 | 500 | KV/memory |

A serving benchmark should reproduce the actual production distribution.

## 5. Cost per successful task

Suppose:

- compute cost = 100 currency units/hour;
- output throughput = 2M useful tokens/hour;
- average task uses 400 output tokens.

Tasks/hour:

2,000,000 / 400 = 5,000

Cost/task:

100 / 5,000 = 0.02

Now suppose a smaller model delivers 3M useful tokens/hour but task quality falls below the product threshold.

Its nominal cost/token may be lower, but it is not a valid replacement.

## 6. Concurrency frontier

As concurrency increases:

**utilization usually rises**

until:

- memory saturates;
- queueing grows;
- latency violates the SLO;
- throughput plateaus.

This produces a practical frontier:

**maximum useful throughput subject to p95/p99 latency and quality constraints.**

## 7. Caching

Caching can reduce repeated work.

Examples:

- repeated system prompt;
- common retrieved documents;
- repeated user prefixes;
- deterministic calculations.

Measure:

- cache hit rate;
- saved prefill work;
- latency reduction;
- memory cost.

Caching is beneficial only when hit rate and reuse justify memory/complexity.

## 8. Model-size economics

Suppose:

| Model | Quality | Useful tok/s | Cost/hour |
|---|---:|---:|---:|
| Small | 82 | 3000 | 60 |
| Medium | 88 | 1800 | 75 |
| Large | 91 | 900 | 120 |

The appropriate model depends on the minimum acceptable quality and workload.

This is a constrained optimization problem, not an overall score ranking.

## 9. Break-even after distillation

Suppose a distillation project costs 20k currency units.

The student reduces serving cost by 0.015 per successful task.

Break-even:

20,000 / 0.015 ≈ 1.33 million successful tasks.

Then include:

- maintenance;
- retraining;
- evaluation;
- migration cost.

## 10. 24-month TCO

Compare:

| Cost | API | Self-hosted | Distilled/self-hosted |
|---|---:|---:|---:|
| Initial engineering | measure | measure | measure |
| Training/distillation | usually low | optional | required |
| Serving | usage-based | capacity | capacity |
| Evaluation | required | required | required |
| Operations | required | higher | higher |
| Migration | provider-dependent | internal | internal |

Project month by month rather than multiplying one month by 24 without checking traffic growth and model changes.

## 11. Sensitivity analysis

Sweep:

- requests/month;
- tokens/request;
- concurrency;
- GPU utilization;
- model quality threshold;
- cache hit rate;
- model updates.

Identify the assumptions that change the feasible design.

## Research exercise

Build a 24-month serving-cost calculator.

Compare two model sizes across three workload levels.

Report:

- quality;
- p95 latency;
- useful throughput;
- cost/task;
- GPU utilization;
- annual TCO.

Then find the workload volume at which the smaller and larger options have different economic feasibility.

## Laboratory

[inference_and_kv_cache.ipynb](../../notebooks/inference_and_kv_cache.ipynb)

## Reference

https://docs.vllm.ai/en/stable/
