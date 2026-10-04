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

## Laboratory

Run two controlled experiments:

1. fixed model, sequence length 512 vs 2048;
2. fixed sequence, batch 1 vs batch 4.

Record:

| Condition | Peak memory | tokens/sec | step time |
|---|---:|---:|---:|
| baseline | measure | measure | measure |
| changed | measure | measure | measure |

## Break it

Create a configuration that fits inference but fails training.

Diagnose which memory term caused failure.

## Exit challenge

You must answer:

> “Before renting another GPU, which quantity would you measure first, and why?”

The expected reasoning is **resource decomposition → measurement → intervention**, not GPU shopping.

## Research bridge

Read the relevant CS336 resource-accounting material and compare the assumptions behind its calculations with your measured run.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

This lab is part of this lecture. Do not leave the lecture to find the experiment: run the notebook, record the baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.

---

<div align="center">

[← Previous: Lecture 02 — Tokenization](../02_tokenization/lecture.md) · [Next: Lecture 04 — Transformer Architectures →](../04_transformer_architectures/lecture.md)

</div>