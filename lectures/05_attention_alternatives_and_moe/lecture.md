# Lecture 05 — Attention Alternatives and Mixture-of-Experts

**Lab:** [Attention and MoE Lab](./lab.ipynb)  
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

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 04 — Transformer Architectures](../04_transformer_architectures/lecture.md) · [Next: Lecture 06 — Data Sources and Dataset Construction →](../13_data_sources_and_dataset_construction/lecture.md)

</div>
## Video companions

[Video companions: MoE, MQA, GQA and efficient attention](https://www.youtube.com/results?search_query=Mixture+of+Experts+GQA+MQA+efficient+attention+lecture)

## Navigation

[← Previous](../04_transformer_architectures/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../06_gpus_and_kernels/lecture.md)
