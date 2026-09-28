# Chapter 24 — Tokenizer Training for a Target Language

**Part:** Part III

## 1. Tokenizer choice affects the entire model

For multilingual or low-resource models, tokenizer design affects:

- sequence length;
- training compute;
- KV-cache memory;
- context utilization;
- vocabulary allocation;
- text fidelity.

A poor tokenizer can make a language expensive to represent.

## 2. Measure fertility

A simple measure:

fertility = tokenizer_tokens / words

Also track:

tokens / characters

Compare languages under the same tokenizer.

## 3. Worked example

| Language | Tokenizer A | Tokenizer B |
|---|---:|---:|
| English | 1.2 | 1.1 |
| Language A | 1.8 | 1.4 |
| Language B | 3.1 | 2.0 |
| Language C | 4.5 | 2.8 |

Tokenizer B is substantially more compact for the lower-resource languages in this example.

The practical consequence is fewer sequence tokens for the same text.

## 4. Vocabulary-size trade-off

A larger vocabulary can:

- reduce token counts;
- increase embedding/output parameters;
- increase model memory;
- change rare-token behavior.

A smaller vocabulary can:

- improve parameter efficiency;
- increase sequence length;
- increase decode steps.

Measure the complete trade-off.

## 5. Tokenizer benchmark

For each candidate:

| Metric | Measure |
|---|---|
| fertility | tokens/word |
| char efficiency | tokens/character |
| vocabulary coverage | observed vocabulary |
| sequence expansion | tokens per document |
| multilingual balance | per-language fertility |
| training throughput | tokens/sec |
| model size effect | embedding/output parameters |

## 6. Worked selection

Suppose:

- tokenizer A gives 1.5 average fertility;
- tokenizer B gives 1.2;
- B adds 50M embedding parameters.

Now estimate:

**training compute saved by shorter sequences**

vs

**memory/model-size cost of larger vocabulary**

The decision is quantitative.

## 7. Normalization and scripts

Test:

- Unicode normalization;
- punctuation;
- whitespace;
- diacritics;
- mixed scripts;
- code switching;
- spelling variants.

A tokenizer that performs well on clean text may behave poorly on real user input.

## 8. Research exercise

Train or evaluate three tokenizers on a multilingual corpus.

Report:

**vocabulary → fertility → sequence length → embedding size → throughput**

Then estimate which tokenizer gives the best quality/resource trade-off.

## Laboratory

[tokenizer_design_and_measurement.ipynb](../../notebooks/tokenizer_design_and_measurement.ipynb)

## References

- SentencePiece: https://arxiv.org/abs/1808.06226
- Stanford CS336: https://cs336.stanford.edu/
