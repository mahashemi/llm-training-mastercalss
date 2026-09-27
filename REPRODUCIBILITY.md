# Reproducibility Standard

Reproducibility is a first-class requirement of this project.

## Minimum experiment record

A substantial experiment should let another reader reconstruct:

code version + data version + model/version + tokenizer + configuration + environment + hardware + evaluation = reported result

## Required metadata

| Area | Examples |
|---|---|
| Code | Git commit, branch, or tag |
| Data | dataset name, version, split, provenance |
| Model | model identifier and checkpoint |
| Tokenizer | identifier and version |
| Hardware | accelerator type, count, memory |
| Software | Python, PyTorch, Transformers, CUDA |
| Configuration | batch size, sequence length, learning rate, scheduler, steps/epochs |
| Randomness | seed(s) and deterministic settings where relevant |
| Evaluation | datasets, metrics, decoding settings |
| Runtime | elapsed time, throughput, peak memory |
| Cost | measured or estimated cost plus assumptions |

## Reproduction tiers

### Tier 1 — Educational
Runs on free Colab or CPU and demonstrates one concept.

### Tier 2 — Experimental
Runs a meaningful model/data comparison and produces a result suitable for engineering comparison.

### Tier 3 — Research
Includes controlled baselines, ablations, detailed configuration, and evidence appropriate for a research report.

### Tier 4 — Program-scale
Documents realistic infrastructure, operations, costs, staffing, risks, and scaling assumptions.

## Data

Never publish private or restricted data merely to make an experiment reproducible. Publish provenance, preprocessing code, schema, lawful access instructions, hashes or version identifiers where appropriate, and a public substitute when possible.

## External APIs

When an experiment uses an external API, record the provider, model/API identifier, relevant date or version information, and material configuration. Never commit credentials.

## Results

Prefer raw observations plus interpretation. For comparisons, report the baseline and configuration alongside the claimed improvement.

## Failed reproductions

A failed reproduction is valuable. Explain what was attempted, where it differed from the original, what happened, and what evidence supports the proposed explanation.
