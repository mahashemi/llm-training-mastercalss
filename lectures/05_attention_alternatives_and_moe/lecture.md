# Lecture 05 — Attention Alternatives and Mixture-of-Experts

**Lab:** [Attention and MoE Lab](`./lab.ipynb`)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

You can compare MHA, MQA, GQA, local attention, and MoE by the tensors they replicate, the memory they consume, and the communication/routing they introduce.

## Start from KV-cache pressure

Ask:

> During autoregressive generation, why store K and V for every prior token?

Then ask:

> What if many query heads shared fewer KV heads?

This motivates MQA/GQA.

## Head geometry

Let:

- $H_q$ = query heads;
- $H_{kv}$ = KV heads.

MHA: $H_q = H_{kv}$.

MQA: $H_{kv}=1$.

GQA: 1 < H_kv < H_q.

Explain the memory implication for cached keys/values.

## MoE

Contrast dense and MoE:

**Dense:** every token visits the same FFN parameters.

**MoE:** a router selects a subset of experts.

Introduce:

- top-k routing;
- expert capacity;
- load balance;
- auxiliary/router losses;
- communication.

The crucial lesson:

> “Total parameters” and “active parameters per token” are different quantities.

## Laboratory

Vary:

- number of KV heads;
- sequence length;
- number of experts;
- top-k.

Measure:

| Configuration | KV memory | attention time | routing load | throughput |
|---|---:|---:|---:|---:|
| MHA | measure | measure | — | measure |
| GQA | measure | measure | — | measure |
| MQA | measure | measure | — | measure |

For MoE, deliberately create imbalanced routing and inspect expert utilization.

## Break it

Force one expert to receive most tokens.

Ask:

- Does quality necessarily fail?
- What fails first: load balance, throughput, or memory?

Separate algorithmic and systems failures.

## Engineering decision

Use a method when its resource benefit addresses the bottleneck:

**KV-cache bottleneck → GQA/MQA hypothesis**

**capacity-per-active-FLOP hypothesis → MoE**

Do not treat architectural novelty as a reason by itself.

## Exit challenge

Explain one benefit and one cost of MoE without saying “it is cheaper.”

## Research bridge

Read original GQA/MQA/MoE papers and compare active computation with total parameter count.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

This lab is part of this lecture. Do not leave the lecture to find the experiment: run the notebook, record the baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
