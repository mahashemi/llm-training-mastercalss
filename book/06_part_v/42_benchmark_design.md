# Chapter 42 — Benchmark Design

**Part:** Part V

## 1. A benchmark is a measurement instrument

A benchmark measures:

**population + task + dataset + interface + scoring protocol**

Change the protocol and the number may no longer be comparable.

## 2. Start from the requirement

Weak:

“Create a benchmark for our chatbot.”

Strong:

“The system must correctly answer 90% of policy questions, cite supporting evidence, and avoid unsupported answers when evidence is insufficient.”

Now the benchmark has measurable dimensions:

| Requirement | Metric |
|---|---|
| Correct answer | task-specific accuracy |
| Evidence support | citation / groundedness |
| Appropriate abstention | false-answer vs abstention rate |
| Latency | p50 / p95 |
| Economics | cost per successful task |

## 3. Coverage matrix

| Dimension | Example slices |
|---|---|
| Difficulty | easy / medium / hard |
| Language | L1 / L2 / L3 |
| Domain | general / specialist |
| Length | short / medium / long |
| Intent | factual / procedural / ambiguous |
| Safety | ordinary / edge / high-risk |
| Freshness | current / outdated / conflicting |
| Failure type | retrieval / reasoning / format / refusal |

A single average can hide the cases that matter most.

## 4. Sample-size thinking

Benchmark size should be chosen from:

- expected effect size;
- variability;
- number of slices;
- annotation cost;
- required confidence.

A 5,000-item benchmark can be less informative than a carefully designed 500-item benchmark if the smaller set has better coverage and labels.

## 5. Contamination resistance

Separate:

- training;
- development;
- public validation;
- private test;
- challenge set.

Useful controls:

- temporal holdouts;
- source-based splits;
- lexical overlap checks;
- semantic similarity scans;
- protected test storage.

## 6. Interface versioning

Store:

- model/checkpoint;
- tokenizer;
- system prompt;
- user template;
- tool definitions;
- decoding settings;
- retrieval configuration;
- benchmark version.

Otherwise an evaluation result is hard to reproduce.

## 7. Example scorecard

| Model | Overall | L1 | L2 | Safety | Long-context | Cost/task |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 78 | 82 | 61 | 91 | 70 | 0.10 |
| Candidate | 81 | 84 | 58 | 89 | 76 | 0.13 |

The aggregate improved while L2 and safety declined.

Release evaluation should therefore inspect slices rather than only the overall number.

## 8. Metric selection

| Task | Possible metric |
|---|---|
| Classification | accuracy / F1 |
| Extraction | precision / recall / F1 |
| Ranking | MRR / NDCG |
| Open-ended generation | rubric/human evaluation |
| Grounded QA | correctness + evidence support |
| Structured output | schema validity + semantic correctness |
| Agent | end-to-end success |
| Serving | throughput + p95 latency |

## 9. Benchmark versioning

Record:

- added/removed items;
- label changes;
- rubric changes;
- prompt changes;
- evaluator changes.

A score from benchmark-v2 should not be compared casually with benchmark-v1.

## Research exercise

Design a 200-item benchmark for one application with:

- four difficulty levels;
- three input slices;
- two major failure classes;
- one safety slice.

Specify expected items per slice and explain whether that is enough to detect the desired improvement.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Reference

https://cs336.stanford.edu/
