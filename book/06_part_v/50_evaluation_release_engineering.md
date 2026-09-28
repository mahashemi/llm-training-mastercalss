# Chapter 50 — Evaluation Release Engineering

**Part:** Part V

## 1. Evaluation is a release artifact

A model release should produce an immutable evaluation package containing:

- model/checkpoint identifier;
- tokenizer;
- dataset versions;
- prompts;
- tool definitions;
- retrieval configuration;
- decoding parameters;
- evaluator versions;
- raw predictions;
- metrics;
- failure samples;
- hardware/software metadata.

Without this, “model v2 scores 84” is difficult to reproduce.

## 2. Release scorecard

| Dimension | Gate | Result | Status |
|---|---:|---:|---|
| Target task | ≥90% | 92% | pass |
| Safety-critical slice | 0 critical failures | 0 | pass |
| L2 language | ≥75% | 73% | fail |
| p95 latency | ≤2s | 1.7s | pass |
| Cost/task | ≤0.20 | 0.24 | fail |

The release outcome is a set of gates, not one aggregate score.

## 3. Regression gates

For every new model compare the current release with the candidate on:

- primary capability;
- critical safety;
- multilingual slices;
- long-context;
- robustness;
- latency;
- cost.

A candidate is not automatically an improvement because one metric rises.

## 4. Reproducibility manifest

Create a machine-readable manifest with:

model_id  
tokenizer_id  
dataset_version  
prompt_version  
retrieval_version  
tool_schema_version  
evaluation_version  
hardware  
software  
seed  
run_id

The exact schema can evolve, but identifiers must be stable enough to trace results.

## 5. Raw predictions matter

Store predictions when policy permits.

Aggregate metrics can hide:

- systematic errors;
- duplicate examples;
- evaluator bugs;
- language regressions;
- benchmark artifacts.

Raw examples enable independent failure analysis.

## 6. CI-style evaluation

A mature pipeline can run:

code change → unit tests → smoke evaluation → full evaluation → regression gate → report

For expensive suites:

- small fast suite on code changes;
- larger suite on candidate checkpoints;
- full suite before release.

## 7. Human audit loop

Sample outputs for human review, especially:

- new failure clusters;
- low-confidence cases;
- largest metric shifts;
- safety cases;
- low-resource languages.

## 8. Worked release example

Candidate model:

- overall +2%;
- target domain +5%;
- safety −1%;
- L3 language −4%;
- p95 latency +30%.

The overall gain is not enough information.

The release discussion needs the program requirements:

- Is L3 critical?
- Is the safety change acceptable?
- Is the latency SLO still met?
- Does the target-domain gain justify the operational cost?

## Research exercise

Build a release checklist with:

- 10 automatic gates;
- 3 human-audit gates;
- artifact manifest;
- regression report;
- rollback rule.

Simulate a candidate that improves overall score but fails two slice gates.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## Reference

https://cs336.stanford.edu/
