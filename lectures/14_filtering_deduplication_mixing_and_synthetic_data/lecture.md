# Lecture 14 — Filtering, Deduplication, Mixing, and Synthetic Data

**Duration:** 25 minutes

## Outcome

Learn how corpus transformations allocate the effective training budget and how to measure whether “cleaner” or “more balanced” data actually improves the target model.

## 0–4 — The raw corpus is not the training corpus

Start with:

**100B raw tokens → 60B after quality filtering → 45B after dedup → 45B sampled with a new mixture**

Ask:

“How did the data change the model's learning budget?”

Every transformation changes what the model sees.

## 4–8 — Four operations

### Filtering
Remove low-quality or unsuitable content.

### Deduplication
Reduce repeated content.

### Mixing
Choose how often source families are sampled.

### Synthetic data
Create additional examples from a model or rule system.

These have different failure modes and should be evaluated separately.

## 8–12 — Filtering trade-off

| Filter setting | Usable tokens | Noise | Target score | Risk |
|---|---:|---|---:|---|
| loose | high | high | measure | noisy learning |
| medium | medium | lower | measure | possible balance |
| aggressive | low | lowest | measure | useful data removed |

The best threshold is empirical.

## 12–16 — Deduplication

Compare:

**exact → normalized → near-duplicate**

The benefit is not “fewer tokens.” It is potentially:

- more unique information;
- less memorization;
- less contamination;
- better effective diversity.

But aggressive dedup can remove legitimate repeated content.

## 16–19 — Data mixing

For source proportions p_i, temperature sampling can use:

q_i = p_i^alpha / Σ p_j^alpha

Example:

raw = 80% / 15% / 5%

alpha = 0.5

approximately becomes:

59% / 26% / 15%

A low-resource source receives more exposure, but high-resource sources receive less.

## 19–21 — Synthetic data

Synthetic data can fill sparse regions but may also introduce correlated teacher errors.

Compare:

| Run | Human/source | Synthetic |
|---|---:|---:|
| A | 100% | 0% |
| B | 75% | 25% |
| C | 50% | 50% |

Measure quality **and failure diversity**.

## 21–23 — Worked experiment

Hold model/training constant.

Run:

A. loose filter + raw mix  
B. medium filter + raw mix  
C. medium filter + temperature mix  
D. medium filter + temperature mix + 25% synthetic

Measure:

- validation loss;
- target score;
- per-language score;
- contamination;
- duplicate rate;
- compute;
- tokens processed.

Now the learner can attribute gains to specific data interventions.

## 23–25 — Exit challenge

Complete:

> “The data intervention changed ___, which we expect to affect ___, so we will measure ___ while holding ___ fixed.”

### Laboratory

[dedup_and_data_mixing.ipynb](../../notebooks/dedup_and_data_mixing.ipynb)

### Research bridge

The key research habit is to report the actual transformed corpus, not only the raw source size.

