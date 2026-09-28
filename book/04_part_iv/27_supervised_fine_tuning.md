# Chapter 27 — Supervised Fine-Tuning

**Part:** Part IV

## 1. SFT changes behavior through demonstrations

The training set contains:

**input x → target response y**

and optimizes the likelihood of target tokens.

The important practical principle is:

**the dataset defines the behavior you repeatedly reward.**

## 2. When SFT is appropriate

SFT is a strong candidate when:

- the desired behavior is stable;
- the output can be demonstrated;
- representative examples exist;
- the base model already has the required knowledge/capability.

It is not the first solution for:

- changing live facts;
- database state;
- current schedules;
- external actions.

Use RAG/tools for those system-level needs.

## 3. Dataset design

| Dimension | Examples |
|---|---|
| intent | factual / advisory / procedural |
| difficulty | easy / medium / hard |
| language | L1 / L2 / L3 |
| format | prose / JSON / table |
| context | none / retrieved / tool result |
| safety | ordinary / edge / refusal |
| length | short / medium / long |

Coverage matters more than raw example count.

## 4. Baseline before SFT

Record:

- model;
- prompt;
- decoding;
- target metric;
- latency;
- cost;
- failure taxonomy.

Then compare SFT against the strongest baseline.

## 5. Data quantity experiment

Use several dataset sizes while keeping quality and distribution controlled.

| Run | Examples | Target score | Regression |
|---|---:|---:|---:|
| A | 500 | measure | measure |
| B | 2k | measure | measure |
| C | 10k | measure | measure |

The key question is the marginal gain per additional example.

## 6. Training strength

Control:

- learning rate;
- epochs;
- sequence length;
- batch size;
- optimizer;
- checkpoint selection.

Too little training can underfit; too much can over-specialize or forget.

## 7. Worked example — strict response schema

Requirement:

**always output concern, urgency, question, next step**

Build varied examples including:

- missing information;
- ambiguous requests;
- edge cases;
- multiple languages;
- safety-sensitive inputs.

Measure:

**schema validity + semantic correctness + safety + language quality**

## 8. Failure analysis

### Format improves, correctness does not
The dataset may teach syntax without enough substantive supervision.

### Training score improves, production fails
The training distribution may not match real usage.

### Target improves, general capability drops
Adaptation may be too strong or too narrow.

## 9. Research exercise

Train two SFT models:

- broad/representative data mix;
- narrow/highly repeated data mix.

Hold compute approximately equal.

Compare:

- target metric;
- general metric;
- rare-case performance;
- multilingual performance;
- output length.

## Laboratory

[sft_with_a_small_open_model.ipynb](../../notebooks/sft_with_a_small_open_model.ipynb)

## Reference

https://huggingface.co/docs/trl/sft_trainer
