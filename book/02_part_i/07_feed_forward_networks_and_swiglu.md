# Chapter 7 — Feed-Forward Networks and SwiGLU

**Part:** Part I

## 1. Attention is only part of a Transformer block

A typical decoder block contains:

**normalization → attention → residual → normalization → MLP → residual**

The MLP provides a large fraction of the block's parameters and performs token-wise nonlinear transformation.

## 2. Standard MLP

A simplified MLP:

MLP(x) = W_2 σ(W_1 x)

The hidden dimension is often larger than d_model.

This expansion gives the network substantial nonlinear capacity.

## 3. Gated MLP intuition

A gated design uses multiple projections, for example:

SwiGLU(x) = (SiLU(xW_gate) ⊙ xW_up) W_down

The gate modulates which hidden features contribute.

## 4. Parameter accounting

For model width d and MLP hidden width m, a simple three-projection gated MLP has approximate parameter count:

3dm

ignoring biases.

Example:

d = 4096  
m = 11,008

Approximate MLP parameters:

3 × 4096 × 11,008 ≈ 135M

This explains why MLP dimensions strongly influence total model size.

## 5. Compute implications

For sequence length T:

MLP compute is approximately proportional to:

T × d × m

Unlike dense self-attention's T² interaction term, the MLP scales roughly linearly with sequence length.

At sufficiently long context, attention can dominate; at shorter sequences, MLPs can be a large share of total compute.

## 6. Why gated designs matter

Potential benefits include:

- richer nonlinear transformations;
- parameter-efficient gating;
- good empirical quality.

But the extra projection increases parameter and compute cost.

Evaluate the whole architecture.

## 7. Worked comparison

| Design | Hidden width | Projections | Approx. params |
|---|---:|---:|---:|
| Standard | 11,008 | 2 | ~90M |
| Gated | 11,008 | 3 | ~135M |
| Gated, smaller m | 8,192 | 3 | ~101M |

A model can preserve similar parameter scale by adjusting hidden width.

## Research exercise

Implement:

1. standard GELU MLP;
2. SwiGLU MLP.

Measure:

- parameter count;
- forward time;
- activation memory;
- tiny-language-model validation loss.

Then compare quality per parameter and quality per compute.

## Laboratory

[build_a_tiny_transformer.ipynb](../../notebooks/build_a_tiny_transformer.ipynb)

## References

- LLaMA: https://arxiv.org/abs/2302.13971
- GLU Variants Improve Transformer: https://arxiv.org/abs/2002.05202
