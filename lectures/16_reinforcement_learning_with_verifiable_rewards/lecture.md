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



## Why verifiable rewards change the problem

Ordinary language-model quality is difficult to score automatically. A response can sound convincing while being wrong.

A verifiable task gives a machine-checkable signal.

Examples include:

- exact mathematical answers;
- executable code tests;
- symbolic equivalence;
- structured constraint satisfaction.

For a sampled answer y to prompt x, a simple reward can be:

$$
R(x,y)=
\begin{cases}
1,&\text{verifier accepts }y\\
0,&\text{otherwise.}
\end{cases}
$$

The simplicity of the reward does not make the optimization simple. The model still has to discover behaviors that increase expected reward.

## A concrete loop

Think of one training iteration as:

**prompt → sample answers → verify → assign rewards → update policy → sample again**

The research question is not merely whether reward rises. Ask whether the model learned the intended behavior or learned to exploit the verifier.

## Reward hacking

Suppose a coding verifier checks only that a program passes a small visible test set.

A model may discover an answer that passes those tests without solving the underlying task.

This is a general lesson:

> **The verifier is part of the training environment.**

A weak verifier can produce a highly optimized but meaningless policy.

## Evaluation must stay independent

Keep hidden tests or independent evaluations that are not exposed to the training loop.

Compare:

- training reward;
- held-out verifier reward;
- human or external evaluation;
- failure categories.

A growing training reward with stagnant held-out performance is evidence that the optimization target may be overfitting.

## Research extension

Design two verifiers with different failure modes. Train against one and evaluate against the other. The gap measures how much the learned policy depends on the verifier itself.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 18 — Preference Optimization and Distillation](../20_preference_optimization_and_distillation/lecture.md) · [Next: Lecture 20 — Multimodality →](../17_multimodality/lecture.md)

</div>