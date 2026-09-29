# Chapter 40 — Pretraining at Scale

**Part:** Part III

## 1. Scaling is a measured systems problem

A large pretraining run is governed by:

**model size + token budget + hardware + parallelism + data pipeline + reliability + evaluation**

The most common mistake is to specify the GPU count before measuring the model's throughput.

## 2. First-order compute

A common dense-model planning heuristic is:

FLOPs ≈ 6ND

where N is trainable parameters and D is training tokens.

For:

N = 7B  
D = 100B tokens

FLOPs ≈ 4.2e21

This is a first-order estimate, not an exact accounting of every operation.

## 3. Convert compute to time

If delivered throughput is F_eff:

time = total_FLOPs / F_eff

This is why measured throughput is more useful than theoretical peak.

## 4. Scale efficiency

Define:

efficiency(k) =
throughput(k) / [k × throughput(1)]

Example:

| GPUs | Throughput | Ideal | Efficiency |
|---:|---:|---:|---:|
| 1 | 50 | 50 | 100% |
| 2 | 95 | 100 | 95% |
| 4 | 180 | 200 | 90% |
| 8 | 320 | 400 | 80% |
| 16 | 560 | 800 | 70% |

The values are illustrative.

The curve tells you where communication begins to dominate.

## 5. Parallelism choice

| Strategy | Splits | Main benefit | Main cost |
|---|---|---|---|
| Data parallel | batches | simple scaling | replication |
| Tensor parallel | model dimensions | fit/throughput | communication |
| Pipeline parallel | layers | model fit | bubbles/scheduling |
| FSDP/sharding | states/parameters | memory efficiency | communication |
| Expert parallel | MoE experts | capacity scaling | routing/communication |

Real systems combine several.

## 6. Data pipeline

GPU utilization depends on:

**storage → read → decode → tokenize/load → host memory → transfer → GPU**

Profile each stage.

A perfect GPU kernel cannot compensate for a starved input pipeline.

## 7. Evaluation during pretraining

Large runs should include scheduled probes:

- validation loss;
- domain loss;
- multilingual loss;
- task benchmarks;
- safety probes.

Do not wait until the end to discover that the training mix is wrong.

## 8. Worked scaling decision

Suppose:

- 8 GPUs: 320 units throughput;
- 16 GPUs: 560;
- 32 GPUs: 880.

If cost doubles from 16 to 32 GPUs but throughput rises only 57%, the larger cluster may not be justified for a latency-sensitive deadline.

The decision depends on:

**wall-clock requirement + cost + availability + utilization + failure risk**

## 9. Research exercise

Run a small model at 1, 2, 4, and 8 GPUs.

Measure:

- tokens/sec;
- effective FLOPs/sec;
- scaling efficiency;
- communication fraction;
- memory;
- cost/hour.

Fit a simple throughput curve and identify the economic scaling limit.

## Laboratory

[resource_accounting_flops_memory.ipynb](../../notebooks/resource_accounting_flops_memory.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
- Chinchilla: https://arxiv.org/abs/2203.15556


## Deepening: derive the cluster from measured throughput

Do not begin with “we need 64 H100s.”

Begin with:

1. target tokens;
2. target wall time;
3. measured tokens/sec on one GPU;
4. measured scaling efficiency;
5. checkpoint/data pipeline limits.

### Worked derivation

If a one-GPU pilot delivers T tokens/sec and a k-GPU run achieves efficiency e:

cluster throughput ≈ k × T × e

Required time:

time ≈ total_training_tokens / cluster_throughput

This gives a defensible GPU-count estimate.

### Scaling experiment

Measure 1, 2, 4 and 8 GPUs for a representative workload.

Record:

| GPUs | tokens/sec | scaling efficiency | communication fraction | peak memory |
|---:|---:|---:|---:|---:|
| 1 | measure | 100% | measure | measure |
| 2 | measure | measure | measure | measure |
| 4 | measure | measure | measure | measure |
| 8 | measure | measure | measure | measure |

Then fit a simple throughput curve.

### Hidden bottlenecks

A large cluster can be limited by:

- input pipeline;
- checkpoint writes;
- network;
- synchronization;
- evaluation;
- failed workers.

The fastest GPU is useless when it is waiting.

### H100 bridge

The H100 is introduced first as a measurement instrument. Students learn its performance only after measuring their workload, rather than treating the accelerator specification as the experiment.
