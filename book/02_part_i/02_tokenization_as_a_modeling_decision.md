# Chapter 2 — Tokenization as a Modeling Decision

**Part:** Part I

## 1. Tokenization is the interface between text and the model

A language model does not directly receive characters or words. It receives token IDs.

text → tokenizer → token IDs → embeddings → Transformer

Therefore tokenization changes:

- sequence length;
- vocabulary size;
- embedding/output parameters;
- training and serving compute;
- multilingual efficiency;
- the model's ability to represent rare forms.

## 2. Tokenizer trade-off

| Choice | Vocabulary | Sequence length | Main cost |
|---|---:|---:|---|
| character-level | tiny | huge | long sequences |
| word-level | huge | short | unknown/rare words |
| subword | medium | medium | tokenizer complexity |
| byte-level | broad coverage | variable | possible expansion |

Modern LLMs commonly use subword or byte-derived schemes because they balance vocabulary size and sequence efficiency.

## 3. Vocabulary-size economics

Increasing vocabulary can reduce token count.

But it also increases:

- embedding parameters;
- output projection size when untied;
- memory;
- optimizer state during training.

For vocabulary V and model width d:

embedding parameters ≈ Vd

Example with d=4096:

| Vocab | Embedding parameters |
|---:|---:|
| 32k | ~131M |
| 64k | ~262M |
| 128k | ~524M |

Vocabulary choice is therefore a model-size decision.

## 4. Fertility

Define:

fertility = token_count / word_count

Example:

| Language | Tokens/word |
|---|---:|
| English | 1.2 |
| Language A | 1.7 |
| Language B | 3.4 |

If the same semantic content is represented with 3× more tokens, the language consumes more context and compute.

## 5. Tokenizer benchmark

Measure:

- fertility;
- tokens/character;
- sequence length distribution;
- vocabulary utilization;
- handling of rare words;
- script coverage;
- code-switching;
- malformed Unicode.

Do not test only clean English text.

## 6. Worked example

Suppose a corpus contains 1B words.

Tokenizer A:

1.5 tokens/word → 1.5B tokens

Tokenizer B:

1.2 tokens/word → 1.2B tokens

B reduces the sequence-token budget by:

300M tokens

That can reduce training work substantially.

But if B requires a much larger vocabulary, include that parameter/memory cost in the comparison.

## 7. Tokenizer failure modes

### Over-fragmentation
Rare language forms become many tokens.

### Under-segmentation
Very large vocabulary consumes excessive parameters.

### Normalization errors
Distinct characters/forms collapse unexpectedly.

### Mixed-script failure
Real user input produces inefficient tokenization.

## 8. Research exercise

Benchmark three candidate tokenizers on:

- English;
- Persian;
- Hindi;
- Arabic;
- one technical domain.

Report:

**vocab size → fertility → sequence expansion → parameter cost → throughput**

Then identify which language drives the tokenizer decision.

## Laboratory

[tokenizer_design_and_measurement.ipynb](../../notebooks/tokenizer_design_and_measurement.ipynb)

## References

- SentencePiece: https://arxiv.org/abs/1808.06226
- Stanford CS336: https://cs336.stanford.edu/
