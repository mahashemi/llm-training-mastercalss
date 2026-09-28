# Chapter 65 — National-Language Strategy

**Part:** Part VIII

## 1. Start with a language inventory

A national-language program should begin with measurement, not architecture.

For each target language or variety, record:

| Dimension | Measure |
|---|---|
| Speakers/use | population and actual digital usage |
| Script | script(s), orthographic variants |
| Digital corpus | source types + token count |
| Quality | human/source quality estimate |
| Domains | education, government, healthcare, commerce, literature |
| Temporal coverage | recent vs historical |
| Licensing | usable, restricted, unknown |
| Tokenizer efficiency | fertility / sequence expansion |
| Existing model quality | native-language benchmark |
| Safety coverage | language-specific safety set |

This produces a resource map.

## 2. Why token allocation matters

A multilingual model does not automatically allocate learning proportionally to population or strategic importance.

Suppose the corpus contains:

- 70% English;
- 20% Language A;
- 8% Language B;
- 2% Language C.

A raw mixture gives Language C far less exposure.

Possible strategies:

**raw sampling**,  
**temperature sampling**,  
**minimum floors**,  
**domain-conditioned sampling**,  
**curriculum schedules**.

The choice should be evaluated rather than justified rhetorically.

## 3. Tokenizer efficiency is part of the strategy

For each language calculate:

fertility = tokens / word

and also:

tokens / character

Compare candidate tokenizers.

Example:

| Language | Tokenizer A | Tokenizer B |
|---|---:|---:|
| English | 1.2 | 1.1 |
| Language A | 1.8 | 1.4 |
| Language B | 3.1 | 2.0 |
| Language C | 4.5 | 2.8 |

A high fertility language needs more tokens to express the same text, which affects:

- training compute;
- context utilization;
- KV-cache memory;
- throughput;
- dataset size;
- user-facing context limits.

## 4. Data strategy

For each language build a source pyramid:

**high-quality curated sources**  
→ **licensed web/corpus sources**  
→ **public documents**  
→ **community contributions**  
→ **synthetic data**

Track each source independently.

Synthetic content should never silently replace source content. Its provenance and expected error characteristics differ.

## 5. Evaluation must be native

Do not evaluate only by translating an English benchmark.

Native evaluation should include:

- reading comprehension;
- instruction following;
- summarization;
- question answering;
- domain tasks;
- safety;
- cultural/linguistic appropriateness;
- morphology and spelling;
- code-switching;
- dialect/variety coverage.

Report a vector:

(language × task × domain × safety)

not just one multilingual average.

## 6. Strategic choices

| Goal | Candidate strategy |
|---|---|
| Current facts | RAG/live data |
| Better instruction following | SFT/PEFT |
| Better language exposure | continued PT |
| Tiny data, stable niche | PEFT + careful data |
| Broad foundation capability | larger pretraining |
| Multiple languages with uneven data | mixed sampling + language floors |

## 7. Worked example

Suppose Language B has:

- 10B usable tokens;
- 2.0 fertility relative to English;
- poor native QA;
- strong source governance.

Run:

1. tokenizer benchmark;
2. baseline model;
3. RAG baseline;
4. SFT baseline;
5. continued-pretraining pilot;
6. mixture ablation.

A result such as:

- RAG: factuality improves;
- SFT: format improves;
- continued PT: language quality improves

provides a causal map of interventions.

## 8. Avoiding language collapse

Monitor:

- per-language validation loss;
- per-language benchmark;
- generation quality;
- sampling exposure;
- code-switching behavior;
- low-resource regression.

Do not assume the aggregate metric is safe.

## 9. Governance

A national-language model requires explicit ownership of:

- corpus rights;
- sensitive data;
- regional/community consent where relevant;
- source removal;
- dataset versioning;
- model release policy;
- benchmark confidentiality.

This is part of technical design, not only administrative work.

## Research exercise

Pick three languages with different corpus sizes.

Build a sampling policy with:

- minimum exposure;
- maximum exposure;
- domain balance;
- evaluation quotas.

Then estimate how your policy changes token allocation and expected compute.

## Laboratory

[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
- OLMo 2: https://allenai.org/olmo2
