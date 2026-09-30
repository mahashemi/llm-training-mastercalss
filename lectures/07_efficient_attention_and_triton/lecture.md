# Lecture 07 — Efficient Attention, FlashAttention, and Triton

**Lab:** [Attention Memory and Tiling](`./lab.ipynb`)  
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

## Laboratory

Run sequence lengths:

128, 512, 2048, 4096.

Measure:

- peak memory;
- latency;
- throughput.

Compare against a naïve/materializing implementation where feasible.

## Break it

Use a shape that causes excessive padding/masking or a context length that exceeds practical memory.

Ask what failed:

**algorithm → kernel → memory → configuration**

## Exit challenge

Complete:

> “The optimized implementation wins because it changes ___, not because it changes ___.”

Expected reasoning: memory movement/materialization rather than merely reducing the mathematical definition of attention.

## Research bridge

Compare your measurements with FlashAttention's stated IO/memory motivation and identify where your small experiment does and does not represent the production algorithm.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
