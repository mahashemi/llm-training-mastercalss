# Lecture 08 — Distributed Training

**Duration:** 25 minutes  
**Lab:** [DDP and Sharding Simulation](../../notebooks/ddp_and_sharding_simulation.ipynb)  
**Primary anchor:** PyTorch FSDP documentation — https://pytorch.org/docs/main/distributed.fsdp.fully_shard.html

## Outcome

Students can explain replication versus sharding and derive why more GPUs do not automatically produce linear throughput.

## 0–4 — The one-GPU wall

Start with a model that cannot fit.

Ask:

> Do we need more compute, more memory, or both?

This distinguishes data parallelism from model/state sharding.

## 4–9 — DDP

Each worker holds a copy of model parameters.

Different batches are processed, then gradients are synchronized.

Draw:

**replicated model + different data → all-reduce gradients**

Advantages:

- simple;
- good scaling when the model fits.

Cost:

- replication.

## 9–14 — Sharding and parallelism

Compare:

| Strategy | What is split? | Main reason |
|---|---|---|
| DDP | data | throughput |
| FSDP/ZeRO | parameters/states | memory |
| tensor parallel | model dimensions | fit/throughput |
| pipeline parallel | layers | model fit |
| expert parallel | experts | MoE scaling |

Real systems combine these.

## 14–19 — Communication model

Use:

**total throughput = compute time + communication + synchronization + input/output**

As GPU count rises, communication and idle time can dominate.

Define:

**scaling efficiency = T_k / (k × T_1)**

where T is throughput.

## 19–22 — Laboratory

Measure or simulate:

1, 2, 4, 8 GPUs.

Record:

- tokens/sec;
- scaling efficiency;
- communication fraction;
- memory.

Then deliberately lower the compute per step and see efficiency fall.

## 22–24 — H100 bridge

The H100's value in a cluster depends on:

- interconnect;
- topology;
- batch/token granularity;
- sharding;
- collective performance;
- checkpoint bandwidth.

A fast accelerator in a badly fed cluster is still badly utilized.

## 24–25 — Exit challenge

Answer:

> “At what point would adding GPUs stop being an attractive experiment, and what measurement proves it?”

## Research bridge

Read a current PyTorch FSDP guide and compare its abstractions with the simulated state partitioning.
