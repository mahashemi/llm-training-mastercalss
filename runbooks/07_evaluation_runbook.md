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
