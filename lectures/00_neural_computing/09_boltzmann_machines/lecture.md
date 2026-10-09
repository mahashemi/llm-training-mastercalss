# Course 1 · Chapter 9 — Boltzmann Machines, RBMs, and Deep Belief Networks

**Course:** Deep Learning & Neural Computing Foundations  
**Primary laboratory:** [Open the executable laboratory](./lab.ipynb)

## Why this chapter exists

Before today's dominant neural architectures, researchers explored probabilistic energy-based models that learn which configurations of variables are plausible.

An RBM assigns an energy to visible/hidden configurations and uses alternating conditional sampling. Contrastive divergence makes this practical by approximating the learning signal.

The lab makes the sampling process tangible and shows why approximation and compute matter.

## Learning objective

By the end of this unit, the learner should be able to explain the mechanism mathematically, implement a minimal version without a high-level abstraction, use a modern library implementation, and design a controlled experiment showing when the method helps or fails.



## Teaching walkthrough

Begin with an energy function rather than a neural-network layer. An energy-based model assigns lower energy to configurations it considers more compatible.

For a restricted Boltzmann machine (RBM), let $v$ be the visible units (the observed data), $h$ the hidden units (latent features), $a$ and $b$ their biases, and $W$ the connection weights. One common energy function is

$$
E(v,h)=-a^\top v-b^\top h-v^\top Wh.
$$

Think of energy as a compatibility score: configurations the model prefers have lower energy. Their probability is proportional to $\exp(-E(v,h))$, after normalizing across possible configurations.

The restriction—no visible-visible or hidden-hidden edges—makes conditional sampling tractable. For binary hidden units,

$$
P(h_j=1\mid v)=\sigma\!\left(b_j+\sum_i W_{ij}v_i\right).
$$

This says: given the visible data, calculate a weighted input for hidden unit $j$, add its bias, and use the sigmoid to turn that score into the probability that the unit is on. Visible units have an analogous conditional distribution.

Explain contrastive divergence: start from observed data, sample hidden states, reconstruct visible states, sample again, and use the difference between data and reconstruction statistics as an approximate learning signal.

Deep belief networks stack RBM-like representations.

Real connection: these models are historically important because they illustrate latent-variable learning, energy-based modeling, and pre-deep-learning representation learning.

Failure experiment: compare reconstruction statistics after different numbers of Gibbs steps and observe why approximate sampling can bias learning.

## Build the intuition before the notation

Imagine a landscape where every possible configuration of variables sits at a different height.

The model wants familiar configurations to sit in **valleys** and implausible configurations to sit at **higher energy**.

Learning then changes the landscape so that real data becomes easier for the model to generate.

That is the intuition behind an energy-based model.

### Why sampling appears

For a discriminative classifier, we can often compute a prediction directly.

For an energy-based generative model, we care about a distribution over many possible configurations.

That means we need a way to explore the landscape.

Gibbs sampling is one such exploration process.

### Why contrastive divergence is clever—and imperfect

Starting the chain at real data gives us a useful reference point.

Rather than waiting for the Markov chain to mix perfectly, contrastive divergence takes only a short journey and uses the resulting sample to approximate the negative phase.

This makes training much cheaper.

It also means the learning rule is approximate.

That is a recurring machine-learning engineering trade-off:

**more accurate computation ↔ more compute ↔ potentially better statistical approximation.**

### Research question

The most educational experiment is not “which RBM gets the lowest reconstruction error?”

It is:

> “At a fixed wall-clock budget, how much does additional negative-phase sampling improve the learned model?”

That question connects statistical approximation directly to systems cost.


## Work a tiny energy calculation by hand

For a restricted Boltzmann machine, one common energy function is

$$
E(v,h)=-a^\top v-b^\top h-v^\top Wh,
$$

where $v$ is the visible vector, $h$ the hidden vector, $a,b$ are biases, and $W$ connects visible to hidden units. Lower energy means the model regards that joint configuration as more compatible.

For a one-visible, one-hidden toy model, set both biases to zero and $W=1$. Then:

- $E(1,1)=-1$, because the active visible and hidden units agree through the positive weight;
- $E(1,0)=0$, because the interaction term is zero.

The unnormalized probability is proportional to $e^{-E(v,h)}$, so the first configuration receives weight $e^1$, while the second receives weight $e^0=1$. This illustrates how the interaction changes relative preference. It is not a full probability calculation over every possible configuration.

