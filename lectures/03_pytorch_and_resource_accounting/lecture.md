# Lecture 03 — PyTorch and Resource Accounting

**Duration:** 25 minutes  
**Lab:** [Resource Accounting — FLOPs and Memory](`./lab.ipynb`)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

Students learn to look at a model as a collection of tensors and resource terms rather than a parameter-count headline.

## 0–4 — The trap

Write:

> “This is a 7B model and it fits in 16 GB.”

Ask whether that statement is enough to launch training.

No.

## 4–8 — Tensor dimensions first

Take one linear layer:

**X ∈ R^(B×L×d_in)**  
**W ∈ R^(d_in×d_out)**  
**Y = XW**

Count the parameters:

**d_in × d_out**

Then ask what happens when B or L doubles.

Students connect shape to compute before seeing FLOPs formulas.

## 8–14 — Memory decomposition

For training:

**M ≈ weights + gradients + optimizer + activations + temporary/runtime**

For inference:

**M ≈ weights + KV cache + runtime**

Example:

7B BF16 raw weights ≈ 14 GB decimal.

That is not a 14-GB training requirement.

## 14–19 — FLOPs and arithmetic intensity

Introduce a first-order dense-model training heuristic:

**FLOPs ≈ 6ND**

where N = parameters and D = training tokens.

Then distinguish:

- theoretical peak;
- achieved FLOPs/sec;
- tokens/sec;
- memory bandwidth;
- communication.

Students should understand why a benchmark number from a GPU vendor is not the throughput of their training job.

## 19–22 — Laboratory

Run two controlled experiments:

1. fixed model, sequence length 512 vs 2048;
2. fixed sequence, batch 1 vs batch 4.

Record:

| Condition | Peak memory | tokens/sec | step time |
|---|---:|---:|---:|
| baseline | measure | measure | measure |
| changed | measure | measure | measure |

## 22–24 — Break it

Create a configuration that fits inference but fails training.

Diagnose which memory term caused failure.

## 24–25 — Exit challenge

Students must answer:

> “Before renting another GPU, which quantity would you measure first, and why?”

The expected reasoning is **resource decomposition → measurement → intervention**, not GPU shopping.

## Research bridge

Read the relevant CS336 resource-accounting material and compare the assumptions behind its calculations with your measured run.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

This lab is part of this lecture. Do not leave the lecture to find the experiment: run the notebook, record the baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
