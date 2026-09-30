# Lecture 01 — What Is an LLM?

**Level:** starts beginner-friendly, ends at Deep Learning engineer level  
**Lab:** `./lab.ipynb`

## Learning objective

By the end of this lecture, a student should be able to explain, without hand-waving:

- what a language model predicts;
- what a token is;
- why the training target is the next token;
- what logits and probabilities mean;
- how cross-entropy becomes the training signal;
- what parameters actually learn;
- why inference differs from training;
- why an LLM is more than an autocomplete demo;
- what information is learned from data versus supplied at inference time.

## Start with a prediction

Consider:

> Given the sentence “The capital of France is ___”, what should the model output?

Then ask:

> What exactly did the model have to learn in order to produce that answer?

Do not begin with “Transformer.” Begin with prediction.

### Critical-thinking question

**Q:** Is a language model trying to store answers?

**Answer:** Not directly. Its fundamental training task is to model a probability distribution over token sequences. During autoregressive generation it repeatedly estimates a distribution for the next token conditioned on the preceding context.

That distinction becomes important later when we compare pretraining, retrieval, and fine-tuning.

## From text to tokens

A neural network does not receive “words” as ideas. It receives integer token IDs.

Example:

```
"The model learns."
       ↓
[token_17, token_892, token_41]
```

A tokenizer is therefore part of the model system, not just a preprocessing convenience.

We will later study BPE, vocabulary size, multilingual tokenization, special tokens, and tokenizer training.

## Next-token prediction

Given:

```
The cat sat on the
```

the training target can be:

```
mat
```

The model produces a vector of logits:

$z \in \mathbb{R}^{|V|}$

where `|V|` is the vocabulary size.

Softmax converts logits into probabilities:

$p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$

The training objective for the correct target token (y) is:

$\mathcal{L} = -\log p(y)$

This is the single idea we will keep returning to:

> **Make the correct next token more probable.**

## Why this simple objective becomes powerful

You should now notice something surprising.

A model trained on enough diverse text must learn statistical structure that helps it predict what comes next:

- spelling;
- morphology;
- syntax;
- semantic relationships;
- style;
- factual associations;
- code patterns;
- discourse structure.

It is not because we wrote separate rules for each phenomenon. The training objective creates pressure to represent whatever structure improves prediction.

### Important qualification

Next-token prediction alone does not guarantee truthfulness, reasoning, factual freshness, or good instruction following.

Those properties depend on data, scale, architecture, post-training, inference, and evaluation.

## Training vs inference

### Training

We know the target token.

```
context → model → logits → loss
                  ↑
               target
                  ↓
              backprop
                  ↓
              update weights
```

During training, the next token from the dataset is available at every step.

### Inference

We do not know the target.

```
context → model → probabilities → sample/select token
                                      ↓
                                   append
                                      ↓
                                  repeat
```

This is autoregressive generation.

### Critical-thinking question

**Q:** Why can training be parallelized across many token positions even though generation is sequential?

**Answer:** During training, the full target sequence is known and a causal mask prevents each position from using future targets. Many positions can therefore be evaluated in parallel. During autoregressive generation, future tokens do not exist yet, so generation proceeds step by step.

This distinction will become central when we later study GPU utilization, KV cache, and inference economics.

## Is an LLM just a probability table?

For a tiny model, almost.

For a neural language model, the probability function is represented by a very large parameterized computation:

[
$p_\theta(x_t \mid x_{<t})$
]

The parameters ($\theta$) are learned from data.

A Transformer is a particular architecture for implementing this conditional distribution efficiently and expressively. We will derive it rather than treat it as magic.

## Engineering takeaway

An LLM training project can be reduced to four questions:

| Question | Engineering interpretation |
|---|---|
| What are the tokens? | tokenizer + vocabulary |
| What probability are we modeling? | training objective |
| What parameters produce that probability? | architecture |
| What data changes those parameters? | dataset + optimizer + training loop |

Then one final question:

> **What evidence would convince you that the model actually learned something useful?**

That leads directly to evaluation.

## Exit questions

1. Why do we need a tokenizer?
2. What is a logit?
3. Why is cross-entropy a natural objective?
4. What is the difference between training and generation?
5. Why can training be parallel but generation is autoregressive?
6. Does next-token prediction guarantee factual correctness?
7. What determines what a model can know?

### Answers

1. It converts raw text into the discrete IDs consumed by the model.
2. A pre-softmax score for a vocabulary item.
3. It penalizes low probability assigned to the observed target and connects naturally to maximum-likelihood training.
4. Training uses known targets to compute loss and update weights; generation must choose each new token.
5. Causal masking allows many known training positions to be computed together; generated future tokens do not yet exist.
6. No. Prediction quality and truthfulness are related but not identical.
7. Model architecture, tokenizer, training data, optimization, scale, post-training, and inference context all matter.

## Research connection

The Transformer architecture was introduced in *Attention Is All You Need* (Vaswani et al., 2017). The paper's central architectural contribution was replacing recurrence/convolution in the proposed sequence-transduction architecture with attention mechanisms, enabling substantially greater parallelization during training.

Primary source:
https://arxiv.org/abs/1706.03762


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

This lab is part of this lecture. Do not leave the lecture to find the experiment: run the notebook, record the baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
