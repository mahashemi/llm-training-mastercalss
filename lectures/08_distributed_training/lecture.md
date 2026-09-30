# Lecture 08 — Distributed Training

**Lab:** [DDP and Sharding Simulation](./lab.ipynb)  
**Primary anchor:** PyTorch FSDP documentation — https://pytorch.org/docs/main/distributed.fsdp.fully_shard.html

## Outcome

You can explain replication versus sharding and derive why more GPUs do not automatically produce linear throughput.

## The one-GPU wall

Start with a model that cannot fit.

Ask:

> Do we need more compute, more memory, or both?

This distinguishes data parallelism from model/state sharding.

## DDP

Each worker holds a copy of model parameters.

Different batches are processed, then gradients are synchronized.

Draw:

**replicated model + different data → all-reduce gradients**

Advantages:

- simple;
- good scaling when the model fits.

Cost:

- replication.

## Sharding and parallelism

Compare:

| Strategy | What is split? | Main reason |
|---|---|---|
| DDP | data | throughput |
| FSDP/ZeRO | parameters/states | memory |
| tensor parallel | model dimensions | fit/throughput |
| pipeline parallel | layers | model fit |
| expert parallel | experts | MoE scaling |

Real systems combine these.

## Communication model

Use:

$T_{total}=T_{compute}+T_{communication}+T_{sync}+T_{I/O}$

As GPU count rises, communication and idle time can dominate.

Define:

$E_k = \frac{T_k}{kT_1}$

where T is throughput.

## Laboratory

Measure or simulate:

1, 2, 4, 8 GPUs.

Record:

- tokens/sec;
- scaling efficiency;
- communication fraction;
- memory.

Then deliberately lower the compute per step and see efficiency fall.

## H100 bridge

The H100's value in a cluster depends on:

- interconnect;
- topology;
- batch/token granularity;
- sharding;
- collective performance;
- checkpoint bandwidth.

A fast accelerator in a badly fed cluster is still badly utilized.

## Exit challenge

Answer:

> “At what point would adding GPUs stop being an attractive experiment, and what measurement proves it?”

## Research bridge

Read a current PyTorch FSDP guide and compare its abstractions with the simulated state partitioning.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.

---

<div align="center">

[← Previous lecture: Lecture 07 — Efficient Attention, FlashAttention, and Triton](../07_efficient_attention_and_triton/lecture.md) · [Next lecture: Lecture 09 — Scaling Laws →](../09_scaling_laws/lecture.md)

</div>
