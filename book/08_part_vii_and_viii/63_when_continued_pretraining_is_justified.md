# Chapter 63 — When Continued Pretraining Is Justified

**Part:** Part VII

## 1. What continued pretraining changes

Supervised fine-tuning teaches behavior from labeled examples.

Continued pretraining changes the model's underlying language/domain exposure using additional unlabeled text.

A useful distinction is:

**SFT:** “When the user asks X, respond with Y.”

**Continued pretraining:** “Spend computation learning from this distribution because the base model is underexposed to it.”

Typical targets:

- a low-resource language;
- a technical domain;
- a specialist corpus;
- a regional style/domain mixture;
- large-scale terminology and syntax adaptation.

## 2. The evidence threshold is higher than SFT

Continued pretraining consumes far more tokens and compute than a small adaptation run.

Start only when:

1. a strong base-model baseline exists;
2. retrieval has been tested where knowledge is external;
3. SFT/PEFT has been tested when the issue is behavior;
4. the remaining gap appears to be representation/domain exposure;
5. a sufficiently large, high-quality unlabeled corpus exists;
6. you can evaluate retained general capability.

## 3. Symptoms that support the hypothesis

| Symptom | Possible cause | Continued PT hypothesis |
|---|---|---|
| Terminology consistently poor | domain exposure | more domain tokens help |
| Native-language grammar weak | language exposure | target-language corpus helps |
| Tokenization inefficient | representation/input | tokenizer + corpus intervention may help |
| Correct evidence still produces weak answers | learned capability gap | broader pretraining may help |
| Only a fixed output format fails | behavior | SFT/PEFT more direct |
| Current facts are wrong | knowledge freshness | RAG/tools more direct |

The diagnostic is important. Continued pretraining is not a stronger synonym for fine-tuning.

## 4. How much data?

There is no universal token threshold.

The correct question is:

**How many useful tokens can we supply, how novel are they, and what capability gap do they cover?**

A planning sweep can use:

| Corpus size | Purpose |
|---:|---|
| 100M tokens | toy/feasibility signal |
| 1B tokens | serious small-domain experiment |
| 10B tokens | meaningful domain adaptation for many research settings |
| 100B+ tokens | large-scale program territory |

These are planning scales, not laws of model improvement.

## 5. Data quality dominates raw volume

For a target domain, track:

- deduplication;
- language identification;
- document quality;
- contamination;
- source mixture;
- licensing;
- temporal distribution;
- domain distribution;
- synthetic vs human/source data.

A billion low-quality tokens can be less useful than a much smaller high-quality corpus.

## 6. Forgetting risk

Continued pretraining can improve the target domain while harming other capabilities.

Therefore construct a mixture:

**target domain/language + retained general data**

and test multiple mixture ratios.

Example:

| Run | Target tokens | General tokens | Hypothesis |
|---|---:|---:|---|
| A | 100% | 0% | maximum specialization |
| B | 75% | 25% | reduce forgetting |
| C | 50% | 50% | broader retention |

Keep total compute comparable where possible.

## 7. Learning-rate discipline

Continued pretraining starts from a pretrained model. An overly aggressive learning rate can destroy useful representations.

Treat:

- learning rate;
- warmup;
- token budget;
- batch size;
- sequence length;
- mixture;
- checkpoint frequency

as a coupled experiment.

The right value depends on the base model and corpus.

## 8. Worked example — low-resource language

Suppose:

- target language is weak on native QA;
- token fertility is high;
- source corpus contains 2B high-quality tokens;
- retrieval supplies facts correctly;
- SFT improves style but not language competence.

Hypothesis:

**the model has insufficient target-language exposure.**

Pilot:

1. freeze a base-model checkpoint;
2. train on 100M–500M target-language tokens;
3. compare language-model loss;
4. run native-language benchmark;
5. test general-language retention;
6. compare against a mixed-corpus control.

The go/no-go metric is not “loss decreased.” It is **target capability gain per unit compute with acceptable regression**.

## 9. Cost reasoning

A rough dense-model compute planning heuristic is:

FLOPs ≈ 6ND

Then:

time ≈ FLOPs / measured_effective_FLOPs_per_second

Do not confuse theoretical GPU peak with delivered training throughput.

Add:

- data processing;
- checkpointing;
- evaluation;
- retries;
- storage;
- experiment overhead.

## 10. When the intervention is justified

Continued pretraining becomes compelling when:

- the target corpus is large and high quality;
- the gap survives strong inference-time baselines;
- the desired improvement is broad rather than one narrow format;
- the team can quantify regression;
- the token budget is economically defensible.

## 11. When it is not justified

Avoid it when:

- the main problem is fresh knowledge;
- a small behavior gap is the only issue;
- the domain corpus is tiny;
- evaluation cannot detect the claimed improvement;
- the expected business/product gain is too small for the compute.

## Research exercise

Design a three-arm experiment:

**Base model**  
vs  
**Continued PT on target corpus**  
vs  
**Continued PT on target + general mixture**

Report:

- target loss;
- target benchmark;
- retained benchmark;
- compute;
- tokens/sec;
- GPU-hours;
- cost;
- checkpoint trajectory.

Then identify the smallest additional experiment that could invalidate your conclusion.

## Laboratory

[full_ft_vs_lora.ipynb](../../notebooks/full_ft_vs_lora.ipynb)

## Reference

Stanford CS336: https://cs336.stanford.edu/
