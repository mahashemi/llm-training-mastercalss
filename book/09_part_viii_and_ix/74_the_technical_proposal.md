# Chapter 74 — The Technical Proposal

**Part:** Part IX

## 1. A proposal is a chain of claims

A serious technical proposal should make every major claim traceable to:

- measured evidence;
- a primary source;
- an explicit assumption;
- or a defined experiment that will resolve the uncertainty.

Avoid prose such as:

“We need a large model because our country needs AI independence.”

Replace it with measurable claims:

“Existing baseline X misses target-language task Y by Z points on a protected native benchmark. Retrieval improves factuality but not language quality. A continued-pretraining pilot produces A improvement per B compute. The next stage therefore tests C model/data scale under a defined budget.”

## 2. Proposal architecture

| Section | What the reviewer should learn |
|---|---|
| Mission | Why the program exists |
| Users | Who benefits |
| Capability gap | What current systems cannot do |
| Baseline | What has already been tested |
| Evidence | What experiments support the claim |
| Technical plan | Data, tokenizer, architecture, training, post-training |
| Evaluation | How success/failure is measured |
| Resource plan | GPUs, storage, people, time |
| Cost | One-time + recurring TCO |
| Governance | Data/security/release controls |
| Risks | What can fail and what happens |
| Milestones | What evidence is required before more spend |
| Deliverables | Model, data artifacts, code, evaluations |
| Publication/open science | What can be reproduced and released |

## 3. One-page decision summary

Every proposal should contain a first-page table:

| Item | Value |
|---|---|
| Problem | precise capability gap |
| Current baseline | model + setup |
| Target | measurable threshold |
| Proposed intervention | exact method |
| Evidence so far | experiment references |
| New spend | compute/data/staff |
| Duration | calendar estimate |
| Main risk | highest-impact uncertainty |
| Gate | evidence required for next stage |
| Fallback | lower-cost alternative |

A reviewer should understand the proposal without reading every appendix.

## 4. Resource calculation

Training compute:

FLOPs ≈ 6ND

Time:

time ≈ FLOPs / measured_effective_FLOPs_per_second

Compute cost:

cost ≈ accelerator_hours × blended_rate

Then add:

- data preparation;
- evaluation;
- retries;
- storage;
- staffing;
- security/governance;
- serving;
- contingency.

Never write “X GPUs for six months” without exposing the assumptions that generated it.

## 5. Milestone design

Good milestones are evidence gates.

| Phase | Deliverable | Gate |
|---|---|---|
| Discovery | baseline report | gap is real |
| Data | dataset v1 | rights + quality |
| Pilot | training/eval report | hypothesis supported |
| Scale test | scaling curve | extrapolation defensible |
| Product pilot | workflow/SLO report | system works |
| Program | full model/release | integrated evidence |

## 6. Budget structure

A useful budget separates:

**people + compute + storage + data + evaluation + security/governance + serving + contingency**

Do not hide all of these inside “GPU budget.”

## 7. Worked proposal example

### Claim

A target language is underserved.

### Evidence

- native benchmark below program target;
- high tokenizer fertility;
- retrieval improves facts but not language quality;
- SFT improves format but not grammar;
- continued-pretraining pilot improves native-language score.

### Next experiment

Train several small model/data configurations to estimate the quality-vs-compute curve.

### Requested resources

Only enough resources for that experiment.

### Gate

Scale only if:

- target gain clears threshold;
- retained capability remains acceptable;
- throughput meets plan;
- data rights are resolved.

This is stronger than requesting the final cluster first.

## 8. Research and publication package

For each major claim preserve:

- code;
- configs;
- data version;
- tokenizer;
- model checkpoint identifier;
- hardware;
- software versions;
- random seeds where applicable;
- evaluation code;
- results;
- limitations.

This turns a funding proposal into a future research artifact.

## 9. Reviewer objection table

Anticipate:

| Objection | Evidence to prepare |
|---|---|
| Why not API? | baseline + TCO |
| Why not RAG? | retrieval experiment + residual gap |
| Why not fine-tune? | SFT/PEFT experiment |
| Why continue pretraining? | domain/language evidence |
| Why this model size? | scaling experiment |
| Why this cluster? | measured throughput |
| Why this budget? | equations + assumptions |
| What if it fails? | predeclared gate + fallback |
| Can results be reproduced? | artifact/reproduction plan |

This table is one of the highest-value parts of a technical proposal.

## Research exercise

Write a six-page proposal for a model program.

Append:

1. baseline report;
2. data card;
3. resource calculator;
4. evaluation plan;
5. risk register;
6. milestone gate table.

## Laboratory

[capstone_model_program.ipynb](../../notebooks/capstone_model_program.ipynb)

## Reference

https://allenai.org/olmo2