### Why contrastive divergence has two phases

The positive phase uses real data to increase compatibility between observed patterns and their likely hidden causes. The negative phase uses model-generated samples to reduce the model's tendency to assign excessive probability to those samples. Contrastive divergence approximates this second phase with a short Gibbs chain; it is computationally convenient but biased.

A falling reconstruction error is useful diagnostic evidence, not proof that the learned distribution is good. Also inspect generated samples, diversity, and stability across random seeds.

**Check yourself:** if the positive and negative phases were identical, what would the expected parameter update be? Explain why the model needs to compare data-driven and model-driven statistics.


## Enumerate a one-visible, one-hidden RBM completely

Let $v,h\in\{0,1\}$, set both biases to zero, and let $W=1$. The energy is $E(v,h)=-vh$. We can list every possible joint configuration—there are only four:

| Visible $v$ | Hidden $h$ | Energy $E(v,h)$ | Unnormalized weight $e^{-E(v,h)}$ |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | -1 | $e\approx2.718$ |

The partition function is the sum of these weights:

$$
Z=1+1+1+e\approx5.718.
$$

So the joint probability of $(v=1,h=1)$ is $e/Z\approx0.475$; each of the other three configurations has probability $1/Z\approx0.175$. The positive weight makes the jointly active configuration more probable, but it does not make it certain.

The conditional probability gives the sampling rule. With zero hidden bias,

$$
P(h=1\mid v)=\sigma(Wv).
$$

If $v=0$, the probability is $\sigma(0)=0.5$. If $v=1$, it is $\sigma(1)\approx0.731$. To perform a Gibbs transition, sample $h$ from $P(h\mid v)$, then sample $v$ from $P(v\mid h)$, and repeat. Each transition alternates between the two conditionals.

### The partition function: why exact probabilities become expensive

To turn unnormalized weights into probabilities, the model needs the partition function

$
Z=\sum_{v\in\{0,1\}^{n_v}}\sum_{h\in\{0,1\}^{n_h}}e^{-E(v,h)}.
$

It sums over every possible visible/hidden configuration. With $n_v$ binary visible units and $n_h$ binary hidden units, there are $2^{n_v+n_h}$ joint configurations. The four-row toy example is easy to enumerate; a realistic RBM may have millions of configurations, making exact summation impractical. Sampling approximates the expectations needed for learning without explicitly enumerating the whole state space.

The visible conditional mirrors the hidden conditional:

$
P(v_i=1\mid h)=\sigma\left(a_i+\sum_j W_{ij}h_j\right).
$

A Gibbs step samples hidden units given the current visible vector, then samples visible units given the new hidden vector. Repeating those two steps creates a Markov chain whose samples are used to approximate model statistics.

## Contrastive divergence as a difference of statistics

For this tiny model, the positive-phase statistic for the weight is the data expectation $\mathbb E_{\text{data}}[vh]$; the negative-phase statistic is the corresponding expectation under reconstructed/model samples. A schematic update is

$$
\Delta W\propto
\underbrace{\mathbb E_{\text{data}}[vh]}_{\text{positive phase}}
-
\underbrace{\mathbb E_{\text{model}}[vh]}_{\text{negative phase}}.
$$

CD-$k$ starts its negative-phase chain at observed examples and performs $k$ Gibbs transitions. CD-1 is cheap but uses a short, generally biased approximation; increasing $k$ spends more compute on the chain but does not guarantee a monotonic improvement in every finite training run.

## How RBM layer-wise pretraining builds a DBN

A classic greedy layer-wise procedure is:

1. Train the first RBM on the input vectors; use its hidden activations as the representation for the next layer.
2. Train a second RBM on those first-layer representations.
3. Repeat to build additional layers.
4. Use the stacked representation in the downstream model; in classic deep-belief-network training, the top two layers form an undirected associative memory while lower connections are treated as directed generative connections.

This pretraining procedure is historically important, but it is not the same as simply stacking several RBMs and declaring the whole stack one RBM. Layer-wise training changes the distribution presented to each subsequent layer, and the exact DBN generative interpretation depends on the chosen architecture and training procedure.

## Core concepts

