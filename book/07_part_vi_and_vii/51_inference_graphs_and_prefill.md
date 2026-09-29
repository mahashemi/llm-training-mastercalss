# Chapter 51 — Inference Graphs and Prefill

**Part:** Part VI

## 1. Generation has two very different phases

### Prefill

The model processes the existing prompt and builds hidden states/KV cache.

### Decode

The model generates new tokens autoregressively, typically one token step at a time.

This distinction matters because prompt length primarily stresses prefill while output length primarily stresses decode.

## 2. Latency decomposition

A useful model is:

L_total =
network
+ queue
+ prefill
+ decode
+ post-processing

For a streaming service, also track:

**TTFT = time to first token**

**ITL = inter-token latency**

A request can have excellent total throughput but unacceptable TTFT.

## 3. Workload matrix

| Workload | Prompt | Output | Dominant concern |
|---|---:|---:|---|
| Short chat | short | short | scheduling/overhead |
| Long-document QA | long | short | prefill |
| Coding | medium | long | decode |
| Summarization | long | medium | both |
| RAG | long with evidence | medium | prefill + token cost |

Do not use a single synthetic prompt to represent all workloads.

## 4. Batch-size tradeoff

Higher batch/concurrency can improve hardware utilization.

But it may increase:

- queue time;
- TTFT;
- memory use;
- tail latency.

The engineering target is often:

**maximum throughput subject to p95/p99 latency constraints**

## 5. Worked example

Suppose:

| Concurrency | Throughput | TTFT p95 |
|---:|---:|---:|
| 1 | 20 tok/s | 150 ms |
| 4 | 70 tok/s | 190 ms |
| 16 | 180 tok/s | 420 ms |
| 32 | 250 tok/s | 900 ms |

If the SLA is TTFT p95 ≤500 ms, concurrency 32 may not qualify despite the higher throughput.

The useful operating point is determined by the SLA.

## 6. Long prompts

For a RAG workload, retrieved context can make prefill the bottleneck.

Therefore optimize:

- retrieval token count;
- prompt template;
- context ordering;
- prefix caching;
- batching;
- attention kernels.

Sometimes improving retrieval reduces latency more than changing the model.

## 7. Measurement protocol

For each benchmark record:

- model/checkpoint;
- precision/quantization;
- hardware;
- prompt length distribution;
- output length distribution;
- concurrency;
- streaming/non-streaming;
- TTFT p50/p95;
- ITL p50/p95;
- end-to-end latency;
- input/output tokens/sec;
- GPU memory/utilization.

## Research exercise

Benchmark one model at four concurrency levels and two prompt lengths.

Plot:

**throughput vs concurrency**

and:

**TTFT vs concurrency**

Identify the point where more batching stops meeting the latency target.

## Laboratory

[inference_and_kv_cache.ipynb](../../notebooks/inference_and_kv_cache.ipynb)

## Reference

https://docs.vllm.ai/en/stable/

## Deepening: prefill and decode create different bottlenecks

Prefill processes the prompt and creates the KV cache.

Decode repeatedly generates new tokens using the cached state.

### Workload decomposition

For each request record:

**prompt tokens + generated tokens + concurrency**

Then measure:

- TTFT;
- inter-token latency;
- output throughput;
- peak memory.

### Experiment

Hold generated tokens constant and increase prompt length.

Then hold prompt length constant and increase generated tokens.

Explain why the two experiments stress the system differently.

### Failure mode

A serving system optimized for short prompts can degrade sharply for long-context workloads.

### Decision

Capacity planning should use a workload distribution, not one average prompt.
