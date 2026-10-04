# Lecture 03 — PyTorch and Resource Accounting

**Lab:** [Resource Accounting — FLOPs and Memory](./lab.ipynb)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

You learn to look at a model as a collection of tensors and resource terms rather than a parameter-count headline.

## The trap

Use:

> “This is a 7B model and it fits in 16 GB.”

Consider: whether that statement is enough to launch training.

No.

## Tensor dimensions first

Take one linear layer:

$X \in \mathbb{R}^{B \times L \times d_{in}}$  
$W \in \mathbb{R}^{d_{in} \times d_{out}}$  
$Y = XW$

Count the parameters:

**d_in × d_out**

Then ask what happens when B or L doubles.

Connect shape to compute before seeing FLOPs formulas.

## Memory decomposition

For training:

$M \approx M_{weights}+M_{gradients}+M_{optimizer}+M_{activations}+M_{runtime}$

For inference:

$M \approx M_{weights}+M_{KV}+M_{runtime}$

Example:

7B BF16 raw weights ≈ 14 GB decimal.

That is not a 14-GB training requirement.

## FLOPs and arithmetic intensity

Introduce a first-order dense-model training heuristic:

$\mathrm{FLOPs} \approx 6ND$

where N = parameters and D = training tokens.

Then distinguish:

- theoretical peak;
- achieved FLOPs/sec;
- tokens/sec;
- memory bandwidth;
- communication.

You should understand why a benchmark number from a GPU vendor is not the throughput of their training job.

## Break it

Create a configuration that fits inference but fails training.

Diagnose which memory term caused failure.

## Exit challenge

You must answer:

> “Before renting another GPU, which quantity would you measure first, and why?”

The expected reasoning is **resource decomposition → measurement → intervention**, not GPU shopping.

## Research bridge

Read the relevant CS336 resource-accounting material and compare the assumptions behind its calculations with your measured run.



## A worked example: why “7B” is not a memory specification

Suppose a model has 7 billion parameters and stores each parameter in BF16. Each BF16 value uses 2 bytes, so raw parameter storage is approximately:

$$
7\times10^9\times2 \approx 14\times10^9\text{ bytes} \approx 14\text{ GB}.
$$

That is only one term in a training system. Optimizer state, gradients, activations, temporary buffers, and runtime overhead can all matter.

### A concrete shape calculation

Let

$$
B=4,\quad L=2048,\quad d=4096.
$$

A hidden activation contains

$$
BLd=4\times2048\times4096\approx33.6\text{ million}
$$

elements. At BF16, one such tensor is about 67 MB. A Transformer keeps many intermediate tensors across layers, so activation memory can become substantial.

Now double the context length from 2048 to 4096. The hidden activation above doubles. Attention-related work also changes with sequence length, so “the model is still 7B” tells us very little about the actual run.

> **Never answer “Will it fit?” from parameter count alone. Write down the memory terms.**

## From formula to PyTorch

A useful resource-accounting workflow is:

1. inspect tensor shapes;
2. calculate parameter storage;
3. estimate activation storage;
4. account for gradients and optimizer state;
5. measure peak memory;
6. compare estimate with measurement;
7. identify the largest gap;
8. change one variable and measure again.

PyTorch matters here because it makes the computation inspectable: tensors, dtypes, devices, gradients, and memory can be observed rather than guessed.

## Real-world connection: choosing a training strategy

| Choice | What changes | Typical reason |
|---|---|---|
| smaller batch | fewer activations | fit memory |
| gradient accumulation | effective batch without larger per-step batch | fit memory |
| activation checkpointing | recompute instead of store | trade compute for memory |
| lower precision | fewer bytes and accelerated kernels | memory + throughput |
| sharding | distribute states | model does not fit on one GPU |

There is no universally best choice. The engineering question is:

> **Which resource is limiting this workload, and what trade-off am I willing to make?**

## Failure analysis

If a run runs out of memory, classify the failure:

- **weights:** the model itself does not fit;
- **optimizer:** training state is too large;
- **activations:** batch, sequence length, or depth is driving memory;
- **temporary/runtime:** kernels or allocators create large transient buffers;
- **distributed state:** replication or communication buffers are responsible.

Reproduce the smallest configuration that still fails. An OOM then becomes an experiment rather than a mysterious crash.

## Research extension

Make a falsifiable prediction before running the notebook. For example:

> Increasing sequence length from 1024 to 2048 will increase this experiment’s hidden-state activation memory by approximately 2×.

Measure the deviation and explain it instead of hiding it.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 02 — Tokenization](../02_tokenization/lecture.md) · [Next: Lecture 04 — Transformer Architectures →](../04_transformer_architectures/lecture.md)

</div>