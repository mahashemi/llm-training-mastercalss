# Chapter 43 — Human Evaluation

**Part:** Part V

## 1. Why humans remain necessary

Open-ended quality often depends on properties that automatic metrics only approximate:

- correctness;
- helpfulness;
- relevance;
- clarity;
- safety;
- grounding;
- cultural/linguistic appropriateness.

Human evaluation is therefore a measurement system that needs its own design.

## 2. Absolute vs pairwise evaluation

| Method | Annotator task | Strength | Weakness |
|---|---|---|---|
| Absolute rating | score each response | easy to aggregate | scale interpretation varies |
| Pairwise | choose A/B | simpler relative judgment | needs more comparisons |
| Ranking | order several outputs | rich comparison | cognitively heavier |
| Rubric + free text | score + explain | diagnostic | expensive |

Use pairwise evaluation when the practical question is “which system is better on this case?” and absolute ratings when fixed thresholds matter.

## 3. Build a rubric

A good rubric defines:

**criterion → allowed scale → anchor examples → edge cases**

Example for grounded QA:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Correctness | wrong | partly correct | correct |
| Evidence use | unsupported | partly supported | supported |
| Relevance | off-topic | some excess | focused |
| Safety | unsafe | borderline | appropriate |

The anchors reduce annotator drift.

## 4. Sampling

Do not sample only easy or spectacular prompts.

Stratify by:

- user intent;
- language;
- difficulty;
- domain;
- input length;
- failure history;
- safety category.

If production is 80% easy questions and 20% difficult cases, a 50/50 evaluation may estimate a useful stress scenario but is not representative of average user traffic. Report both.

## 5. Pairwise preference uncertainty

If n paired examples are evaluated and the candidate wins k:

p_hat = k / n

The uncertainty depends on n and the sampling design.

Do not treat 53% vs 51% on 100 examples as decisive without an uncertainty analysis.

## 6. Agreement

Track disagreement.

Useful measures include:

- percent agreement;
- Cohen's kappa for two raters on categorical labels;
- Krippendorff's alpha for broader annotation settings.

Agreement is diagnostic, not a proof that the rubric is valid.

Low agreement may mean:

- ambiguous examples;
- poor rubric;
- insufficient training;
- genuinely subjective task.

## 7. Blinding

Whenever feasible, hide model identity.

Otherwise:

**brand knowledge → expectation → rating**

can contaminate the measurement.

Also randomize response order in pairwise evaluation.

## 8. Worked example

Suppose 400 blind pairwise comparisons produce:

- candidate A wins 220;
- candidate B wins 180.

Observed win rate A:

220/400 = 55%

Before claiming a meaningful improvement, inspect:

- confidence interval;
- slice-specific wins;
- annotator agreement;
- examples driving the difference.

A 55% aggregate may conceal a severe regression in one language or safety slice.

## 9. Cost planning

Human evaluation cost is:

C_human =
examples × time/example × hourly reviewer cost

Then add:

- adjudication;
- training;
- quality control;
- recruitment;
- domain experts.

For 2,000 examples at 2 minutes each:

2,000 × 2 min = 4,000 min ≈ 66.7 reviewer-hours

That is before adjudication.

## 10. Human + automated hybrid

A practical workflow:

**automatic evaluation → identify uncertain/high-impact cases → human review → update rubric → re-run**

This makes human effort concentrate on cases where it adds the most information.

## Research exercise

Design a blind pairwise study with 500 examples.

Specify:

- sampling;
- rubric;
- raters;
- blinding;
- agreement measurement;
- uncertainty;
- adjudication;
- reporting.

Then estimate labor cost.

## Laboratory

[failure_analysis_and_safety_eval.ipynb](../../notebooks/failure_analysis_and_safety_eval.ipynb)

## Reference

https://arxiv.org/abs/2203.02155
