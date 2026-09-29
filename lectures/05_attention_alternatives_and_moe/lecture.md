# Lecture 05 — Attention Alternatives and Mixture-of-Experts

**Duration:** 25 minutes  
**Lab:** [Attention and MoE Lab](../../notebooks/attention_and_moe_lab.ipynb)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

Students can compare MHA, MQA, GQA, local attention, and MoE by the tensors they replicate, the memory they consume, and the communication/routing they introduce.

## 0–4 — Start from KV-cache pressure

Ask:

> During autoregressive generation, why store K and V for every prior token?

Then ask:

> What if many query heads shared fewer KV heads?

This motivates MQA/GQA.

## 4–9 — Head geometry

Let:

- H_q = query heads;
- H_kv = KV heads.

MHA: H_q = H_kv.

MQA: H_kv = 1.

GQA: 1 < H_kv < H_q.

Explain the memory implication for cached keys/values.

## 9–14 — MoE

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

## 14–19 — Laboratory

Students vary:

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

## 19–22 — Break it

Force one expert to receive most tokens.

Ask:

- Does quality necessarily fail?
- What fails first: load balance, throughput, or memory?

Separate algorithmic and systems failures.

## 22–24 — Engineering decision

Use a method when its resource benefit addresses the bottleneck:

**KV-cache bottleneck → GQA/MQA hypothesis**

**capacity-per-active-FLOP hypothesis → MoE**

Do not treat architectural novelty as a reason by itself.

## 24–25 — Exit challenge

Explain one benefit and one cost of MoE without saying “it is cheaper.”

## Research bridge

Read original GQA/MQA/MoE papers and compare active computation with total parameter count.
