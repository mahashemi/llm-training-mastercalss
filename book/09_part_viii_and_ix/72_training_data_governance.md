# Chapter 72 — Training Data Governance

**Part:** Part VIII

## 1. Data governance is part of the model

A training corpus is a technical artifact.

For every source, preserve:

- source identifier;
- acquisition date;
- provenance;
- license/permission status;
- transformation history;
- language;
- domain;
- sensitivity classification;
- dataset version.

A model checkpoint without a dataset version is difficult to reproduce.

## 2. Provenance chain

The minimum chain is:

**source → raw artifact → transformed artifact → filtered artifact → deduplicated shard → training mix → checkpoint**

Every transformation should be versioned.

## 3. Governance matrix

| Data class | Example | Required control |
|---|---|---|
| Public, permissive | openly licensed corpus | license record |
| Restricted | subscription data | explicit permitted-use decision |
| Sensitive | personal/health information | minimization + access controls |
| Proprietary | internal documents | owner approval + scope |
| Community-contributed | expert data | contributor terms + review |
| Synthetic | generated examples | synthetic provenance |

Do not infer “publicly accessible” means “training permitted.”

## 4. Dataset versioning

A training experiment should record:

**dataset ID + version + shard manifest + preprocessing version + sampling mix**

For example:

dataset = MIX-v3  
sources = A,B,C,D  
dedup = MinHash-v2  
quality_filter = classifier-v5  
sampling = 70/15/10/5

The exact values are project-specific.

## 5. Deletion and correction

Ask:

**If a source must be removed, can the team determine which dataset versions and model runs contained it?**

This is why lineage matters.

A simple lineage graph:

source → dataset v1 → run 001 → checkpoint A  
source → dataset v2 → run 002 → checkpoint B

Without this graph, incident response becomes guesswork.

## 6. Sensitive data minimization

Collect only what is needed.

Separate:

- data necessary for training;
- data necessary for evaluation;
- operational logs;
- debugging traces.

Do not store all raw prompts indefinitely merely because they are useful for future analysis.

## 7. Evaluation set governance

Protect important test sets from training contamination.

Separate:

- development;
- public benchmark;
- private validation;
- held-out research set.

The strongest evaluation set should not quietly become training data.

## 8. Audit checklist

Before a major run:

| Question | Evidence |
|---|---|
| What is in the corpus? | dataset card |
| Why can we use it? | rights record |
| What was removed? | filter report |
| What was deduplicated? | dedup report |
| What sensitive data remains? | risk assessment |
| What model saw it? | lineage |
| Can we reproduce it? | manifest + code |

## 9. Worked incident

Suppose a source must be removed after a governance review.

A mature system can:

1. locate the source ID;
2. identify dataset versions containing it;
3. identify model runs trained on those versions;
4. mark affected checkpoints;
5. decide whether retraining or release restriction is required.

An immature system has only one giant unlabeled corpus and cannot determine impact.

## Research exercise

Design a versioned data lineage schema for a 10B-token multilingual corpus.

Include:

**source → rights → transformations → dataset version → training run → checkpoint**

Then simulate removal of one source and trace the affected artifacts.

## Laboratory

[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
- OLMo 2: https://allenai.org/olmo2
