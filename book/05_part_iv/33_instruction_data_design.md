# Chapter 33 — Instruction Data Design

**Part:** Part IV

## 1. SFT learns from the empirical task distribution

Supervised fine-tuning learns from pairs:

(x, y_target)

The training distribution determines which behaviors receive repeated gradient pressure.

Therefore:

**dataset design is behavior design.**

## 2. Coverage matrix

Before collecting examples, define the task space.

| Dimension | Example values |
|---|---|
| Intent | factual / procedural / advisory / unclear |
| Difficulty | easy / medium / hard |
| Language | L1 / L2 / L3 |
| Output | prose / JSON / table |
| Context | none / retrieved / tool result |
| Safety | ordinary / edge / refusal |
| Input length | short / medium / long |

Then allocate examples across the matrix.

## 3. Quantity vs diversity

Suppose dataset A has 20k near-identical examples.

Dataset B has 5k examples spanning:

- many intents;
- multiple languages;
- edge cases;
- different input lengths;
- real failure modes.

B can provide stronger behavioral coverage despite being smaller.

Track:

- unique task patterns;
- vocabulary/domain coverage;
- language balance;
- failure coverage;
- duplication.

## 4. Response quality

Every target response should be judged on the actual objective:

**correctness + completeness + format + safety + grounding + style**

A model faithfully learns bad targets too.

## 5. Negative examples

Negative examples can be useful when they teach a clear distinction.

Example:

**input:** “What is the current policy?”  
**bad:** invents policy  
**good:** retrieves/cites source or states that evidence is missing

Use them to expose failure boundaries rather than to fill the corpus with random bad answers.

## 6. Data mixture experiment

Compare:

| Dataset | Core task | Edge cases | Safety | Multilingual |
|---|---:|---:|---:|---:|
| A | 90% | 5% | 5% | low |
| B | 70% | 15% | 10% | 5% |
| C | 60% | 15% | 10% | 15% |

Evaluate target quality and retained capabilities.

The proportions are illustrative; the correct mixture depends on deployment.

## 7. Instruction format

Store a canonical format:

system → user → assistant

Record:

- role;
- turn ordering;
- tool calls if used;
- structured schemas;
- stop tokens/template.

Training and inference formats must be compatible.

## 8. Leakage and contamination

Never tune the SFT dataset on the final test set.

Maintain:

- train;
- development;
- validation;
- protected test.

Also inspect near-duplicates across splits.

## 9. Worked example — structured healthcare assistant

Requirement:

For every message produce:

1. concern;
2. urgency;
3. clarifying question;
4. next step.

Build examples across:

- clear symptoms;
- ambiguous symptoms;
- missing information;
- urgent edge cases;
- multilingual prompts.

Then evaluate:

- schema validity;
- field completeness;
- semantic correctness;
- safety;
- language quality.

## Research exercise

Create a 5,000-example instruction dataset.

Produce a coverage report:

**intent × language × difficulty × safety × output format**

Then run a smaller-model SFT experiment using two mixtures and quantify which slice improves.

## Laboratory

[sft_with_a_small_open_model.ipynb](../../notebooks/sft_with_a_small_open_model.ipynb)

## Reference

https://huggingface.co/docs/trl/sft_trainer
