# Assessment and Mastery Rubric

## Principle

A learner does not “pass” because a notebook executed.

Every major stage uses the same evidence ladder:

**Understand → Implement → Measure → Break → Explain → Decide → Reproduce → Research**

## Rubric

| Level | Evidence |
|---|---|
| 0 — Exposure | Can define terms |
| 1 — Understanding | Can explain mechanism and equations |
| 2 — Implementation | Can implement or modify the method |
| 3 — Measurement | Can produce a baseline and quantitative result |
| 4 — Diagnosis | Can reproduce and explain a failure |
| 5 — Engineering | Can choose among alternatives under constraints |
| 6 — Research | Can formulate and test a falsifiable hypothesis |
| 7 — Program leadership | Can turn evidence into a budgeted, staged proposal |

## Stage gates

### Gate A — Foundations
Pass when the learner can build a tiny language model and explain the training loop without hiding behind a framework.

### Gate B — Transformer
Pass when the learner can trace every major tensor shape through a decoder-only Transformer and explain causal masking.

### Gate C — Data
Pass when the learner can create a versioned dataset with provenance, filtering, deduplication, and an evaluation split.

### Gate D — Systems
Pass when the learner can estimate model memory/FLOPs and explain why throughput differs from peak hardware specifications.

### Gate E — Post-training
Pass when the learner can compare SFT, full FT, LoRA, and QLoRA as different choices along multiple axes.

### Gate F — Evaluation
Pass when the learner can design an evaluation suite before training and analyze failures by category.

### Gate G — Serving
Pass when the learner can benchmark latency/throughput and explain KV-cache behavior.

### Gate H — Decision
Pass when the learner can defend API/RAG/tools/training choices using evidence and TCO assumptions.

### Gate I — Program
Pass when the learner can submit and defend the Model Program Dossier.

## Oral defense

At the final stage, ask the learner:

1. Why should we train anything?
2. What is our strongest baseline?
3. Why is the chosen method cheaper or more appropriate than alternatives?
4. What data are we allowed to use?
5. How do we know the model improved?
6. What happens if the main run fails?
7. What is the next cheapest experiment?
8. What would cause us to stop spending?

The learner should answer with evidence, not authority.
