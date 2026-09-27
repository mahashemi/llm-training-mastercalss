# Lecture 01 — Video companions

## Primary companion: Andrej Karpathy

**Let's build GPT: from scratch, in code, spelled out.**

https://www.youtube.com/watch?v=kCc8FmEb1nY

Why we use it:
- extremely practical bridge from language modeling to implementation;
- shows tokenization, data loading, a bigram baseline, self-attention, Transformer blocks, training, generation, and the pretraining/fine-tuning distinction.

### Suggested segments for Lecture 01

| Time | Use |
|---|---|
| 00:00–07:52 | Motivation and language-model setup |
| 07:52–14:27 | Data exploration and tokenization |
| 22:11–34:53 | Bigram model, loss, and generation |
| 34:53–42:13 | Training loop and transition to self-attention |
| 01:42:39–01:54:32 | Architecture variants, pretraining, fine-tuning, RLHF |

**Teaching instruction:** Do not watch the whole video before doing the first notebook. Watch the first 35 minutes, run our notebook, then return to the later architecture sections.

The video description itself recommends this implementation-first route and provides a Colab path.

## Visual companion: 3Blue1Brown

**Attention in transformers, step-by-step**

https://www.youtube.com/watch?v=eMlx5fFNoYc

Use this later in Part I when the course reaches attention. It provides a strong visual explanation of self-attention, masking, values, multiple heads, and cross-attention.

Recommended segment:
- 0:00–18:21 for the core attention mechanism and parameter intuition.

## Academic anchor

Vaswani et al., *Attention Is All You Need*:
https://arxiv.org/abs/1706.03762

Read the abstract and architecture diagram now. Do not attempt to read the full paper yet. We will return to it after the student has built the prerequisites.
