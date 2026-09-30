# Lecture 14 — Filtering, Deduplication, Mixing, and Synthetic Data

**Duration:** 25 minutes  
**Lab:** [Deduplication and Data Mixing](`./lab.ipynb`)

## Outcome

Students can isolate data interventions and quantify whether a cleaner corpus is actually more useful.

## 0–4 — The transformed budget

Show:

**100B raw → 60B filtered → 45B deduped → 45B sampled**

Ask what changed besides token count.

## 4–9 — Filtering

Filtering trades:

**coverage ↔ noise**

Teach thresholds as experiment variables.

## 9–14 — Deduplication and mixing

Exact and near dedup remove repeated content.

Mixing changes exposure rates across domains/languages.

For temperature sampling:

**q_i = p_i^α / Σp_j^α**

The alpha choice changes the balance.

## 14–19 — Laboratory

Run a four-arm study:

A. loose filter  
B. medium filter  
C. medium + changed mixture  
D. medium + mixture + synthetic

Measure:

- token survival;
- language mix;
- validation loss;
- target score;
- duplicate rate.

## 19–22 — Break it

Increase synthetic data until teacher-correlated failures become visible.

Ask whether a larger dataset produced more useful diversity.

## 22–24 — Engineering decision

Every data transformation needs:

**hypothesis → isolated variable → metric → regression check**

## 24–25 — Exit challenge

Name one reason aggressive deduplication can hurt rather than help.

## Research bridge

Compare your classroom experiment with a published dataset-construction pipeline and identify the missing production stages.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
