# Lecture 07 — Efficient Attention, FlashAttention, and Triton

**Duration:** 25 minutes  
**Lab:** [Attention Memory and Tiling](../../notebooks/attention_memory_and_tiling.ipynb)  
**Primary anchor:** FlashAttention — https://arxiv.org/abs/2205.14135

## Outcome

Students understand that attention optimization can come from reducing memory traffic and avoiding materialization, not only from reducing mathematical FLOPs.

## 0–4 — Same equation, different system cost

Compare naive attention and a memory-efficient implementation.

Ask:

> If both compute the same attention result, where did the speedup come from?

## 4–10 — Why materialization matters

Explain that naïve attention can materialize large score/probability tensors.

For sequence length L, the attention matrix has O(L²) entries per head.

The optimization goal is to keep useful tiles in fast memory and avoid unnecessary HBM traffic.

## 10–15 — Tiling and online softmax

Introduce the conceptual loop:

**load tile → update running statistics → accumulate output → discard tile**

Students do not need to implement production FlashAttention yet; they need to understand the data movement.

## 15–19 — Triton mental model

Explain:

- program instances;
- blocks;
- masks;
- memory loads/stores;
- launch grid.

Tie each abstraction back to the tensor being computed.

## 19–22 — Laboratory

Run sequence lengths:

128, 512, 2048, 4096.

Measure:

- peak memory;
- latency;
- throughput.

Compare against a naïve/materializing implementation where feasible.

## 22–24 — Break it

Use a shape that causes excessive padding/masking or a context length that exceeds practical memory.

Ask what failed:

**algorithm → kernel → memory → configuration**

## 24–25 — Exit challenge

Complete:

> “The optimized implementation wins because it changes ___, not because it changes ___.”

Expected reasoning: memory movement/materialization rather than merely reducing the mathematical definition of attention.

## Research bridge

Compare your measurements with FlashAttention's stated IO/memory motivation and identify where your small experiment does and does not represent the production algorithm.
