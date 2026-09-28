# Chapter 67 — Team Design for LLM Programs

**Part:** Part VIII

## 1. Treat people as a technical dependency

A model program can fail even with enough compute because key work is missing.

The minimum capability map is:

**research → data → training systems → evaluation → product/serving → governance → program management**

One person can cover several roles in a small pilot. At scale, those responsibilities must still exist even when job titles differ.

## 2. Role matrix

| Capability | Pilot responsibility | Scale responsibility | Typical outputs |
|---|---|---|---|
| Model research | architecture + optimization | research team | experiments, model configs |
| Data engineering | collection + processing | data platform team | datasets, pipelines |
| Training systems | single/multi-GPU | distributed systems | throughput, reliability |
| Evaluation | benchmarks + human tests | eval/release team | scorecards, release gates |
| ML/serving | prototype endpoint | inference/platform | SLOs, deployment |
| Domain/language | expert review | dedicated panel/team | quality criteria |
| Security/governance | basic controls | formal owners | policy, audit |
| Program management | schedule/budget | portfolio governance | milestones, procurement |

## 3. Example staffing plans

These are planning heuristics, not universal ratios.

### Tiny research pilot

| Role | Approx. capacity |
|---|---:|
| Technical lead/researcher | 1.0 |
| ML engineer | 1.0 |
| Data engineer | 0.5 |
| Evaluation/domain expert | 0.5 |
| Program/product | 0.25 |
| Infra/security | 0.25 |

This is enough to prove a narrow hypothesis, not to operate a large foundation-model program.

### Small production adaptation team

| Role | Approx. capacity |
|---|---:|
| ML/research | 2–4 |
| Data | 1–2 |
| Training/infra | 1–2 |
| Evaluation | 1–2 |
| Serving/platform | 1–2 |
| Domain/language | 1–3 |
| PM/program | 1 |
| Security/governance | 0.5–1 |

For a foundation-model program, these capabilities expand and gain specialists in distributed training, storage/networking, data governance, safety, benchmark operations, release engineering, procurement, and research publishing.

## 4. Single points of failure

Ask:

**If this person is unavailable for 30 days, can the program continue?**

Red flags include:

- only one person understands checkpoint recovery;
- only one person can reproduce the data pipeline;
- only one language expert can validate results;
- only one person can estimate compute;
- only one person owns deployment knowledge.

Mitigate with:

- runbooks;
- pair ownership;
- reproducibility checks;
- documented interfaces;
- backup ownership.

## 5. Staffing economics

TCO should include people:

C_people =
salary/contract
+ hiring
+ training
+ management
+ specialist review
+ external expertise

Do not compare an API with self-hosting while assigning the self-hosting team's labor a zero cost.

## 6. Team-to-milestone mapping

| Milestone | Owner | Exit evidence |
|---|---|---|
| Baseline | ML lead | reproducible benchmark |
| Data release | data lead | versioned dataset/card |
| Training pilot | systems + ML | throughput + loss curves |
| Quality gate | evaluation lead | evaluation report |
| Serving pilot | platform | p95 SLO + load test |
| Production release | program lead | release checklist |

A roadmap without ownership is a wish list.

## 7. Decision interfaces

**Data → research:** available data, provenance, quality, rights.

**Research → systems:** exact training configuration and success metrics.

**Systems → evaluation:** exact artifact, checkpoint, tokenizer, data version.

**Evaluation → program:** evidence and uncertainty.

**Program → procurement:** required capacity and time window.

These interfaces prevent each function from optimizing locally.

## 8. Worked example — 7B pilot

Suppose a team has:

- one model researcher;
- one general ML engineer;
- one part-time data engineer;
- one part-time evaluator;
- no dedicated infrastructure owner.

The pilot may work.

Before scaling, add ownership for:

- distributed training;
- checkpoint recovery;
- observability;
- storage/network;
- deployment.

Otherwise technical debt becomes a scaling blocker.

## Research exercise

Design a team for a 12-month project containing:

- one pilot model;
- one production adaptation;
- one paper;
- one public release.

For every role specify:

**responsibility → owner → backup → artifact → success metric**

## Laboratory

[national_llm_resource_plan.ipynb](../../notebooks/national_llm_resource_plan.ipynb)

## Reference

Stanford CS336: https://cs336.stanford.edu/
