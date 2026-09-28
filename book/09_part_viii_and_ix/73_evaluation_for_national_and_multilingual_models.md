# Chapter 73 — Evaluation for National and Multilingual Models

**Part:** Part VIII

## 1. A single average is dangerous

For multilingual models, a single aggregate score can hide severe failures in low-resource languages.

Report at least:

**language × task × domain × safety slice**

Example:

| Language | QA | Instruction | Summarization | Safety |
|---|---:|---:|---:|---:|
| L1 | 82 | 88 | 79 | 91 |
| L2 | 76 | 81 | 73 | 87 |
| L3 | 54 | 61 | 49 | 68 |
| L4 | 91 | 92 | 88 | 94 |

The average can look healthy while L3 remains unusable.

## 2. Native evaluation

Use native-language tests for:

- reading comprehension;
- instruction following;
- summarization;
- reasoning;
- terminology;
- spelling;
- morphology;
- code-switching;
- safety;
- domain-specific tasks.

Translation of an English benchmark can be an additional test, but it should not be the entire evaluation strategy.

## 3. Evaluation layers

| Layer | Question |
|---|---|
| Capability | Can the model perform the task? |
| Language | Does it perform naturally in the target language? |
| Domain | Does terminology match expert expectations? |
| Safety | Does it avoid harmful failures? |
| Robustness | Does performance survive perturbations? |
| Product | Does the task succeed under real constraints? |
| Operations | Is latency/cost acceptable? |

## 4. Benchmark construction

A serious native benchmark should document:

- task definition;
- population;
- language/variety;
- source provenance;
- annotation guidelines;
- reviewer qualifications;
- train/dev/test split;
- contamination controls;
- scoring method;
- uncertainty.

## 5. Human evaluation

For open-ended outputs, human review is often necessary.

Use at least:

- rubric-defined criteria;
- blinded model identity;
- multiple raters where feasible;
- disagreement tracking;
- adjudication rules.

Report:

- mean/median;
- agreement;
- confidence interval where appropriate;
- sample size.

Do not treat one reviewer rating 20 examples as statistically decisive.

## 6. Model-as-judge

Judge models can increase throughput, but they require validation.

Compare judge decisions against a human-labeled subset.

Measure:

- agreement;
- false positives;
- false negatives;
- systematic language bias;
- sensitivity to verbosity/style.

A judge should be calibrated, not assumed correct.

## 7. Contamination and leakage

Protect high-value evaluation data.

Useful controls:

- hidden test sets;
- temporal holdouts;
- source-based splits;
- n-gram overlap checks;
- semantic similarity checks;
- known benchmark contamination scans.

A higher score after contamination is not evidence of capability improvement.

## 8. Statistical thinking

For a proportion metric p over n independent examples, the rough standard error is:

SE ≈ sqrt(p(1-p)/n)

For example, if p = 0.80 and n = 400:

SE ≈ 0.02

A small benchmark score difference may therefore be noise.

The independence assumption may be false for clustered tasks, so use appropriate bootstrap or clustered methods when needed.

## 9. Language regression matrix

Every multilingual training change should compare:

**new model vs previous model**

across all target languages.

Track:

Δ score, Δ error rate, Δ safety failures, Δ human preference.

Flag regressions explicitly.

## 10. Worked example

Suppose a new training mixture produces:

| Language | Old QA | New QA | Delta |
|---|---:|---:|---:|
| L1 | 82 | 85 | +3 |
| L2 | 76 | 78 | +2 |
| L3 | 54 | 50 | −4 |
| L4 | 91 | 92 | +1 |

An aggregate average may increase.

The program still needs to investigate L3 because the model's intended multilingual capability has regressed there.

Possible causes:

- reduced sampling;
- tokenizer effects;
- domain shift;
- forgetting;
- evaluation artifacts.

## 11. Product-level evaluation

A national model should eventually be tested on real workflows:

**task completion → latency → cost → safety → human review**

For example, a public-service assistant can be evaluated on complete tasks rather than only question answering.

## Research exercise

Build a 4-language benchmark with:

- 100 items/language;
- 4 task categories;
- native-language evaluation;
- human review subset;
- safety slice.

Report per-language scores and uncertainty. Then run a simulated regression and explain why the aggregate should not be the only release gate.

## Laboratory

[evaluation_harness.ipynb](../../notebooks/evaluation_harness.ipynb)

## References

- Stanford CS336: https://cs336.stanford.edu/
- OLMo 2 evaluation/reproduction materials: https://allenai.org/olmo2
