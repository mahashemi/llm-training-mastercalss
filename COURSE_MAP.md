# Course Map — LLM Trainer Masterclass

**Canonical graph:** [Learning Graph](docs/LEARNING_GRAPH.md) · **[Persian Dataset Track](data/PERSIAN_DATASET_TRACK.md)**

The **README is the canonical pedagogical map**. This file is a compact reference for instructors and contributors; it is not a second curriculum.

## Natural teaching order

| Stage | Lecture IDs | Textbook | Primary purpose |
|---|---|---|---|
| 0. Orient | — | Ch. 00 | establish the real open-weight workflow and reproducibility spine |
| 1. Foundations | 01 → 02 → 04 → 05 | Ch. 01–13 | probability → tokens → Transformer → attention/MoE |
| 2. Training + systems | 03 → 06 → 07 → 08 → 09 → 11 | Ch. 14–16, 25, 39–40 | optimization, hardware, kernels, distributed training, scaling |
| 3. Evaluation contract | 12 | Ch. 41–47 | define evaluation before expensive training |
| 4. Real data | 13 → 14 | Ch. 17–24 | acquire, inspect, filter, deduplicate, mix; run the Persian longitudinal case |
| 5. Train + adapt | 15 → 18 → 19 | Ch. 26–33, 38 | SFT, full FT, LoRA/QLoRA, quantization |
| 6. Align | 16 → 20 | Ch. 34–37 | RLVR, preferences, DPO, distillation |
| 7. Extend + release | 17 → 21 | Ch. 48–50, 73 | multimodality, robustness, safety, release evaluation |
| 8. Serve + decide | 10 → 22 | Ch. 51–64 | inference, RAG/tools, API economics, training-method choice |
| 9. Program + research | 23 → 24 | Ch. 65–75 | national strategy, teams, compute, governance, proposals, funding |

## Mastery loop

At every stage:

**understand → implement → measure → break → diagnose → decide → reproduce**

The stage is complete only when the learner has an evidence artifact, not merely finished a reading or notebook.

## Materials hierarchy

**Lecture = narrative.**  
**Book = deep explanation.**  
**Notebook = executable experiment.**  
**Runbook = operational procedure.**  
**Project = synthesis / assessment.**

Use only the material attached to the current stage. Do not read all runbooks or open every notebook sequentially.

## Canonical navigation

[Master Course Flow in README](README.md#master-course-flow--the-one-path-through-the-repository) · [Lecture TOC](README.md#lecture-series-toc--24-lectures) · [Textbook TOC](README.md#textbook-toc--at-a-glance) · [Book ↔ Lecture ↔ Laboratory Map](BOOK_LAB_MAP.md)
