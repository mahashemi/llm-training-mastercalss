# Evaluation Runbook

## Objective

Create evidence that a model improved for its intended use.

## Before training

Freeze:
- tasks;
- datasets;
- prompts;
- metrics;
- judge rubric;
- sampling/decoding settings;
- safety criteria.

## Evaluation layers

### Intrinsic
Validation loss/perplexity.

### Capability
Task benchmarks and domain tests.

### Behavioral
Instruction following, format adherence, tool use, grounded response.

### Safety
Risk-specific adversarial and normal-use tests.

### Human
Representative pairwise or rubric-based review.

## Analysis

Always report:
- aggregate;
- per-task/per-language buckets;
- representative failures;
- uncertainty where meaningful;
- baseline;
- resource changes.

## Contamination

Check whether evaluation material, benchmark answers, or close duplicates can exist in training data.

## Release

Archive raw predictions where lawful, metrics, scripts, evaluator versions, prompts, and a clear limitation statement.


## Evaluation protocol

### Freeze the protocol

Record:

- dataset revision;
- prompt/template;
- model revision;
- decoding;
- evaluator version;
- metric implementation;
- random seed where relevant.

### Build slices

At minimum consider:

**task × difficulty × language × length × failure class**

Do not let one huge easy slice dominate the aggregate.

### Human calibration

Before using a model judge at scale:

1. create a human-labeled calibration set;
2. compare judge decisions with human decisions;
3. inspect systematic disagreements;
4. revise rubric;
5. freeze the judge prompt/version.

### Regression

Every candidate is evaluated against:

- target suite;
- protected/general suite;
- safety suite;
- robustness suite.

### Release gate

A release requires explicit pass/fail rules, including critical blockers. Record failures, not only averages.
