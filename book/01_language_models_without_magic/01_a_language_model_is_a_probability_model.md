# Chapter 1 — A Language Model Is a Probability Model

## The first principle

Before discussing Transformers, Llama, GPT, instruction tuning, or RLHF, define the object we are trying to build.

A language model assigns probabilities to token sequences. In an autoregressive model, the sequence probability can be factorized as:

[
p_	heta(x_1,ldots,x_T)
=
prod_{t=1}^{T}
p_	heta(x_t mid x_{<t})
]

The model is therefore repeatedly answering one question:

> Given everything I have seen so far, which token is most probable next?

This sounds simple. It is simple.

The engineering difficulty comes from building a parameterized function that can estimate those conditional distributions well across enormous numbers of contexts.

## A tiny example

Suppose the vocabulary contains only:

```
{cat, dog, sat, ran, the, end}
```

After seeing:

```
the cat
```

a model might produce:

| Token | Logit | Probability |
|---|---:|---:|
| sat | 4.0 | 0.88 |
| ran | 2.0 | 0.12 |
| dog | -1.0 | 0.00 |
| the | -2.0 | 0.00 |
| end | -3.0 | 0.00 |

The exact values are not important. The structure is.

The model emits one score per vocabulary item. These scores are **logits**. Softmax converts them into a probability distribution.

[
p_i = operatorname{softmax}(z)_i
]

## Why use logits?

Because neural networks naturally produce unconstrained real-valued outputs.

We do not need to force the final layer to produce valid probabilities directly. Softmax performs the normalization.

Also, adding the same constant to every logit does not change the softmax distribution. This is one reason the logit representation is convenient.

## Cross-entropy

Suppose the observed next token is `sat`.

The loss for this one example is:

[
-log p(	ext{sat})
]

If the model assigns high probability to `sat`, the loss is small.

If it assigns tiny probability to `sat`, the loss is large.

Across a dataset, training minimizes the average negative log-likelihood.

## What is actually being learned?

A common beginner misconception is:

> The model is explicitly learning grammar rules, a database of facts, and a reasoning algorithm.

Sometimes its internal representations behave as though useful abstractions have been learned, but the training procedure does not directly label these abstractions.

The optimization process changes parameters so that predictions become better.

What internal representations emerge is an empirical question.

## Training versus inference

During training:

```
tokens
  ↓
model
  ↓
logits
  ↓
loss against known next token
  ↓
gradients
  ↓
parameter update
```

During generation:

```
prompt
  ↓
model
  ↓
next-token distribution
  ↓
choose token
  ↓
append token
  ↓
repeat
```

Training has a target. Generation does not.

## Why this matters for engineering

This tiny distinction predicts major system behavior.

Training is dominated by:

- throughput;
- accelerator utilization;
- memory;
- communication;
- optimizer state;
- checkpointing;
- data pipeline efficiency.

Generation is dominated by:

- latency;
- memory bandwidth;
- KV cache;
- batching;
- sequence length;
- tokens per second;
- concurrency.

Later chapters will derive these consequences experimentally.

## A useful mental model

For this course, use:

[
oxed{
	ext{LLM}
=
	ext{Tokenizer}
+
	ext{Parameterized Network}
+
	ext{Training Data}
+
	ext{Optimization}
}
]

That is a simplification, but an extremely useful one.

It reminds us that changing the model can mean changing more than the network weights.

## Questions to think about

**Q1.** If a model predicts the next token extremely well, must it understand the world?

**Answer:** No. Predictive performance and human interpretations such as understanding are not logically identical. Empirical evaluation is required.

**Q2.** If we already have a perfect tokenizer and architecture, can poor data still produce a poor model?

**Answer:** Yes. The data distribution, quality, duplication, contamination, domain coverage, and sampling mixture strongly affect what the optimizer can learn.

**Q3.** If a fact changes tomorrow, does retraining always make sense?

**Answer:** No. This is one of the most important questions in the course. Retrieval, tools, or other external knowledge mechanisms may be more appropriate for information that changes frequently.

## Exercise

Before opening the notebook, write down what you expect to happen if:

1. the model has 10 possible next tokens but the correct token gets probability 0.9;
2. the correct token gets probability 0.1;
3. the same token appears many times in the training set;
4. the validation set contains examples that are near-duplicates of the training set.

Then run the experiment and compare your predictions.

## Primary references

Vaswani et al. (2017), *Attention Is All You Need*:
https://arxiv.org/abs/1706.03762

Karpathy, *Let's build GPT from scratch*:
https://www.youtube.com/watch?v=kCc8FmEb1nY
