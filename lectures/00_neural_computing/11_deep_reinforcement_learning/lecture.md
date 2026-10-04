# Course 1 · Chapter 11 — Deep Reinforcement Learning

**Course:** Deep Learning & Neural Computing Foundations  
**Primary laboratory:** [Open the executable laboratory](./lab.ipynb)

## 1. The problem

Supervised learning provides a target for each example. Reinforcement learning provides consequences of actions.

At time $t$:

- state: $s_t$;
- action: $a_t$;
- reward: $r_t$;
- next state: $s_{t+1}$.

The agent maximizes discounted return:

$$
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}.
$$

The central difficulty is **credit assignment through delayed consequences**.

## 2. Value functions

The action-value function is

$$
Q^\pi(s,a)
=
\mathbb E_\pi
\left[
\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
\mid s_t=s,a_t=a
\right].
$$

The optimal Bellman equation is

$$
Q^*(s,a)
=
\mathbb E
\left[
r+\gamma\max_{a'}Q^*(s',a')
\right].
$$

Q-learning therefore updates toward

$$
y=r+\gamma(1-d)\max_{a'}Q_{\theta^-}(s',a'),
$$

with loss

$$
L(\theta)
=
\mathbb E
\left[
\left(y-Q_\theta(s,a)\right)^2
\right].
$$

## 3. Why DQN needs stabilizers

A neural network approximates $Q_\theta(s,a)$.

Two mechanisms are particularly important:

**Experience replay.** Store transitions and sample them later. This reduces the correlation between consecutive updates and reuses experience.

**Target network.** Keep a slowly updated copy $Q_{\theta^-}$ for the bootstrap target. Otherwise the model changes both its prediction and its target simultaneously.

The failure loop is:

**prediction changes → target changes → gradient changes → prediction changes again.**

This can make apparently reasonable gradient updates unstable.

## 4. Worked CartPole example

CartPole exposes four continuous state variables: position, velocity, pole angle, and angular velocity.

The agent chooses left or right.

A reward may arrive many steps after the action that helped preserve balance. The value function therefore has to connect immediate decisions to delayed outcomes.

## 5. Engineering evaluation

A high training return is not enough.

For each condition measure:

| Evidence | Why it matters |
|---|---|
| Mean evaluation return | Typical performance |
| Standard deviation | Stochastic reliability |
| Learning curve | Sample efficiency |
| Time to threshold | Training efficiency |
| Failure episodes | Safety/robustness |
| Runtime | Engineering cost |

## 6. Laboratory

**[Open the executable laboratory](./lab.ipynb).**

Run the full DQN, remove replay, and remove the target network separately. Evaluate each condition on 20 fresh episodes with exploration disabled. The notebook produces the comparison table and an answer key.

## 7. Research question

A falsifiable study is:

> At equal environment interactions, do replay and target stabilization increase the probability of reaching a predefined return threshold?

Predefine the threshold, seeds, evaluation episodes, and stopping rule.

## Mastery questions

1. Why is delayed reward difficult?
2. What does $Q(s,a)$ represent?
3. Why is a target network useful?
4. Why is replay useful?
5. Why is one high-return episode weak evidence?

### Answers

1. The useful action may need credit for rewards observed many steps later.
2. Expected future return after taking action $a$ in state $s$ under a policy.
3. It reduces the rate at which the bootstrap target moves.
4. It reduces temporal correlation and improves sample reuse.
5. RL is stochastic; one trajectory can be lucky.

[← Previous](../10_attention_transformers_and_llms/lecture.md) · [Course 1 home](../README.md) · [Next →](../12_research_capstone/lecture.md)
