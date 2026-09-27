# LLM Trainer Glossary

## A
**Adapter** — A small trainable module added to a mostly frozen pretrained model.

**Activation** — Intermediate tensor produced during a forward pass.

**Autoregressive model** — A model that predicts a sequence one element/token at a time conditioned on earlier elements.

## B
**BPE** — Byte Pair Encoding, a tokenization family that iteratively merges frequent symbol pairs/substrings.

**Batch size** — Number of training examples processed before an optimizer update, adjusted for accumulation/distribution.

## C
**Causal mask** — Mask preventing a token position from attending to future positions.

**Checkpoint** — Saved training state used for recovery, analysis, or release.

**Context window** — Maximum sequence context supported by a model/configuration.

**Cross-entropy** — Negative log-likelihood loss for categorical prediction.

## D
**DPO** — Direct Preference Optimization, a preference-learning objective that can train directly from chosen/rejected responses relative to a reference model.

**Data parallelism** — Replicate a model across devices and divide batches/data across workers.

## F
**Fine-tuning** — Adapting a pretrained model to a new data/objective distribution.

**Full fine-tuning** — Updating all or most model parameters.

**FLOPs** — Floating-point operations; used for compute accounting.

## G
**GQA** — Grouped-Query Attention; multiple query heads share fewer key/value heads.

**Gradient accumulation** — Accumulate gradients over multiple micro-batches before an optimizer step.

## H
**Head** — One attention subspace in multi-head attention.

## I
**Instruction tuning / SFT** — Supervised training on instruction/response examples.

## K
**KV cache** — Cached attention keys and values used during autoregressive generation.

## L
**LoRA** — Low-Rank Adaptation; learn a low-rank update while freezing the base parameters.

**Logit** — Unnormalized model score before the output probability transformation.

## M
**MoE** — Mixture of Experts; route different tokens through a subset of specialized feed-forward experts.

**Mixed precision** — Use lower-precision arithmetic selectively to improve performance and reduce memory.

## P
**PEFT** — Parameter-Efficient Fine-Tuning.

**Perplexity** — Exponential of average negative log-likelihood for token-level language modeling.

**Prefill** — Initial processing of the prompt before generation.

**Pretraining** — Large-scale learning of a general language-model distribution.

## Q
**QLoRA** — Quantized base-model weights plus LoRA adaptation.

## R
**RAG** — Retrieval-Augmented Generation; retrieve external context at inference time.

**RLHF** — Reinforcement Learning from Human Feedback.

**RLVR** — Reinforcement Learning with Verifiable Rewards.

## S
**SFT** — Supervised Fine-Tuning.

**Scaling law** — An empirical relationship describing how loss or capability changes with model/data/compute scale.

## T
**Tensor parallelism** — Split model tensor operations across devices.

**Throughput** — Work completed per unit time, such as training tokens/sec or generated tokens/sec.

**Tokenizer fertility** — A measure such as tokens per word/byte used to compare tokenization efficiency.

## V
**Validation set** — Held-out data used during development to monitor/generalize training choices.

## W
**Weight decay** — Regularization mechanism often applied in optimizers such as AdamW.

## One-page mental model

```
DATA
  ↓
TOKENIZER
  ↓
MODEL
  ↓
LOSS
  ↓
GRADIENT
  ↓
OPTIMIZER
  ↓
WEIGHTS
  ↓
EVALUATION
  ↓
DEPLOYMENT
```

Then ask:

> Which part is actually limiting us?
