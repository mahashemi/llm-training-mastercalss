# Lecture 07 — Efficient Attention, FlashAttention, and Triton

**Lab:** [Attention Memory and Tiling](./lab.ipynb)  
**Primary anchor:** FlashAttention — https://arxiv.org/abs/2205.14135

## Outcome

You understand that attention optimization can come from reducing memory traffic and avoiding materialization, not only from reducing mathematical FLOPs.

## Same equation, different system cost

Compare naive attention and a memory-efficient implementation.

Ask:

> If both compute the same attention result, where did the speedup come from?

## Why materialization matters

Explain that naïve attention can materialize large score/probability tensors.

For sequence length L, the attention matrix has O(L²) entries per head.

The optimization goal is to keep useful tiles in fast memory and avoid unnecessary HBM traffic.

## Tiling and online softmax

Introduce the conceptual loop:

**load tile → update running statistics → accumulate output → discard tile**

You do not need to implement production FlashAttention yet; they need to understand the data movement.

## Triton mental model

Explain:

- program instances;
- blocks;
- masks;
- memory loads/stores;
- launch grid.

Tie each abstraction back to the tensor being computed.

## Break it

Use a shape that causes excessive padding/masking or a context length that exceeds practical memory.

Consider: what failed:

**algorithm → kernel → memory → configuration**

## Exit challenge

Complete:

> “The optimized implementation wins because it changes ___, not because it changes ___.”

Expected reasoning: memory movement/materialization rather than merely reducing the mathematical definition of attention.

## Research bridge

Compare your measurements with FlashAttention's stated IO/memory motivation and identify where your small experiment does and does not represent the production algorithm.



## Work through one attention tile

For one attention head,

$$
S=QK^\top,\qquad
P=\operatorname{softmax}(S),\qquad
O=PV.
$$

A naïve implementation can materialize S and P. For sequence length L, each contains roughly L² entries per head.

For

$$
L=4096,
$$

we have

$$
L^2=16{,}777{,}216
$$

entries per head before considering batches, heads, and element size.

The key insight is not that the attention equation is wrong. The problem is that intermediate matrices can be expensive to move to and from HBM.

### What tiling changes

Instead of computing the entire score matrix at once, process blocks conceptually as:

**load tile → update running statistics → accumulate output → discard tile**

Useful intermediate information stays close to the compute units while tiles that are no longer needed are discarded.

The mathematical result is preserved while the **IO schedule** changes.

## Online softmax intuition

Softmax appears to require an entire row because

$$
\operatorname{softmax}(x_i)=\frac{e^{x_i}}{\sum_j e^{x_j}}.
$$

A tiled implementation can maintain running maximum and normalization statistics as new blocks arrive. This allows accumulation without storing the complete score matrix.

The design principle is:

> **Reorganize computation so expensive memory traffic is avoided while preserving the mathematical result.**

## Triton: from tensor equation to kernel program

A Triton kernel makes you think about:

- which program instance owns a block;
- which elements are loaded;
- how masks handle boundaries;
- where intermediate values live;
- which values are written back.

This is the bridge between high-level PyTorch and low-level accelerator programming.

## Real-world connection: long-context inference

Attention optimization matters disproportionately as context grows. A system serving short prompts may tolerate an implementation that becomes unacceptable at long context.

The engineering objective is therefore not simply “make attention faster.” It is:

> **Reduce latency and memory traffic at the sequence lengths the product actually serves.**

## Failure analysis

An optimized attention implementation can still lose because:

- the sequence is too short for tiling benefits to amortize;
- dimensions create inefficient masking;
- another kernel dominates end-to-end latency;
- numerical behavior differs;
- compilation/setup time contaminates the benchmark;
- the hardware differs from the reference system.

Compare identical outputs within an agreed tolerance before comparing speed.

## Research extension

Choose three sequence lengths and predict where the crossover between naïve and tiled attention should occur. Measure latency, peak memory, and numerical error. Report the crossover, not only the fastest configuration.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 10 — GPUs and Kernels](../06_gpus_and_kernels/lecture.md) · [Next: Lecture 12 — Distributed Training →](../08_distributed_training/lecture.md)

</div>
## Video companions

[Video companions: FlashAttention and Triton](https://www.youtube.com/results?search_query=FlashAttention+Triton+lecture)

## Navigation

[← Previous](../06_gpus_and_kernels/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../08_distributed_training/lecture.md)
