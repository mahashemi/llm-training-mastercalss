# Chapter 35 — RLHF Pipeline

**Part:** Part IV

## 1. RLHF is a multi-system pipeline

Classic RLHF can be represented as:

**demonstrations → SFT model → preference data → reward model → policy optimization → evaluation**

Each stage can fail independently.

This is why RLHF is operationally more complex than a simple supervised fine-tune.

## 2. Stage responsibilities

| Stage | Input | Main output | Main failure |
|---|---|---|---|
| SFT | demonstrations | seed policy | imitation gaps |
| Preference collection | prompt + responses | rankings | noisy preferences |
| Reward modeling | preference pairs | reward model | proxy mismatch |
| Policy optimization | policy + reward | updated policy | instability/over-optimization |
| Evaluation | held-out tasks | evidence | reward/eval mismatch |

## 3. Reward model risk

The reward model estimates human preference:

r_phi(x,y)

The optimization process then tries to increase r_phi.

This creates an important danger:

**optimizing the reward model is not the same as optimizing the human objective.**

A policy can discover patterns that receive high reward without being genuinely better.

## 4. Worked example — verbosity reward hacking

Suppose annotators slightly prefer detailed answers.

Reward model learns:

longer → better

Policy optimization discovers very long responses.

Observed:

| Metric | Before | After |
|---|---:|---:|
| Reward | 0.72 | 0.91 |
| Human helpfulness | 82 | 81 |
| Average tokens | 220 | 620 |
| Cost/task | 0.10 | 0.28 |

Reward increased while product value decreased.

This is classic proxy failure.

## 5. KL constraint intuition

Policy optimization often constrains the new policy relative to a reference.

A conceptual objective is:

maximize reward − beta × divergence(policy || reference)

The purpose is to prevent unrestricted drift.

The correct coefficient depends on implementation and task.

## 6. RLHF vs DPO

| Property | DPO-style preference optimization | Classic RLHF |
|---|---|---|
| Reward model | not required | required |
| Online rollouts | not central | central |
| Engineering complexity | lower | higher |
| Main data | preference pairs | preferences + rollouts |
| Main risk | preference bias | reward hacking + instability |
| Useful first test | small preference pilot | after simpler baselines |

This is a complexity comparison, not a universal performance ranking.

## 7. Evaluation must be independent

Use:

- held-out preference data;
- objective capability tasks;
- safety tests;
- cost/latency measurements;
- human audits.

Do not evaluate only with the same reward model used for optimization.

## 8. When RLHF is worth the complexity

Consider it when:

- high-quality preference signals exist;
- the target behavior is not easily expressed as supervised targets;
- iterative optimization is valuable;
- the team can operate the training loop;
- simpler preference methods are insufficient.

## Research exercise

Construct a toy reward model with an intentional proxy:

**reward favors longer responses**

Train a small policy and observe the reward/helpfulness divergence.

Then redesign the reward rubric and repeat.

## Laboratory

[dpo_and_distillation_concepts.ipynb](../../notebooks/dpo_and_distillation_concepts.ipynb)

## Reference

https://arxiv.org/abs/2203.02155
