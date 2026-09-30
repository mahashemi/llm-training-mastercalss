# Lecture 24 — From Experiment to Fundable Model

**Lab:** [capstone_model_program.ipynb](`./lab.ipynb`)

## Outcome

Turn an experiment into a fundable, reviewable technical case without hiding uncertainty.

## The proposal is an evidence chain

Start with:

“We should train a 30B model.”

Consider how to rewrite it.

Better:

“Baseline A misses target benchmark B by C points. RAG improves factuality but not language quality. A continued-pretraining pilot improves B by D points at E compute. We therefore propose a scale experiment to estimate the quality-vs-compute curve.”

Every claim should point to evidence or an explicit assumption.

## Proposal anatomy

| Section | Core question |
|---|---|
| Mission | Why does this matter? |
| Users | Who uses it? |
| Gap | What cannot current systems do? |
| Baseline | What was already tested? |
| Evidence | What experiments support the claim? |
| Technical plan | What exactly will be trained/built? |
| Evaluation | How will success be measured? |
| Resources | What compute/data/people are needed? |
| Budget | What is one-time vs recurring? |
| Risk | What can invalidate the plan? |
| Gates | When is more money released? |
| Deliverables | What artifacts will exist? |

## The reviewer objection table

Learn to answer:

| Reviewer asks | Required evidence |
|---|---|
| Why not API? | quality + TCO baseline |
| Why not RAG? | retrieval experiment + residual gap |
| Why not SFT/PEFT? | adaptation comparison |
| Why continued PT? | domain/language evidence |
| Why this architecture? | controlled architecture experiment |
| Why this model size? | scaling study |
| Why these GPUs? | measured throughput |
| Why this budget? | equations + assumptions |
| What if it fails? | gate + fallback |
| Can it be reproduced? | artifact plan |

This table makes the proposal falsifiable.

## Budget from the workload

For training:

FLOPs ≈ 6ND

For time:

$t \approx \frac{\mathrm{total\ FLOPs}}{\mathrm{measured\ effective\ throughput}}$

For compute cost:

$\mathrm{cost} \approx \mathrm{accelerator\ hours}\times\mathrm{blended\ rate}$

Then add:

- data;
- storage;
- evaluation;
- retries;
- people;
- security/governance;
- serving;
- contingency.

Never make the GPU line equal the project budget.

## Milestone-funded development

Example:

| Milestone | Release condition |
|---|---|
| Discovery | baseline gap reproduced |
| Data | rights + quality pass |
| Pilot | target gain demonstrated |
| Scaling | trend measurable |
| Product | task/SLO gate |
| Full program | integrated evidence |

This converts a large request into a sequence of testable claims.

## Make the proposal research-grade

Preserve:

- code;
- model/config;
- tokenizer;
- dataset version;
- hardware;
- software versions;
- evaluation;
- results;
- limitations.

The proposal should be capable of becoming a paper, a reproduction package, and a future maintenance record.

## Worked proposal

Claim:

“A target language is underserved.”

Evidence:

- native benchmark gap;
- tokenizer inefficiency;
- RAG factuality gain without language gain;
- SFT format gain without grammar gain;
- continued-pretraining pilot improves native score.

Next request:

a controlled small-scale scaling experiment.

Not yet:

the final large cluster.

## Exit challenge

Write the first page of a proposal with exactly:

**problem → baseline → evidence → proposed experiment → resources → gate → fallback**

### Critical-thinking question

What makes a proposal more credible: a larger requested budget or a stronger chain of measured evidence?

The proposal should make the evidence chain explicit so the reviewer can inspect the assumptions and challenge them.

### References

OLMo 2: https://allenai.org/olmo2  
Stanford CS336: https://cs336.stanford.edu/  
Chinchilla: https://arxiv.org/abs/2203.15556


## Lab contract

Complete the linked laboratory before treating the lecture as mastered. Record a baseline, one intervention, at least one failure, and the next experiment. See the lecture's lab contract.

## Deepening — write the proposal from the experiment backwards

Take one measured experiment and turn it into a proposal.

### Evidence chain

**problem → baseline → intervention → measurement → failure → remaining gap → next experiment → resources**

Every proposal paragraph should map to one element of this chain or be clearly labeled as an assumption.

### Reviewer challenge matrix

Students must answer:

| Question | Evidence |
|---|---|
| Why not API? | workload baseline + TCO |
| Why not RAG? | retrieval experiment + residual gap |
| Why not PEFT? | adaptation comparison |
| Why this model size? | scaling/resource evidence |
| Why these GPUs? | measured throughput |
| What if it fails? | kill criterion + fallback |
| How reproducible? | artifact/version plan |

### Final practical exercise

Using the course's Qwen3-0.6B → H100 ladder, write a one-page scale proposal that names:

**current evidence → proposed model → hardware → training method → evaluation → budget assumptions → gate → fallback**.



## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
