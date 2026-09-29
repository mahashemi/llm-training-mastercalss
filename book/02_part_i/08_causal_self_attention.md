# Chapter 8 — Causal Self-Attention

**Part:** Part I

## 1. The mechanism

Given Q, K, V:

S = QK^T / sqrt(d_head)

Apply a causal mask so position t cannot attend to positions > t.

Then:

A = softmax(S + mask)

Output:

O = AV

## 2. Why causal masking is necessary

For next-token prediction, token t must not see its future target.

Without masking, the model could directly inspect information it is supposed to predict.

That would invalidate the autoregressive training objective.

## 3. Shape accounting

For B batch, T sequence length, H heads, D head dimension:

Q,K,V ∈ R^(B×H×T×D)

Scores:

S ∈ R^(B×H×T×T)

This T² structure drives attention memory.

## 4. Worked memory example

Suppose:

B=8  
H=32  
T=2048  
BF16=2 bytes

Raw score elements:

8×32×2048² ≈ 1.07 billion elements

At 2 bytes:

≈2.15 GB

This is why storing full attention matrices can be expensive.

Efficient attention kernels avoid materializing the full matrix in the same way.

## 5. Computational complexity

A rough score-computation cost:

O(BHT²D)

A second term exists for multiplying attention weights by V.

Both grow strongly with T.

## 6. Causal mask implementation

A common implementation uses a triangular mask.

Test that:

- position 0 sees only position 0;
- position 1 sees positions 0–1;
- position T−1 can see the full prefix.

A one-line masking bug can silently corrupt training.

## 7. Failure analysis

### Future-token leakage
Training loss becomes suspiciously good.

### Wrong mask shape
Broadcasting bugs produce incorrect attention.

### Numerical instability
Large logits can create NaNs without stable softmax.

## Research exercise

Implement causal attention from matrix operations.

Add tests that assert future positions have zero attention probability.

Then benchmark T = 256, 512, 1024, 2048 and measure memory/time.

## Laboratory

[attention_and_moe_lab.ipynb](../../notebooks/attention_and_moe_lab.ipynb)

## References

- Transformer: https://arxiv.org/abs/1706.03762
- FlashAttention: https://arxiv.org/abs/2205.14135


## Deepening: attention is a memory problem

For sequence length L and head dimension d, the naive attention score matrix has O(L²) elements per head.

The important classroom question is not only “why is attention quadratic?”

It is:

> **Which tensor becomes large, and what happens to GPU memory when L doubles?**

Run a controlled experiment with:

- L = 128;
- L = 512;
- L = 2048;
- L = 4096.

Measure:

| L | score-memory estimate | measured peak memory | attention time |
|---:|---:|---:|---:|
| 128 | calculate | measure | measure |
| 512 | calculate | measure | measure |
| 2048 | calculate | measure | measure |
| 4096 | calculate | measure | measure |

Then compare naive attention with a memory-efficient implementation.

### Engineering consequence

A model may fit at sequence length 2k and fail at 8k even though the parameter count is unchanged.

This is why “model size” is not a sufficient hardware specification.

### Research bridge

Ask whether the bottleneck is:

- score materialization;
- activation storage;
- kernel efficiency;
- KV cache;
- bandwidth.

Students should learn to identify the tensor or kernel responsible rather than memorizing “quadratic.”
