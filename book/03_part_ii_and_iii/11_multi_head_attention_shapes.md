# Chapter 11 — Multi-Head Attention Shapes

**Part:** Part I

## 1. The tensor shapes are the mechanism

Let:

- B = batch size;
- T = sequence length;
- d_model = model width;
- h = query heads;
- d_head = head dimension.

Usually:

d_model = h × d_head

Input:

X ∈ R^(B×T×d_model)

Projection:

Q = XW_Q  
K = XW_K  
V = XW_V

with head-separated representations.

## 2. One-head calculation

For one head:

Q_h, K_h, V_h ∈ R^(B×T×d_head)

Attention scores:

S = Q_h K_h^T / sqrt(d_head)

S has shape:

B × T × T

After softmax:

A = softmax(S)

Output:

O_h = A V_h

Again:

B × T × d_head

Concatenate h heads:

B × T × (h d_head) = B × T × d_model

## 3. Why the T² term matters

The score matrix has T×T interactions.

Approximate attention work therefore grows strongly with sequence length:

O(B T² d_model)

Example:

| Context | Relative attention interaction count |
|---:|---:|
| 1k | 1× |
| 2k | 4× |
| 4k | 16× |
| 8k | 64× |
| 16k | 256× |

This is the systems reason efficient attention and long-context engineering matter.

## 4. Parameter accounting

For a standard self-attention block, Q/K/V projections plus output projection are each roughly d_model² in parameter scale.

Approximate attention projection parameters:

4 d_model²

ignoring biases and implementation-specific variations.

For d_model = 4096:

4 × 4096² ≈ 67.1M parameters

for the four large projections.

## 5. Head-count trade-offs

At fixed d_model:

| Heads h | d_head if d_model=4096 | Main effect |
|---:|---:|---|
| 16 | 256 | fewer wider heads |
| 32 | 128 | common configuration |
| 64 | 64 | more narrower heads |

More heads do not automatically mean better quality.

Hardware kernels and memory layout also matter.

## 6. Worked example

Suppose:

B=4, T=2048, d_model=1024, h=16.

Then:

d_head = 64

The score tensor per layer has:

B×h×T×T
= 4×16×2048²
≈ 268 million score elements

At 2 bytes/element this is roughly 536 MB before other tensors.

This explains why attention memory can dominate long-sequence workloads.

## Research exercise

Implement a single attention head in PyTorch.

Print every tensor shape for:

B=2, T=128, d_model=512, h=8.

Then vary T from 128 to 1024 and measure memory/time.

## Laboratory

[build_a_tiny_transformer.ipynb](../../notebooks/build_a_tiny_transformer.ipynb)

## Reference

https://arxiv.org/abs/1706.03762
