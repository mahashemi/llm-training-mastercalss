# Chapter 13 — Mixture of Experts

**Part:** Part I

## 1. The core idea

A Mixture-of-Experts (MoE) model contains multiple expert subnetworks, while a router selects only a subset of experts for each token.

A dense layer computes all parameters for every token.

An MoE layer approximates:

token → router → top-k experts → combine

The attraction is:

**large parameter capacity without activating every parameter for every token.**

## 2. Dense vs MoE

| Property | Dense | MoE |
|---|---|---|
| Active parameters/token | most/all | subset |
| Total parameters | roughly active size | can be much larger |
| Compute/token | predictable | routing-dependent |
| Memory | simpler | larger total weight store possible |
| Communication | conventional | expert routing can be communication-heavy |
| Main new failure | ordinary optimization | routing imbalance / expert collapse |

Neither is automatically better.

## 3. Router mathematics

Let x be a token representation and W_r the router projection.

router_logits = W_r x

Softmax gives routing probabilities:

p = softmax(router_logits)

Select top-k experts.

The output can be approximated as:

y = Σ_{i in TopK(x)} p_i E_i(x)

where E_i is expert i.

## 4. Why load balancing matters

Without balancing, many tokens can choose the same few experts.

Then:

- some experts overflow;
- others are underused;
- capacity is wasted;
- communication becomes uneven.

Monitor:

| Metric | What it detects |
|---|---|
| tokens/expert | utilization |
| routing entropy | concentration |
| dropped/overflow tokens | capacity pressure |
| expert FLOPs | actual compute |
| communication time | routing overhead |

## 5. Worked example

Suppose 8 experts exist and k=2.

Ideal balanced routing over a large token batch:

each expert receives about 25% of routed assignments.

Observed:

| Expert | Assignment share |
|---|---:|
| E1 | 41% |
| E2 | 29% |
| E3 | 7% |
| E4 | 5% |
| E5 | 5% |
| E6 | 5% |
| E7 | 4% |
| E8 | 4% |

The model has eight experts but is effectively using a small subset.

This is a systems and optimization problem.

## 6. Capacity factor intuition

If each expert can accept only a bounded number of tokens, the router may need to drop or reroute overflow tokens.

Trade-off:

**more capacity → fewer drops but more memory**

**less capacity → better resource efficiency but more overflow**

Measure overflow rather than assuming the nominal expert count equals usable capacity.

## 7. When MoE is attractive

Evaluate MoE when:

- model capacity is a central objective;
- active compute must remain constrained;
- distributed infrastructure is available;
- serving can handle larger weight storage/routing complexity.

It may be unattractive for:

- small local deployments;
- very latency-sensitive systems;
- teams without distributed-systems expertise.

## 8. Research experiment

Compare a small dense model against an MoE model under a matched active-compute budget.

Measure:

- target quality;
- active parameters/token;
- total parameters;
- tokens/sec;
- communication fraction;
- memory;
- serving complexity.

The important question is the quality/resource frontier.

## Laboratory

[attention_and_moe_lab.ipynb](../../notebooks/attention_and_moe_lab.ipynb)

## Reference

https://arxiv.org/abs/2101.03961
