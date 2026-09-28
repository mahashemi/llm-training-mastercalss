# Chapter 41 — Validation Loss and Perplexity

**Part:** Part V

## 1. What validation loss tells you

For a token sequence, the language-model objective is average negative log-likelihood:

L = -(1/T) Σ log p_theta(x_t | x_<t)

Perplexity is:

PPL = exp(L)

when L is measured in natural-log units.

Lower validation loss means the model assigns higher probability, on average, to held-out tokens under the evaluation distribution.

It does not automatically mean better instruction following, factuality, tool use, safety, serving cost, or product performance.

## 2. Training loss vs validation loss

| Pattern | Likely interpretation | Next investigation |
|---|---|---|
| Train ↓, validation ↓ | learning | continue while improvement justifies compute |
| Train ↓, validation flat | overfitting or distribution mismatch | inspect data and checkpoint |
| Train ↓, validation ↑ | overfitting / instability | stop or adjust |
| Both flat | optimization/data problem | inspect LR, data, implementation |
| Loss improves but task metric does not | objective mismatch | inspect downstream task |

Loss is a diagnostic signal, not the final product metric.

## 3. Validation distribution matters

Suppose training is 70% English web, 20% multilingual, 10% code.

If Validation A is all English web and Validation B is target-language healthcare text, improvement on A may say little about B.

Maintain multiple validation slices when the program has multiple objectives.

## 4. Per-language validation

| Slice | Validation loss | PPL | Tokens |
|---|---:|---:|---:|
| English | 2.4 | 11.0 | 10M |
| Language A | 2.9 | 18.2 | 5M |
| Language B | 4.1 | 60.3 | 2M |
| Healthcare | 3.0 | 20.1 | 3M |

Do not average away the slices. Track them separately.

## 5. Loss comparability

Perplexity values depend on:

- tokenizer;
- normalization;
- tokenization granularity;
- context treatment;
- causal objective;
- evaluation corpus.

Always report:

**model + tokenizer + dataset version + objective + evaluation code**

## 6. Checkpoint selection

| Checkpoint | Val loss | Target task | Safety | General |
|---|---:|---:|---:|---:|
| A | 2.9 | 72 | 91 | 84 |
| B | 2.7 | 75 | 90 | 84 |
| C | 2.6 | 75 | 86 | 80 |
| D | 2.5 | 74 | 85 | 78 |

The lowest validation loss is not automatically the release checkpoint.

Selection should follow the predeclared program objective and protected metrics.

## 7. Compute-aware interpretation

The useful quantity is often quality gain per additional training compute.

| Run | Compute | Val loss | Target score |
|---|---:|---:|---:|
| A | 1× | 2.90 | 72 |
| B | 2× | 2.72 | 75 |
| C | 4× | 2.63 | 76 |
| D | 8× | 2.58 | 76.2 |

The marginal target gain collapses after C. That should influence whether the next compute tranche goes to data, architecture, post-training, or deployment.

## 8. Research exercise

Create:

- train-loss curve;
- validation-loss curve;
- per-language slices;
- one downstream task metric.

Find a checkpoint where validation loss improves but the task metric regresses. Explain why the measurements can disagree.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Reference

https://cs336.stanford.edu/
