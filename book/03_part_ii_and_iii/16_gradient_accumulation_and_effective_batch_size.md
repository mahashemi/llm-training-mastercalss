# Chapter 16 — Gradient Accumulation and Effective Batch Size

**Part:** Part I

## 1. Why accumulation exists

A large batch may not fit in accelerator memory.

Gradient accumulation lets the trainer process several micro-batches before applying one optimizer update.

If:

- micro-batch = M;
- data-parallel world size = W;
- accumulation steps = A;

then a common approximation is:

effective_batch ≈ M × W × A

subject to sequence packing/padding and implementation details.

## 2. Example

Suppose:

- micro-batch = 2 sequences/GPU;
- 8 GPUs;
- 8 accumulation steps.

Effective batch:

2 × 8 × 8 = 128 sequences/update

The model sees 64 micro-batches before the optimizer step.

## 3. Why batch size changes optimization

Changing effective batch size changes:

- gradient noise;
- number of optimizer updates per token;
- learning-rate behavior;
- throughput;
- memory;
- convergence dynamics.

Therefore accumulation is not only a memory trick.

## 4. Token-based accounting

For language modeling, sequences can have different lengths.

A better accounting unit is often:

**tokens/update = tokens/micro-batch × accumulation × data-parallel workers**

Example:

2 sequences × 2,048 tokens × 8 GPUs × 8 accumulation

= 262,144 tokens/update

This is much more informative than saying “batch 128.”

## 5. Memory vs throughput

| Change | Memory | Optimizer updates | Potential throughput |
|---|---|---|---|
| Larger micro-batch | ↑ | fewer per token | often ↑ |
| More accumulation | similar per micro-step | fewer optimizer updates | may ↓ due to extra launches |
| More GPUs | distributed | fewer local samples | often ↑ |
| Longer sequence | strongly ↑ | same sequence count | often ↓ |

Measure actual tokens/sec rather than assuming accumulation improves throughput.

## 6. Gradient scaling and correctness

With accumulation, gradients must be normalized consistently.

A common failure is averaging each micro-batch and then accidentally applying a different scale than intended.

Test a tiny case where:

**one large batch**

and:

**several accumulated micro-batches**

should produce nearly equivalent gradients under controlled conditions.

## 7. Learning-rate interactions

If effective batch increases substantially, the optimal learning-rate schedule may change.

Do not blindly copy a learning rate from a different batch regime.

Compare:

- tokens/update;
- updates/token;
- loss curve;
- gradient norm;
- validation loss.

## 8. Worked comparison

| Run | Micro-batch | Accumulation | Effective tokens/update | Val loss | Tok/s |
|---|---:|---:|---:|---:|---:|
| A | 2 | 1 | 32k | 2.8 | 20k |
| B | 2 | 8 | 256k | 2.7 | 18k |
| C | 4 | 4 | 256k | 2.7 | 25k |

B and C have the same effective batch but different micro-batch behavior and throughput.

This demonstrates why effective batch alone does not determine performance.

## Research exercise

Construct three configurations with the same effective token batch but different:

- micro-batch;
- accumulation;
- GPU count.

Measure:

**memory → tokens/sec → optimizer updates/token → validation loss**

Then explain which differences are hardware effects and which are optimization effects.

## Laboratory

[training_loop_instrumentation.ipynb](../../notebooks/training_loop_instrumentation.ipynb)

## Reference

https://cs336.stanford.edu/
