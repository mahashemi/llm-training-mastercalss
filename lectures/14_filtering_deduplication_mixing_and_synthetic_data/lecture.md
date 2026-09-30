# Lecture 14 — Filtering, Deduplication, Mixing, and Synthetic Data

**Lab:** [Deduplication and Data Mixing](`./lab.ipynb`)

## Outcome

Students can isolate data interventions and quantify whether a cleaner corpus is actually more useful.

## The transformed budget

Show:

**100B raw → 60B filtered → 45B deduped → 45B sampled**

Ask what changed besides token count.

## Filtering

Filtering trades:

**coverage ↔ noise**

Teach thresholds as experiment variables.

## Deduplication and mixing

Exact and near dedup remove repeated content.

Mixing changes exposure rates across domains/languages.

For temperature sampling:

$q_i = \frac{p_i^{\alpha}}{\sum_j p_j^{\alpha}}$

The alpha choice changes the balance.

## Laboratory

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

## Break it

Increase synthetic data until teacher-correlated failures become visible.

Ask whether a larger dataset produced more useful diversity.

## Engineering decision

Every data transformation needs:

**hypothesis → isolated variable → metric → regression check**

## Exit challenge

Name one reason aggressive deduplication can hurt rather than help.

## Research bridge

Compare your classroom experiment with a published dataset-construction pipeline and identify the missing production stages.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
