# Chapter 45 — Error Taxonomies

**Part:** Part V

## 1. Why a taxonomy matters

“Accuracy is 82%” does not tell an engineer what to fix.

A useful taxonomy maps:

**observed failure → likely cause → cheapest confirming test → intervention**

## 2. First-level taxonomy

| Failure bucket | Example | Likely layer |
|---|---|---|
| Knowledge access | outdated fact | retrieval/source |
| Reasoning | arithmetic error | model/task |
| Evidence use | ignores supplied evidence | generation |
| Format | invalid JSON | interface/behavior |
| Tool selection | chooses wrong API | agent policy |
| Tool arguments | wrong ID/date | model/schema |
| Safety | unsafe recommendation | policy/model/system |
| Language | malformed target language | tokenizer/training |
| Robustness | fails after paraphrase | model/data |
| Reliability | timeout/retry failure | infrastructure |

## 3. Make buckets mutually useful

A good taxonomy should be:

- observable;
- sufficiently specific to change engineering action;
- stable across evaluators;
- measurable.

Avoid overlapping labels such as “bad answer” and “reasoning problem” unless their decision meaning is explicit.

## 4. Error-rate decomposition

If 1,000 examples produce:

- 80 retrieval failures;
- 50 evidence-use failures;
- 30 format failures;
- 20 safety failures;
- 820 successes;

then:

retrieval error = 8%  
evidence-use error = 5%  
format error = 3%  
safety error = 2%

The total failure rate is 18%, but the bucketed view tells you where to investigate first.

## 5. Severity matters

Do not treat all errors equally.

Add severity:

| Severity | Example | Handling |
|---|---|---|
| S0 | harmless formatting | backlog |
| S1 | minor wrong detail | fix/monitor |
| S2 | meaningful task failure | regression gate |
| S3 | harmful/high-impact | release blocker |

The exact definitions must be set for the domain.

## 6. Root-cause workflow

For each failure:

1. reproduce;
2. classify;
3. isolate layer;
4. formulate hypothesis;
5. run smallest confirming test;
6. apply intervention;
7. re-evaluate original failure;
8. check regressions.

This prevents “training by anecdote.”

## 7. Worked example

Symptom:

“The assistant gave a wrong policy answer.”

Test 1: Was the correct policy retrieved?

- No → retrieval failure.
- Yes → continue.

Test 2: Does the supplied evidence entail the correct answer?

- No → source/interpretation problem.
- Yes → continue.

Test 3: Can the model answer correctly with oracle context?

- No → generation/reasoning gap.
- Yes → retrieval/context-assembly issue.

This is a causal diagnostic tree.

## 8. Error Pareto analysis

Sort error buckets by frequency × severity.

A rare S3 failure can deserve more engineering attention than a common S1 formatting issue.

A useful program dashboard has:

**frequency × severity × trend × owner**

## Research exercise

Label 500 failures from a real or synthetic task.

Produce:

- taxonomy;
- severity;
- frequency;
- root-cause hypothesis;
- proposed experiment.

Then identify the smallest experiment that could distinguish your top two root-cause hypotheses.

## Laboratory

[failure_analysis_and_safety_eval.ipynb](../../notebooks/failure_analysis_and_safety_eval.ipynb)

## Reference

https://cs336.stanford.edu/
