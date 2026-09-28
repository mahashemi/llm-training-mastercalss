# Chapter 20 — Data Mixing and Sampling

**Part:** Part III

## 1. Sampling is how the training budget is allocated

The corpus may contain billions of tokens, but the model sees a sampled stream.

Therefore:

**sampling policy = implicit allocation of training compute**

If Language A receives 50% of tokens and Language B 1%, the model has received very different learning budgets.

## 2. Temperature sampling

If raw source proportions are p_i, a common family is:

q_i = p_i^alpha / Σ_j p_j^alpha

For 0 < alpha < 1, the distribution is flattened.

For alpha > 1, it is sharpened.

## 3. Worked example

Suppose raw proportions are:

| Source | Raw p |
|---|---:|
| English | 0.80 |
| Language A | 0.15 |
| Language B | 0.05 |

With alpha = 0.5:

sqrt proportions are approximately:

0.894, 0.387, 0.224

Normalize:

| Source | Approx. sampled q |
|---|---:|
| English | 59% |
| Language A | 26% |
| Language B | 15% |

A small language receives substantially more exposure than its raw corpus share.

The cost is that high-resource data is sampled less often.

## 4. Oversampling is not free

If a source contains 100M unique usable tokens and you sample it for 300M training tokens, you have effectively replayed the source three times.

This can:

- improve exposure;
- increase memorization;
- reduce diversity;
- overfit the source.

Track **unique tokens vs sampled tokens**.

## 5. Mixture design matrix

| Strategy | Benefit | Risk |
|---|---|---|
| Raw proportions | faithful corpus distribution | low-resource starvation |
| Temperature | raises low-resource exposure | less high-resource exposure |
| Floors | guarantees minimum exposure | hand-tuned |
| Caps | prevents dominance | may discard useful data |
| Curriculum | changes exposure over training | more complexity |

## 6. Data quality × sampling

A tiny high-quality source may deserve more sampling than a huge noisy source.

Therefore optimize:

**useful learning signal per sampled token**

not merely corpus size.

## 7. Worked multilingual example

Suppose:

- L1 = 800B raw tokens;
- L2 = 100B;
- L3 = 20B.

Training budget = 200B tokens.

Compare:

**Raw:** 174B / 22B / 4B

**Temperature/floored mix:** 130B / 45B / 25B

Now ask:

- Did L3 improve?
- Did L1 degrade?
- Did duplicate exposure increase?
- Did compute per quality gain improve?

## 8. Research exercise

Design three mixtures:

1. raw;
2. temperature;
3. floor + cap.

Run a small-model experiment.

Report:

- sampled tokens per source;
- validation loss;
- per-language scores;
- unique-source coverage;
- compute.

Then choose the next experiment based on the observed bottleneck.

## Laboratory

[dedup_and_data_mixing.ipynb](../../notebooks/dedup_and_data_mixing.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
- Chinchilla: https://arxiv.org/abs/2203.15556
