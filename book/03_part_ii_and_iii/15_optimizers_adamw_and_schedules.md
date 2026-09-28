# Chapter 15 — Optimizers: AdamW and Schedules

**Part:** Part I

## 1. The optimizer controls how gradients become parameter updates

A training run contains:

**forward pass → loss → backward pass → gradients → optimizer update**

Adam-style optimization tracks:

- a first moment of gradients;
- a second moment of squared gradients.

Conceptually:

m_t = beta1 m_{t-1} + (1-beta1) g_t

v_t = beta2 v_{t-1} + (1-beta2) g_t^2

Then the parameter update uses bias-corrected moments and a learning rate.

AdamW separates weight decay from the adaptive gradient update.

## 2. Why optimizer choice matters

| Variable | Changes | Failure if poorly chosen |
|---|---|---|
| learning rate | update size | divergence / slow learning |
| beta1 | momentum response | noisy/over-smoothed updates |
| beta2 | variance tracking | unstable adaptation |
| weight decay | regularization | under/over-regularization |
| schedule | LR over time | poor convergence |
| warmup | early-step protection | instability at start |

## 3. Learning rate is often the highest-impact knob

A useful sweep:

| Run | Peak LR | Observation |
|---|---:|---|
| A | low | slower but stable |
| B | medium | target |
| C | high | faster or unstable |

Plot:

- train loss;
- validation loss;
- gradient norm;
- throughput.

A small LR sweep can be more informative than dozens of architecture changes.

## 4. Schedule design

Common patterns:

**constant**  
**warmup + cosine decay**  
**warmup + linear decay**

The schedule determines how much optimization pressure exists at different training stages.

## 5. Worked example

Suppose:

| Run | LR | Final train loss | Val loss | Result |
|---|---:|---:|---:|---|
| A | 1e-5 | 3.2 | 3.3 | under-training |
| B | 3e-5 | 2.7 | 2.8 | stable |
| C | 1e-4 | 2.2 | 4.5 | overfit/instability |

The lowest training loss is clearly not sufficient evidence.

## 6. Effective batch interaction

Optimizer behavior depends on effective batch size.

If batch increases substantially, reassess:

- learning rate;
- warmup;
- steps/token;
- gradient noise.

Do not copy a hyperparameter set from another batch regime without validation.

## 7. Debugging order

If loss diverges:

1. data;
2. numerical precision;
3. learning rate;
4. gradient norms/clipping;
5. optimizer implementation;
6. schedule;
7. architecture.

Fix the simplest plausible cause first.

## Research exercise

Run a 3-point learning-rate sweep.

Record:

**LR → warmup → final loss → validation loss → gradient norm → stability**

Then explain the choice using evidence rather than folklore.

## Laboratory

[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## Reference

https://cs231n.github.io/neural-networks-3/
