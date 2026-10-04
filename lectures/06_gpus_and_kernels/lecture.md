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


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

This lab is part of this lecture. Do not leave the lecture to find the experiment: run the notebook, record the baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.

---

<div align="center">

[← Previous: Lecture 09 — Scaling Laws](../09_scaling_laws/lecture.md) · [Next: Lecture 11 — Efficient Attention and Triton →](../07_efficient_attention_and_triton/lecture.md)

</div>