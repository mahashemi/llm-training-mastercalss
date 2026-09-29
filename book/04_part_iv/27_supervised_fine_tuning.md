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


## Deepening: SFT is a data-distribution experiment

The central quantity is not “number of examples.” It is the distribution of training signal.

### Coverage matrix

Construct a matrix over:

- task/intent;
- difficulty;
- language;
- answer length;
- format;
- ambiguity;
- safety;
- refusal/uncertainty;
- domain.

Then measure the proportion of examples in every cell.

### Controlled data experiment

Keep training steps approximately fixed and compare:

| Run | Data | Question |
|---|---|---|
| A | narrow/repeated | what does repetition teach? |
| B | broad/representative | what does coverage teach? |
| C | broad + hard cases | do rare cases improve? |

Evaluate target performance **and retained capability**.

### Critical distinction

A lower training loss is not proof that the model became more useful.

A successful SFT experiment must demonstrate:

**baseline → training → target gain → regression check → failure analysis**

### Colab lab

Use Qwen3-0.6B and an inspectable dataset. Require students to print several training examples before training and compare generations before/after training.

The lesson is intentionally small enough to run in a free-first environment while preserving the same methodology used on H100.
