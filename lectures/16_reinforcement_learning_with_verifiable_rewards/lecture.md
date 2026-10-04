# Lecture 16 — Reinforcement Learning with Verifiable Rewards

**Lab:** [RLVR Toy Experiment](./lab.ipynb)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

You can explain why verifiable rewards change the reinforcement-learning problem, build a simple verifier, and diagnose reward hacking.

## Start with an objective we can check

Consider a math problem with a known answer.

Instead of asking a human to score every response, create a verifier:

**response → parser/verifier → reward**

Ask:

> What can go wrong if the verifier is imperfect?

This frames RLVR as an objective-design problem.

## Outcome versus process rewards

An outcome reward scores the final answer.

A process reward scores intermediate reasoning/actions.

Discuss the trade-off:

| Signal | Advantage | Risk |
|---|---|---|
| outcome | simple, objective when verifiable | sparse |
| process | denser feedback | evaluator errors / reward gaming |

## Policy update intuition

The policy generates candidate outputs.

The training system uses rewards to change the probability of future outputs.

You should distinguish:

**policy model → sampled responses → verifier → reward → optimization**

from ordinary supervised labels.

## Break it: reward hacking

Construct a response that satisfies the heuristic but not the real objective.

Ask:

> Did optimization fail, or did our reward function fail?

The answer is often the latter.

## Engineering decision

RLVR is attractive when:

- a reliable verifier exists;
- the target behavior is hard to supervise directly;
- the cost of online/rollout training is justified.

Without a trustworthy verifier, a sophisticated RL loop can optimize the wrong thing very efficiently.

## Exit challenge

Use:

**task → verifier → reward → failure mode → protected metric**

## Research bridge

Compare the toy verifier with a real mathematical/code verifier and identify which assumptions become fragile at scale.


## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 18 — Preference Optimization and Distillation](../20_preference_optimization_and_distillation/lecture.md) · [Next: Lecture 20 — Multimodality →](../17_multimodality/lecture.md)

</div>