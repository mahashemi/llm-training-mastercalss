# Chapter 14 — Initialization and Optimization Stability

**Part:** Part I

## 1. Stability is a first-class training metric

A run can fail before it produces useful learning:

- loss becomes NaN;
- gradients explode;
- activations saturate;
- validation loss diverges;
- throughput collapses because of numerical retries.

Training stability should therefore be monitored continuously.

## 2. Why initialization matters

At initialization, parameter scales influence:

- activation variance;
- gradient variance;
- residual-stream magnitude;
- optimizer behavior.

A poor scale can make early layers unstable or make gradients too small to learn efficiently.

## 3. What to instrument

| Signal | Healthy use |
|---|---|
| loss | learning progress |
| validation loss | generalization |
| gradient norm | exploding/vanishing behavior |
| activation norm | layer-scale stability |
| parameter norm | update magnitude |
| update/parameter ratio | optimization aggressiveness |
| NaN/Inf count | numerical failure |
| throughput | systems stability |

A good training dashboard shows these together.

## 4. Common failure patterns

### Exploding gradients
Loss becomes unstable and gradient norms spike.

Investigate:

- learning rate;
- initialization;
- sequence length;
- numerical precision;
- architecture.

### Vanishing updates
Loss barely moves and update/parameter ratio is tiny.

Investigate:

- learning rate;
- normalization;
- initialization;
- dead/saturated computations.

### NaNs
Can arise from:

- invalid kernels;
- overflow;
- unstable softmax;
- bad inputs;
- mixed-precision issues.

## 5. Normalization and residual pathways

Modern Transformer stability depends heavily on where normalization occurs relative to residual connections.

Compare designs experimentally rather than memorizing a single pattern.

Useful measurements:

**activation norm by layer**

**gradient norm by layer**

This reveals where instability originates.

## 6. Worked example

Suppose:

| Step | Loss | Grad norm | Status |
|---:|---:|---:|---|
| 100 | 5.2 | 4 | stable |
| 200 | 4.8 | 7 | stable |
| 300 | 4.1 | 25 | warning |
| 400 | NaN | Inf | failure |

A response is not “restart and hope.”

Test:

- lower LR;
- gradient clipping;
- precision change;
- check input batch;
- inspect the layer with abnormal activations.

## 7. Gradient clipping

A simple clipping rule limits gradient norm to a threshold.

This can improve stability, but it can also mask a deeper problem.

Measure how often clipping activates.

If clipping triggers on nearly every step, investigate the training configuration rather than celebrating stability.

## 8. Stability experiment

Run three configurations:

| Run | LR | Clip threshold | Result |
|---|---:|---:|---|
| A | baseline | none | measure |
| B | baseline | 1.0 | measure |
| C | 0.5× | 1.0 | measure |

Compare:

- convergence;
- validation loss;
- clipping frequency;
- gradient norms;
- throughput.

## Research exercise

Instrument layerwise activation and gradient norms in a tiny Transformer.

Create one intentionally unstable configuration.

Identify the earliest signal that predicts the final failure.

## Laboratory

[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## References

https://cs336.stanford.edu/
