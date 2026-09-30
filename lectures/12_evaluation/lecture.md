# Lecture 12 — Evaluation That Can Block a Bad Model

**Duration:** 25 minutes  
**Lab:** [Evaluation Harness](`./lab.ipynb`)

## Outcome

Students design evaluation before training, partition failures by layer, and distinguish statistical evidence from release significance.

## 0–4 — The benchmark trap

“Model B improved by 3 points.”

Ask:

- same examples?
- same prompt?
- same decoding?
- same evaluator?
- same contamination status?

## 4–9 — Requirement to metric

Requirement:

**correct + grounded + safe + fast**

Map each to measurable outputs.

Then create slices:

**language × difficulty × task × failure type**

## 9–14 — Automatic versus human evaluation

Compare:

| Method | Main value | Limitation |
|---|---|---|
| exact/automatic | cheap repeatability | narrow |
| model judge | broad semantic evaluation | bias/calibration |
| human | richer validity | expensive |
| hybrid | scale + audit | more infrastructure |

## 14–19 — Laboratory

Build a small scorecard.

The notebook should compute at least:

- aggregate score;
- per-slice score;
- failure count;
- confidence interval or bootstrap interval where appropriate.

## 19–22 — Break it

Create a benchmark with one easy slice dominating 80% of samples.

Observe how aggregate score hides rare failures.

## 22–24 — Release gates

Define both:

- quality gates;
- critical-failure blockers.

A model can improve aggregate quality and still fail release.

## 24–25 — Exit challenge

Write the minimum information needed for someone else to reproduce your reported score.

## Research bridge

Connect your benchmark protocol to the evaluation chapters and preserve the exact evaluation code/configuration alongside results.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
