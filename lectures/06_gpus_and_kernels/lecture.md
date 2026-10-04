# Lecture 06 — GPUs and Kernels

**Lab:** [GPU Kernel Benchmark](./lab.ipynb)  
**Primary anchor:** NVIDIA/H100 documentation + Stanford CS336 — https://cs336.stanford.edu/

## Outcome

You can explain why two mathematically equivalent implementations can have very different runtime.

## The benchmark surprise

Run one matrix multiply two ways.

Ask:

> If the math is identical, why isn't the runtime identical?

This opens the hardware discussion.

## Memory hierarchy

Walk through:

**HBM → cache/shared memory/registers**

Explain that kernels spend time moving data as well as performing arithmetic.

Introduce:

- memory bandwidth;
- compute throughput;
- kernel launch overhead;
- occupancy.

## Tensor Cores and precision

Compare:

**FP32 vs BF16 vs FP16 vs FP8**

without presenting precision as “more bits = better.”

Discuss:

- representational range;
- numerical stability;
- hardware acceleration;
- accumulation precision.

## Profiling before optimization

Run a benchmark and collect:

- wall-clock time;
- achieved throughput;
- memory utilization if available;
- repeated-run variance.

Then ask whether they are compute-bound or memory-bound.

## Laboratory break

Make matrix dimensions unfriendly to hardware alignment.

Compare with dimensions that map cleanly to common accelerator tile sizes.

Then discuss why kernels may change behavior abruptly.

## H100 bridge

The H100 is not just “a faster GPU.”

The relevant question is:

> How does this workload use its compute units, memory system, precision modes, and interconnect?

This is why the course measures the workload rather than quoting peak specifications.

## Exit challenge

Use:

**kernel → bottleneck → measurement → optimization → regression test**

## Research bridge

You should inspect one profiler trace and identify the top two contributors to step time.



## A worked example: the same matrix multiply can have different costs

Consider

$$
Y=AB
$$

with

$$
A\in\mathbb{R}^{1024\times4096},\qquad
B\in\mathbb{R}^{4096\times4096}.
$$

The mathematical operation is fixed, but the implementation decides where A and B live, how they are tiled, how threads cooperate, whether Tensor Cores are used, what precision is used, and how often data is moved.

A kernel is therefore not “just the equation.” It is a program that schedules the equation onto hardware.

## The memory hierarchy as a teaching model

Think of the GPU as a hierarchy:

**HBM → cache/shared memory → registers**

If a tile is reused by many multiply-add operations, loading it into a faster memory level can avoid repeatedly fetching it from HBM.

This is the intuition behind tiling and explains why two implementations with identical FLOPs can have very different runtimes.

## Precision is a systems decision

| Question | What to inspect |
|---|---|
| Can values be represented safely? | range and precision |
| Does hardware accelerate the format? | Tensor Core support |
| Where should accumulation happen? | accumulation precision |
| Does quality change? | task/error metric |
| Does throughput change? | samples/sec or tokens/sec |
| Does memory change? | peak bytes |

The correct experiment is not “BF16 is faster.” It is:

> **Does BF16 preserve the required quality while improving this workload’s resource profile?**

## Profiling walkthrough

1. Warm up the GPU.
2. Synchronize before timing.
3. Run repeated measurements.
4. Report median and spread.
5. Vary one dimension.
6. Inspect utilization/profile information.
7. Form a bottleneck hypothesis.
8. Change the implementation.
9. Rerun the same measurement.

Without warmup and synchronization, a timing number can describe Python scheduling rather than GPU execution.

## Real-world connection

Transformer training is a sequence of kernels: matrix multiplications, normalization, attention, communication, data movement, and bookkeeping.

A kernel that becomes 2× faster but occupies 1% of the step may barely move end-to-end training time. This is the difference between **microbenchmark optimization** and **system optimization**.

## Failure analysis

When an optimization disappoints, ask:

1. Did the optimized kernel actually run?
2. Did launch overhead dominate?
3. Was the workload memory-bound?
4. Was this kernel only a small fraction of end-to-end latency?
5. Did synchronization hide the gain?
6. Did the change increase another cost?

## Research extension

Change only matrix alignment or only precision. Predict the direction of latency and throughput before measuring. Explain non-monotonic behavior instead of treating it as noise.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 09 — Scaling Laws](../09_scaling_laws/lecture.md) · [Next: Lecture 11 — Efficient Attention and Triton →](../07_efficient_attention_and_triton/lecture.md)

</div>