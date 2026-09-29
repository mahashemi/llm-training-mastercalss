# Course Operating Manual

## Core teaching loop

Every module follows:

**predict → explain → implement → measure → break → diagnose → decide → reproduce**

The lecture supplies the mental model. The textbook supplies depth. The notebook supplies evidence. The runbook supplies operational procedure.

## Individual learner

Follow:

**START_HERE → lectures → notebooks → textbook → projects → paper reproduction → Model Program Dossier**

Use [BOOK_LAB_MAP.md](../BOOK_LAB_MAP.md) whenever a chapter reuses a laboratory.

## Hardware progression

| Phase | Model/workload | Environment | Mastery target |
|---|---|---|---|
| A | tiny GPT | CPU | understand training mechanics |
| B | Qwen3-0.6B | free Colab | real checkpoint workflow |
| C | 1.7B/4B class | single GPU | resource scaling |
| D | 7B/8B | 1× H100 | professional adaptation/profiling |
| E | Qwen3.8-27B case study | H100 / multi-GPU | large-model resource planning |
| F | 7B–30B+ | multi-GPU H100 | distributed training |
| G | project-specific | H100 cluster | foundation-model program |

The exact model can change as the open-weight ecosystem changes. The workflow and evidence requirements should remain stable.

## University semester structure

| Phase | Focus | Required artifact |
|---|---|---|
| 1 | language modeling + tokenizer | tiny LM + tokenizer report |
| 2 | Transformer + attention | tensor-shape audit |
| 3 | resource accounting + GPUs | memory/FLOPs report |
| 4 | distributed + scaling | scaling curve |
| 5 | data | dataset card |
| 6 | SFT + PEFT | baseline/adaptation report |
| 7 | evaluation + safety | scorecard/failure taxonomy |
| 8 | inference | serving benchmark |
| 9 | research | reproduction/ablation |
| 10 | program design | final dossier |

## Independent-work readiness

A learner is ready for independent model work when they can:

- train a small model from scratch;
- download and audit an unfamiliar open-weight checkpoint;
- estimate inference and training memory;
- run a smoke-test training job;
- adapt a model with SFT and PEFT;
- evaluate target and retained capability;
- diagnose at least one failure;
- reproduce the run from exact versions;
- derive a larger resource plan from measured throughput.

## Instructor rule

Do not grade notebook completion. Grade:

**prediction quality + experimental control + measurements + diagnosis + decision quality + reproducibility**.

## Program-level use

For organizations, the same repository can serve as:

- onboarding;
- model-training SOP;
- evaluation standard;
- experiment archive;
- technical proposal library.

For a research program, require every expensive run to pass a cheaper evidence gate first.
