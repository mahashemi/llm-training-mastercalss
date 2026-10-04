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



## A worked example: why eight GPUs need not be eight times faster

Suppose one GPU processes 1000 tokens/s. An ideal eight-GPU system would process 8000 tokens/s.

Define scaling efficiency:

$$
E_8=\frac{T_8}{8T_1}.
$$

If measured throughput is 6400 tokens/s,

$$
E_8=\frac{6400}{8\times1000}=0.8.
$$

The system achieved 80% scaling efficiency. The missing 20% can come from communication, synchronization, input stalls, load imbalance, or framework overhead.

## DDP from first principles

Suppose two workers receive different mini-batches.

**worker 0: model copy + batch A → gradients g₀**  
**worker 1: model copy + batch B → gradients g₁**  
**g₀ and g₁ → all-reduce → synchronized update**

The important limitation is that each worker still needs the model and training state. DDP improves aggregate data processing but does not make a model that cannot fit suddenly fit.

## Sharding changes the question

With sharding, model states are partitioned across workers. A simplified memory view is

$$
M_{\text{per GPU}}\approx\frac{M_{\text{states}}}{K}+M_{\text{local overhead}}
$$

where K is the number of participating GPUs.

This can make a previously impossible model fit, but introduces communication and coordination.

## Real-world connection: choosing a parallelism strategy

| Problem | First strategy to investigate |
|---|---|
| model fits, want throughput | data parallelism |
| model states do not fit | FSDP/ZeRO-style sharding |
| individual layers are too large | tensor/model parallelism |
| very deep model | pipeline parallelism |
| sparse MoE | expert parallelism |

These strategies are often combined.

## Failure analysis

Distributed runs commonly fail in ways that look like “the GPUs are slow” but are actually:

- network bandwidth limits;
- collective synchronization;
- uneven batch sizes;
- slow data loading;
- checkpoint I/O;
- stragglers;
- poor topology.

Measure the timeline before changing the cluster.

## Research extension

Run one scaling experiment with fixed global batch size and another with fixed per-GPU batch size. Explain how the two experiments answer different questions about scaling.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 11 — Efficient Attention and Triton](../07_efficient_attention_and_triton/lecture.md) · [Next: Lecture 13 — Evaluation →](../12_evaluation/lecture.md)

</div>
## Video companions

[Video companions: distributed deep learning and data parallelism](https://www.youtube.com/results?search_query=distributed+deep+learning+data+parallelism+lecture)

## Navigation

[← Previous](../07_efficient_attention_and_triton/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../09_scaling_laws/lecture.md)
