# Chapter 3 — Logits, Softmax, and Cross-Entropy

**Part:** Part I

## 1. The model outputs scores, not probabilities

For vocabulary size V, the final linear layer produces:

z ∈ R^V

where z are **logits**.

Softmax converts logits into probabilities:

p_i = exp(z_i) / Σ_j exp(z_j)

The model then assigns a probability to the observed next token.

## 2. Why logits are useful

A logit vector can be shifted by the same constant without changing softmax probabilities.

For numerical stability, implementations commonly subtract the maximum logit before exponentiation:

softmax(z)_i = exp(z_i - max(z)) / Σ_j exp(z_j - max(z))

This prevents unnecessary overflow.

## 3. Cross-entropy

For the correct target token y:

L = -log p_y

Example:

| Correct-token probability | Loss |
|---:|---:|
| 0.90 | 0.105 |
| 0.50 | 0.693 |
| 0.10 | 2.303 |
| 0.01 | 4.605 |

A confident wrong prediction is therefore heavily penalized.

## 4. Why lower loss is meaningful

The objective rewards assigning probability mass to the observed data distribution.

But lower token loss does not directly guarantee:

- instruction following;
- factuality;
- safety;
- tool reliability.

Those need additional evaluation.

## 5. Gradient intuition

For softmax cross-entropy:

∂L/∂z_i = p_i − 1[i=y]

So:

- if a wrong token has high probability, its gradient pushes it down;
- the target token receives a gradient pushing its probability up.

This is the core learning signal for next-token prediction.

## 6. Temperature is not training loss

At inference:

p_i(T) ∝ exp(z_i/T)

Lower T makes the distribution sharper; higher T makes it flatter.

Temperature changes **sampling behavior**, not the learned model weights.

Therefore do not compare a model's capability using inconsistent decoding settings.

## 7. Worked example

Suppose target probability is:

0.2

Then:

L = -log(0.2) ≈ 1.61

After training it becomes:

0.5

L ≈ 0.69

The loss contribution fell by roughly 0.92 nats for that example.

## 8. Failure modes

### Saturated probabilities
Very large logit differences can create numerical issues without stable implementations.

### Wrong target alignment
A label/token shift error can make a correct model look broken.

### Padding leakage
Loss must exclude invalid/padded positions.

## Research exercise

Implement:

- stable softmax;
- cross-entropy;
- a small next-token classifier.

Compare your implementation with PyTorch on random tensors.

Then intentionally shift labels by one position and observe how the loss changes.

## Laboratory

[01_next_token_prediction_and_a_tiny_language_model.ipynb](../../notebooks/01_next_token_prediction_and_a_tiny_language_model.ipynb)

## Reference

https://cs231n.github.io/neural-networks-case-study/

## Deepening: loss is an information signal

### Numerical example

If the correct token has probability:

- 0.9 → loss = −log(0.9) ≈ 0.105
- 0.1 → loss = −log(0.1) ≈ 2.303
- 0.01 → loss = −log(0.01) ≈ 4.605

The loss therefore changes nonlinearly as probability assigned to the target changes.

### Tensor shapes

For batch B, sequence length L, and vocabulary V:

**logits: B × L × V**

The target labels have shape:

**B × L**

The loss reduces these predictions against the observed target tokens.

### Failure experiment

Shift labels by one position.

If the model is correctly predicting token t from context through t−1, a misaligned target changes the learning signal even though every tensor still has a valid shape.

### Engineering consequence

A training run can be numerically healthy while learning the wrong task because of a labeling/template error. Always test one hand-verified batch before scaling.
