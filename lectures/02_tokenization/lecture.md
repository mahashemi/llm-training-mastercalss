# Lecture 02 — Tokenization: The First Hidden Model Decision

**Lab:** [Tokenizer Design and Measurement](./lab.ipynb)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

By the end, you can build a simple BPE intuition, measure tokenizer behavior on real text, and explain why tokenization changes model compute, context utilization, and multilingual performance.

## Start with the surprising question

Inspect:

- "internationalization"
- "internationalization" split into subwords
- the same concept in a morphologically richer language.

Ask:

> If two sentences contain the same amount of meaning, why might one require twice as many tokens?

The answer is not “because that language is worse.” Tokenization is an encoding choice learned from a corpus.

## From characters to subwords

Walk through:

**characters → candidate pairs → frequent merges → vocabulary**

Explain BPE using a tiny corpus. You should manually perform two merges.

Then distinguish:

| Unit | Strength | Failure |
|---|---|---|
| character | robust, small vocabulary | long sequences |
| word | short sequences | huge/OOV vocabulary |
| subword | compromise | uneven fertility |

Define **fertility** as average tokenizer-produced token count for a chosen unit of text.

## Formal resource consequence

For a corpus with C characters and fertility f:

$\mathrm{tokens} \approx C \times f$

If tokenizer A gives 1.0M tokens and B gives 1.4M for the same corpus, B creates roughly 40% more token positions.

That can affect:

- context length;
- attention work;
- activation memory;
- training-token budget;
- inference latency;
- KV-cache growth.

You should not leave this lecture thinking vocabulary design is cosmetic.

## Laboratory

Open the tokenizer notebook.

Before running it, predict:

1. which language will have highest fertility;
2. which tokenizer will produce longer sequences;
3. whether vocabulary size alone predicts fertility.

Measure:

| Metric | Result |
|---|---|
| tokens | measure |
| tokens/character | measure |
| mean sequence length | measure |
| p95 sequence length | measure |
| vocabulary utilization | measure |
| per-language fertility | measure |

## Break it

Use a corpus distribution that is mostly English while evaluating a low-resource target language.

Ask:

> Can a tokenizer optimized for average corpus compression be bad for a target language?

Then test it.

Failure category: **distribution mismatch**.

## Engineering decision

Tokenizer choice should be evaluated against:

**language coverage × sequence expansion × vocabulary budget × training/inference compute**

For multilingual projects, report fertility by language rather than one global average.

## Exit challenge

Complete:

> “Tokenizer A creates ___% more/fewer positions than B on our target corpus, which changes ___; therefore our next experiment is ___.”

## Research bridge

Compare your measured result with a published tokenizer claim and identify what is measured, what is a benchmark-specific result, and what is an engineering inference.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

This lab is part of this lecture. Do not leave the lecture to find the experiment: run the notebook, record the baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.

---

<div align="center">

[← Previous lecture: Lecture 01 — What Is an LLM](../01_what_is_an_llm/lecture.md) · [Next lecture: Lecture 03 — PyTorch and Resource Accounting →](../03_pytorch_and_resource_accounting/lecture.md)

</div>
