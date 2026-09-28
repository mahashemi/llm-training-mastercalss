# Chapter 48 — Hallucination and Groundedness

**Part:** Part V

## 1. Separate two questions

**Factuality:** Is the claim true in the relevant world/source?

**Groundedness:** Is the claim supported by the supplied evidence?

These are related but not equivalent.

A model can be:

- factually correct but unsupported by the supplied context;
- grounded in a supplied document that is itself wrong or outdated;
- neither factual nor grounded;
- appropriately uncertain because evidence is insufficient.

## 2. Claim-level evaluation

Decompose an answer into claims.

For each claim:

| Claim | Supported by context? | Factually correct? | Citation valid? |
|---|---|---|---|
| C1 | yes | yes | yes |
| C2 | yes | no | points to wrong source |
| C3 | no | unknown | no |

This is far more diagnostic than one answer-level “hallucination” label.

## 3. Groundedness metric

Define:

groundedness = supported_claims / evaluable_claims

Example:

8 supported claims out of 10:

groundedness = 0.80

But report the denominator and evaluation rule.

Some claims may be opinions, common knowledge, or impossible to verify from the provided context. Define how those are handled before measuring.

## 4. Retrieval coupling

A wrong answer in RAG can arise from:

1. source wrong;
2. retrieval missed source;
3. wrong passage selected;
4. model ignored correct passage;
5. model invented unsupported content;
6. citation did not support the claim.

This is why groundedness debugging must connect to retrieval evaluation.

## 5. Oracle-context experiment

One powerful diagnostic:

### Run A
Normal retrieval.

### Run B
Provide the correct evidence directly.

If B improves substantially:

**retrieval/context assembly is a likely bottleneck.**

If B remains poor:

**generation/reasoning/model behavior is a stronger hypothesis.**

This experiment separates system layers.

## 6. Abstention

A trustworthy system needs an appropriate response when evidence is insufficient.

Define three outcomes:

- correct answer;
- correct abstention;
- unsupported answer.

Then measure:

| Metric | Meaning |
|---|---|
| Answer accuracy | correct substantive answers |
| Abstention precision | abstentions are actually appropriate |
| False-answer rate | unsupported answers |
| Coverage | fraction of cases answered rather than abstained |

Do not maximize answer rate alone.

## 7. Worked example

100 questions:

- 70 have sufficient evidence;
- 30 do not.

System:

- correctly answers 60 of the 70;
- correctly abstains on 24 of the 30;
- gives unsupported answers on 6 of the 30;
- answers incorrectly on 10 of the 70.

Report:

- answer accuracy = 60/70 on answerable cases = 85.7%;
- unsupported-answer rate = 6/100 = 6%;
- appropriate abstention rate = 24/30 = 80%.

This tells a different story than “84 answers were generated.”

## 8. Citation correctness

A citation can be:

- present but irrelevant;
- relevant but incomplete;
- correct for one claim but not another.

Evaluate at claim-to-source level.

For each claim ask:

**Does the cited span actually entail or support this claim?**

## 9. Failure taxonomy

Common categories:

- fabricated fact;
- unsupported inference;
- contradiction of evidence;
- stale evidence;
- citation mismatch;
- overconfident uncertainty;
- omission of critical evidence.

Use category counts to choose the next engineering intervention.

## Research exercise

Build a 100-item grounded QA test.

Annotate each answer at claim level.

Report:

- groundedness;
- factuality where verifiable;
- citation support;
- abstention quality;
- retrieval recall;
- oracle-context performance.

Then identify whether the dominant problem lies in retrieval or generation.

## Laboratory

[failure_analysis_and_safety_eval.ipynb](../../notebooks/failure_analysis_and_safety_eval.ipynb)

## References

- RAG: https://arxiv.org/abs/2005.11401
- Stanford CS336: https://cs336.stanford.edu/
