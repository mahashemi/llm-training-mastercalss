# Lecture 14 — Filtering, Deduplication, Mixing, and Synthetic Data

**Lab:** [Deduplication and Data Mixing](./lab.ipynb)

## Outcome

You can isolate data interventions and quantify whether a cleaner corpus is actually more useful.

## The transformed budget

Inspect:

**100B raw → 60B filtered → 45B deduped → 45B sampled**

Consider: what changed besides token count.

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

## Break it

Increase synthetic data until teacher-correlated failures become visible.

Consider: whether a larger dataset produced more useful diversity.

## Engineering decision

Every data transformation needs:

**hypothesis → isolated variable → metric → regression check**

## Exit challenge

Name one reason aggressive deduplication can hurt rather than help.

## Research bridge

Compare your classroom experiment with a published dataset-construction pipeline and identify the missing production stages.


## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 06 — Data Sources and Dataset Construction](../13_data_sources_and_dataset_construction/lecture.md) · [Next: Lecture 08 — Pretraining Systems →](../11_training_system_design/lecture.md)

</div>
## Video companions

[Video companions: data filtering, deduplication and synthetic data](https://www.youtube.com/results?search_query=LLM+data+filtering+deduplication+synthetic+data+lecture)

## Navigation

[← Previous](../13_data_sources_and_dataset_construction/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../15_mid_and_post_training_sft_and_rlhf/lecture.md)
