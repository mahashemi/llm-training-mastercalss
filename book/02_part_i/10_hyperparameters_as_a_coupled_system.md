# Chapter 10 — Hyperparameters as a Coupled System

**Part:** Part I

## 1. Hyperparameters interact

Do not treat training settings as isolated knobs.

Important coupled variables include:

- learning rate;
- effective batch size;
- sequence length;
- optimizer;
- warmup;
- weight decay;
- training duration;
- model size.

Changing one can change the appropriate value of another.

## 2. Resource variables

| Variable | Quality effect | Resource effect |
|---|---|---|
| batch size | optimization dynamics | memory |
| sequence length | context capability | quadratic attention pressure |
| model width | capacity | compute/memory |
| learning rate | convergence | instability risk |
| accumulation | effective batch | memory/throughput |
| precision | numerical behavior | memory/speed |

## 3. Why random sweeps are inefficient

Suppose you vary:

- 5 learning rates;
- 4 batch sizes;
- 3 sequence lengths;
- 3 weight-decay values.

That is:

5×4×3×3 = 180 combinations

Most may be unnecessary.

Start with a small hypothesis-driven design.

## 4. Example sweep

| Run | LR | Batch | Sequence | Question |
|---|---:|---:|---:|---|
| A | low | base | base | under-update |
| B | medium | base | base | baseline |
| C | high | base | base | stability |
| D | medium | 2× | base | batch effect |
| E | medium | base | 2× | context cost |

Change one dimension at a time first.

## 5. Resource accounting

For a fixed model:

doubling sequence length can increase attention interaction count by about 4×.

Doubling effective batch does not necessarily double activation memory if accumulation is used instead of a larger micro-batch.

This distinction matters for hardware planning.

## 6. Worked decision

Suppose quality is similar for:

- Run B: 20k tokens/sec;
- Run D: 30k tokens/sec.

D may be preferable operationally, but only after checking:

- convergence;
- validation loss;
- GPU utilization;
- stability.

Throughput is not the objective if quality changes.

## 7. Research exercise

Design a five-run hyperparameter experiment.

For each run record:

**configuration → GPU memory → tokens/sec → loss → validation → instability**

Then identify which variable produced the largest useful improvement per unit resource.

## Laboratory

[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## Reference

https://cs336.stanford.edu/

## Deepening: hyperparameters form a resource-constrained system

Learning rate, batch size, sequence length, optimizer, and training duration interact.

### Effective batch tokens

A useful accounting identity is:

**global batch tokens ≈ micro-batch × gradient accumulation × sequence length × data-parallel world size**

Changing sequence length therefore changes both memory and the number of tokens processed per optimizer update.

### Experiment

Hold total training tokens approximately constant and compare:

| Run | micro-batch | accumulation | sequence | peak memory | tokens/sec |
|---|---:|---:|---:|---:|---:|
| A | 1 | 16 | 512 | measure | measure |
| B | 1 | 4 | 2048 | measure | measure |

Then ask whether equal token counts imply equal optimization behavior.

### Failure mode

Change learning rate while also changing batch size. You can no longer attribute the result to one variable.

### Engineering lesson

The correct unit of tuning is often a **configuration**, not a single hyperparameter.