This unit covers **energy-based learning, RBM, contrastive divergence, DBN intuition**. Do not memorize the architecture. Derive the computation, identify its inductive bias, and ask what evidence would distinguish its claimed advantage from a larger parameter count or better optimization.

## Required practical workflow

1. Load the real dataset in the lab and record its provenance, split, schema, license/access basis, and revision/date.
2. Build the smallest defensible baseline.
3. Implement the central mechanism once from first principles.
4. Run the framework implementation.
5. Keep the primary budget fixed while changing one factor.
6. Measure quality, compute, memory, and failure modes.
7. Repeat with seeds when feasible and report uncertainty.
8. Inspect qualitative examples—not only aggregate metrics.
9. Write a short interpretation that separates observation from explanation.
10. Propose the next falsifiable experiment.

## Research exercise

The lab must end with a research question. A good question has a measurable independent variable, a defined outcome, a baseline, and a reason the result would matter. Examples include:

- Does the mechanism improve accuracy at the same parameter count?
- Does it improve sample efficiency at the same training budget?
- Does it improve robustness under distribution shift?
- Does it reduce inference memory or latency?
- Which failure mode becomes more or less common?

## Paper-ready deliverable

Every learner produces a **mini research package**: hypothesis, related-work note, dataset card, method description, experiment matrix, baseline, results table, one figure, error analysis, limitations, reproducibility block, and next-work proposal. These artifacts accumulate toward the final publication capstone.

## Exit questions

1. What problem does the method solve?
2. What inductive bias does it introduce?
3. Which tensor operations implement it?
4. What is the simplest credible baseline?
5. Which metric and split answer the research question?
6. What failure would falsify your hypothesis?

### Answers

1. An RBM models a joint distribution over visible data and hidden features using an energy function.
2. Lower energy gives greater unnormalized weight $e^{-E}$; the partition function normalizes those weights into probabilities.
3. The restricted graph has no visible-visible or hidden-hidden edges, making the conditional distributions easy to sample.
4. The positive phase measures data-driven statistics; the negative phase measures statistics from model samples. If they match exactly, their difference—and the corresponding schematic update—is zero.
5. Contrastive divergence approximates the negative phase with a short Gibbs chain initialized from data, which saves compute but introduces bias.
6. A lower reconstruction error alone does not prove distribution quality; inspect generated samples, diversity, held-out likelihood proxies where appropriate, and sensitivity to the number of Gibbs steps.

## Visual intuition

![An RBM learns by contrasting distributions](../../../visuals/course1/09-boltzmann-machine.svg)

— energy and hidden structure

An RBM assigns an energy to a visible/hidden configuration. Training adjusts weights and biases so observed data configurations become more compatible with the model than configurations produced by its own sampling process.

```mermaid
flowchart TB
    V["Visible units v: observed pixels"] <--> H["Hidden units h: latent features"]
    V --- E["Energy E(v,h)"]
    H --- E
    E --> P["Lower energy → higher relative probability"]
    P --> S["Sample hidden units given visible units"]
    S --> R["Sample reconstructed visible units"]
    R --> C["Contrastive divergence: data statistics minus model statistics"]
    C --> U["Update weights and biases"]
    U -. "repeat" .-> V
```

The restricted structure matters: there are no visible-visible or hidden-hidden connections, which makes the conditional distributions easier to sample. Contrastive divergence is an approximation; it is not exact maximum-likelihood training.

## Laboratory — run the experiment end to end

**[Open the executable laboratory](./lab.ipynb)**

This notebook is part of the chapter, not optional homework. Follow the same scientific loop used in real ML work:

**predict → establish a baseline → run → change one factor → measure → inspect failures → produce the results table → conclude → propose the next experiment.**

The notebook uses a real dataset or environment, records quantitative results, and ends with an answer key and a research extension.

## Video companions

**Recommended starting point:** [Boltzmann machines and energy-based learning](https://www.youtube.com/watch?v=_bqa_I5hNAo)

For the training approximation used in RBMs, [explore contrastive divergence and Gibbs sampling](https://www.youtube.com/results?search_query=restricted+Boltzmann+machine+contrastive+divergence+Gibbs+sampling).

## Navigation

[← Previous](../08_sequence_architectures_and_forecasting/lecture.md) · [Course 1 home](../README.md) · [Next →](../10_attention_transformers_and_llms/lecture.md)
