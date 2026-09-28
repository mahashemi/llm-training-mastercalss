# Chapter 53 — Serving with vLLM

**Part:** Part VI

## 1. Serving is a systems optimization problem

Serving quality is necessary but not sufficient.

A production benchmark should measure:

- throughput;
- TTFT;
- inter-token latency;
- p95/p99 latency;
- concurrency;
- GPU utilization;
- memory;
- cost per successful task.

vLLM is one implementation for high-throughput LLM serving; its scheduler and KV-cache management make it useful for studying the interaction between batching, memory, and latency.

Reference:
https://docs.vllm.ai/en/stable/

## 2. Continuous batching

Static batching waits for a fixed batch.

Continuous batching admits and schedules requests dynamically.

Potential benefit:

**higher utilization → more useful tokens/sec**

Potential cost:

**more scheduling complexity → tail-latency pressure**

## 3. Serving benchmark matrix

| Variable | Levels |
|---|---|
| Prompt length | 256 / 2k / 8k |
| Output length | 64 / 256 / 1k |
| Concurrency | 1 / 4 / 16 / 32 |
| Precision | BF16 / quantized |
| Workload | chat / RAG / code |
| Streaming | on / off |

A single benchmark point is not a serving profile.

## 4. Throughput vs latency

Suppose:

| Concurrency | Output tok/s | TTFT p95 | ITL p95 |
|---:|---:|---:|---:|
| 1 | 20 | 150ms | 55ms |
| 4 | 72 | 190ms | 58ms |
| 16 | 185 | 410ms | 66ms |
| 32 | 250 | 910ms | 80ms |

If the SLO is TTFT p95 ≤500 ms, the 32-request operating point is not valid even though it has higher throughput.

## 5. Cost per useful token

Define:

cost_per_useful_token =
serving infrastructure cost / output tokens delivered while meeting SLOs

The word **useful** matters.

A cheap configuration that violates latency or quality requirements is not cheap for the real product.

## 6. Capacity planning

Suppose peak load is 150 requests/sec and your measured configuration sustains 25 requests/sec while meeting the SLA.

Minimum serving replicas:

150 / 25 = 6

Then add reliability capacity according to the service objective.

If two replicas can fail while maintaining service:

planned_capacity ≥ 8 replicas

These are simplified calculations; real systems must account for queueing, traffic bursts, warm-up, and uneven request lengths.

## 7. Operational checklist

Before production:

- load test;
- failure/restart test;
- memory-pressure test;
- long-context test;
- burst traffic test;
- rolling-update test;
- observability;
- cost monitoring;
- model rollback.

## Research exercise

Benchmark a small open model across four concurrency levels.

Report:

- output tok/s;
- TTFT p50/p95;
- ITL p50/p95;
- peak memory;
- cost/hour;
- cost per million useful output tokens.

Then select an operating point based on explicit SLOs.

## Laboratory

[inference_and_kv_cache.ipynb](../../notebooks/inference_and_kv_cache.ipynb)

## Reference

https://docs.vllm.ai/en/stable/
