# Chapter 64 — When Training From Scratch Is Justified

**Part:** Part VII

## 1. From-scratch training is a program, not a larger fine-tune

Training a foundation model from scratch means owning or coordinating:

**data → tokenizer → architecture → optimizer → distributed system → pretraining → evaluation → post-training → serving → release**

The decision therefore belongs at program level.

A from-scratch model should not be proposed merely because:

- a current API is expensive;
- a benchmark is disappointing;
- a team wants “its own model”;
- fine-tuning is inconvenient.

## 2. The strategic questions

A from-scratch program becomes plausible only when several of these are true:

| Question | Evidence required |
|---|---|
| Is there a real capability not served by existing models? | benchmark + user evidence |
| Is the gap caused by representation/data exposure? | controlled experiments |
| Does ownership of weights/data matter? | explicit governance requirement |
| Is the target language poorly served? | native-language evaluation |
| Is there enough quality training data? | corpus inventory |
| Is there enough compute? | measured resource plan |
| Is there enough engineering talent? | staffing plan |
| Is the model useful for years? | lifecycle/mission case |
| Can the organization evaluate and operate it? | eval + serving plan |

A weak answer to several columns means the program should remain at the pilot stage.

## 3. Alternatives that must be tested first

Before requesting foundation-model compute, compare:

| Intervention | What it tests |
|---|---|
| Best available model/API | capability ceiling |
| RAG | knowledge gap |
| Tools | action gap |
| SFT/PEFT | stable behavior gap |
| Continued PT | domain/language exposure gap |
| Distillation | cost/latency gap |
| New pretraining | foundation-model ownership/capability |

This creates an evidence ladder.

## 4. Scale economics

For dense-model pretraining:

FLOPs ≈ 6ND

where N is parameter count and D is training tokens.

Example planning scenarios:

| Model | Tokens | First-order FLOPs |
|---:|---:|---:|
| 1B | 100B | 6e20 |
| 7B | 100B | 4.2e21 |
| 7B | 1T | 4.2e22 |
| 30B | 1T | 1.8e23 |

These values are planning approximations. They do not include optimizer specifics, communication overhead, wasted work, evaluation, or failed runs.

## 5. Compute is not the only scarce resource

A foundation-model budget must account for:

- training accelerators;
- networking/interconnect;
- storage;
- checkpoint bandwidth;
- data processing;
- engineering;
- evaluation;
- reliability;
- security;
- legal/data governance;
- serving;
- maintenance.

A team can have enough FLOPs and still fail because it cannot process the data, recover from failures, or evaluate the model.

## 6. Tokenizer ownership

For low-resource and multilingual programs, measure:

- tokens per character/word;
- fertility across languages;
- vocabulary utilization;
- sequence expansion;
- memory effect;
- throughput effect.

A tokenizer that expands the target language by 2× can increase downstream sequence length, affecting context and compute.

The correct experiment is to compare candidate tokenizers on representative corpora before committing to a foundation model.

## 7. Open weights versus full openness

These are different.

| Level | Artifacts |
|---|---|
| API-only | service access |
| Open weights | model checkpoint |
| Partially open | weights + some data/code |
| Fully open research artifact | weights + data details/access + training code + evaluations + recipes |

Ai2's OLMo program is an important reference because it explicitly emphasizes open training data, code, checkpoints, evaluations, and recipes rather than only final weights. https://allenai.org/olmo2

## 8. Worked example — national language program

Suppose a country wants a model optimized for several languages.

Initial evidence:

- existing models have poor native-language evaluation;
- tokenizer fertility is high;
- high-quality national corpus exists;
- RAG improves factuality but not language quality;
- SFT improves instruction following but not grammar;
- continued pretraining shows a measurable language gain.

That evidence strengthens the representation hypothesis.

Next stage:

**1B–7B pilot model → controlled tokenizer/data experiments → scaling law study → architecture decision → larger pretraining**

This is far more defensible than jumping directly to a very large model.

## 9. Kill criteria

Define these before spending heavily.

Examples:

- target-language gain below threshold after agreed token budget;
- retained capability falls below threshold;
- delivered throughput is below economic requirement;
- data rights remain unresolved;
- evaluation cannot demonstrate progress;
- serving cost exceeds mission constraint.

Kill criteria are not pessimism. They protect the project from sunk-cost escalation.

## 10. Program gate

A serious gate requires:

**baseline → pilot evidence → scaling evidence → budget → staffing → governance → release plan**

Only then should the team commit to a long pretraining campaign.

## Research exercise

Write a from-scratch business/mission case with:

- one capability that existing models cannot satisfy;
- evidence from at least three controlled experiments;
- corpus inventory;
- tokenizer study;
- model-size/token scenarios;
- compute and storage plan;
- team;
- evaluation;
- risks;
- kill criteria.

Do not use “we want independence” as the only argument.

## Laboratory

[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
- OLMo 2: https://allenai.org/olmo2
- Chinchilla: https://arxiv.org/abs/2203.15556

## Deepening: evidence before scale

Use an explicit escalation gate:

| Gate | Required evidence |
|---|---|
| 1 | best existing-model baseline |
| 2 | RAG/tool baseline where applicable |
| 3 | SFT/PEFT experiment |
| 4 | continued-pretraining pilot when representation is suspected |
| 5 | tokenizer/data study |
| 6 | scaling/resource study |
| 7 | distributed throughput and recovery test |
| 8 | full program proposal |

A proposal should identify what evidence would cause the team to stop.

### Student exercise

Given a proposed 30B foundation model, identify:

- capability gap;
- existing-model baseline;
- smallest experiment isolating the gap;
- resource estimate;
- success criterion;
- kill criterion.

The lesson is not “never train from scratch.”

It is:

> **Training from scratch should be the conclusion of an evidence chain, not the starting assumption.**
