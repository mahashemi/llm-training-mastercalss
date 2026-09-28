# Chapter 21 — Synthetic Data

**Part:** Part III

## 1. Synthetic data creates supervision, not guaranteed truth

A generator can turn a small source set into many examples.

But the generated data may inherit:

- factual errors;
- stylistic artifacts;
- repeated patterns;
- teacher bias;
- safety failures.

Therefore synthetic data should be treated as a **data-generation pipeline** with quality gates.

## 2. Synthetic-data lifecycle

**seed/source → generation → validation → filtering → deduplication → human audit → training → evaluation**

Do not jump directly from generation to training.

## 3. When synthetic data is useful

| Need | Potential value |
|---|---|
| sparse task examples | expand coverage |
| rare edge cases | generate targeted scenarios |
| format supervision | create consistent schema examples |
| multilingual coverage | fill controlled gaps |
| reasoning traces | provide intermediate supervision where appropriate |

## 4. Main risks

| Risk | Symptom | Test |
|---|---|---|
| teacher error | same wrong fact repeats | human/source check |
| mode collapse | outputs look too similar | diversity metrics |
| style transfer | student imitates teacher quirks | cross-teacher comparison |
| contamination | benchmark-like examples appear | overlap scan |
| synthetic bias | real-user performance falls | human/production slice |

## 5. Mixture decisions

Never ask only:

“Does synthetic data help?”

Ask:

**At what synthetic fraction does it help?**

| Run | Source/human | Synthetic |
|---|---:|---:|
| A | 100% | 0% |
| B | 75% | 25% |
| C | 50% | 50% |
| D | 25% | 75% |

Measure target quality and failure diversity.

## 6. Worked example

Suppose target score:

- 0% synthetic = 76;
- 25% = 80;
- 50% = 81;
- 75% = 78.

The result suggests diminishing returns and possible synthetic over-weighting.

Now inspect whether the 75% run contains:

- more repeated language;
- teacher artifacts;
- fewer real edge cases.

## 7. Source-grounded generation

For factual tasks, prefer generation grounded in an approved source.

Store:

- source ID;
- generator model/version;
- generation prompt;
- generation timestamp;
- validation status.

This preserves provenance.

## Research exercise

Generate 10k examples at three synthetic fractions.

Compare:

**quality → diversity → contamination → human error rate → training cost**

Then determine the maximum synthetic fraction that preserves the target data-quality requirements.

## Laboratory

[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## Reference

https://cs336.stanford.edu/
