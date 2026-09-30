# Lecture 16 — Reinforcement Learning with Verifiable Rewards

**Lab:** [RLVR Toy Experiment](`./lab.ipynb`)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

Students can explain why verifiable rewards change the reinforcement-learning problem, build a simple verifier, and diagnose reward hacking.

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

## Laboratory

Run a toy task with a deterministic verifier.

Measure:

- reward;
- accuracy;
- invalid outputs;
- verifier rejection rate.

Then compare two reward functions:

1. exact correctness;
2. a flawed heuristic that rewards formatting.

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

Write:

**task → verifier → reward → failure mode → protected metric**

## Research bridge

Compare the toy verifier with a real mathematical/code verifier and identify which assumptions become fragile at scale.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
