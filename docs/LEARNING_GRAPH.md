# Learning Graph — LLM Trainer Masterclass

This is the single dependency graph for the curriculum. It resolves the relationship between lectures, textbook chapters, real datasets, notebooks, runbooks, and projects without turning each artifact type into a separate course.

## 1. The learner's path

```text
ORIENT
  │
  ▼
FOUNDATIONS
  │
  ▼
TRAINING SYSTEMS
  │
  ▼
EVALUATION CONTRACT
  │
  ▼
REAL DATA
  ├───────────────┬─────────────────┬──────────────────┐
  ▼               ▼                 ▼                  ▼
English web    Multilingual      Persian track      Instruction /
corpora        corpora           + Persian-first    reasoning
  └───────────────┴─────────────────┴──────────────────┘
                          │
                          ▼
                  DATA INTERVENTIONS
             filter → dedup → mix → audit
                          │
                          ▼
                    TRAIN / ADAPT
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
        SFT/PEFT      Continued PT     From scratch
          └───────────────┼────────────────┘
                          ▼
                       ALIGN
                DPO / RLHF / RLVR /
                    distillation
                          │
                          ▼
                    EVALUATE AGAIN
              ┌───────────┼───────────────┐
              ▼           ▼               ▼
          robustness   multimodal       safety
              └───────────┼───────────────┘
                          ▼
                   SERVE / SYSTEM
             inference → RAG → tools
                          │
                          ▼
                   DECIDE / SCALE
             economics → program → capstone
```

## 2. The stage contract

Every stage uses the same learning loop:

**intuition → reading → lecture → real artifact → experiment → measurement → failure → decision → reproducibility**

| Stage | Learn | Touch real data/model | Produce evidence | Exit question |
|---|---|---|---|---|
| 0. Orient | workflow, checkpoints, reproducibility | open-weight checkpoint | audit card | Can I inspect a model before touching training? |
| 1. Foundations | LM objective, tokenizer, Transformer, attention, MoE | tiny corpus + checkpoint tokenizer | tensor/loss/tokenization measurements | Can I explain every major tensor? |
| 2. Training systems | optimization, GPU memory, kernels, distributed training, scaling | real model/resource profiles | resource worksheet | Can I predict whether a run fits? |
| 3. Evaluation | benchmarks, human/judge eval, statistics | real evaluation sets | evaluation contract | What would falsify my claim? |
| 4. Real data | acquisition, schema, quality, dedup, mixing | multiple HF/Kaggle sources | dataset manifest | Can I defend every training example's provenance? |
| 5. Train/adapt | SFT, FT, LoRA, QLoRA, continued PT | open-weight model + real data | experiment card | What problem does each intervention actually solve? |
| 6. Align | preferences, RLHF, DPO, RLVR, distillation | preference/reasoning data | alignment experiment | What signal is the model optimizing? |
| 7. Extend/release | multimodality, safety, robustness | multimodal + adversarial/eval data | release gate | Did capability improve without hiding regressions? |
| 8. Serve/decide | inference, RAG, tools, API economics | live/retrieval/tool scenarios | architecture decision record | Is training actually necessary? |
| 9. Program/research | scale, governance, teams, compute, funding | evidence from prior experiments | Model Program Dossier | Can I defend the entire program? |

## 3. The master material matrix

A learner should never have to guess which artifact belongs to a topic.

| Module | Lecture | Book | Mind map / visual | Real dataset | Primary lab | Runbook / decision aid | Project |
|---|---|---|---|---|---|---|---|
| Foundations | ✓ | ✓ | ✓ | small corpus | Tiny LM / Transformer | — | Tiny GPT |
| Tokenization | ✓ | ✓ | ✓ | Persian + multilingual slices | Tokenizer measurement | — | Tiny GPT |
| Training systems | ✓ | ✓ | ✓ | model/resource metadata | Resource/GPU/distributed labs | resource runbooks | Tiny GPT |
| Evaluation | ✓ | ✓ | ✓ | ParsiNLU / PersianMedQA / general benchmarks | Evaluation harness | Evaluation runbook | Data-quality paper |
| Data construction | ✓ | ✓ | ✓ | FineWeb / Dolma / CulturaX / Persian corpora | Real Dataset Bench | Dataset curation | Data-quality paper |
| Data quality | ✓ | ✓ | ✓ | web + Persian + synthetic | Dedup/mixing | Dataset curation | Data-quality paper |
| SFT | ✓ | ✓ | ✓ | Aya / task datasets / Persian instruction sets | Qwen SFT | SFT runbook | Domain SFT + PEFT |
| LoRA / QLoRA | ✓ | ✓ | ✓ | same controlled task data | PEFT comparison | PEFT runbook | Domain SFT + PEFT |
| Continued PT | ✓ | ✓ | ✓ | Persian web / Naab / FineWeb2-HQ / synthetic Persian | FT vs LoRA + resource experiments | Pretraining decision | Data-quality paper |
| Preference / DPO | ✓ | ✓ | ✓ | preference pairs | DPO concepts | SFT/PEFT + evaluation | Domain SFT + PEFT |
| RLVR | ✓ | ✓ | ✓ | verifiable reasoning | RLVR toy | training triage | Data-quality paper |
| Multimodality | ✓ | ✓ | ✓ | image-text / audio / video sources | alignment map | — | Capstone |
| RAG / tools | ✓ | ✓ | ✓ | documents / live records | Build-vs-buy | decision trees | Capstone |
| Serving | ✓ | ✓ | ✓ | model profiles | KV-cache / serving | inference runbook | Capstone |
| Program design | ✓ | ✓ | ✓ | all prior evidence | resource plan | funding/program runbooks | Model Program Dossier |

## 4. The Persian longitudinal case

Persian is not a one-off dataset example. It is a thread through the entire course:

```text
Persian text → tokenizer fertility → corpus provenance / filtering
→ Persian data mixture → continued pretraining / Persian-first training
→ SFT / PEFT → Persian evaluation → multilingual regression
→ serving / deployment economics → language-model program design
```

This lets students ask the same engineering question repeatedly:

> What changes when the target language has less high-quality digital data, different orthography/tokenization behavior, and different evaluation coverage?

## 5. Evidence artifacts

A stage is complete only when the learner can save the relevant artifact:

- **model audit:** checkpoint/config/tokenizer/resource record
- **tokenization:** fertility table and examples
- **data:** immutable source manifest + schema map + quality/dedup report
- **training:** loss/resource/checkpoint record
- **adaptation:** baseline vs intervention table
- **evaluation:** benchmark protocol + slice results + error taxonomy
- **serving:** latency/memory/TCO record
- **decision:** alternatives + evidence + gate
- **program:** Model Program Dossier

## 6. Rules that prevent curriculum sprawl

1. A new dataset must attach to an existing stage and lab before it becomes a course artifact.
2. A new notebook must replace a missing executable experiment; it should not duplicate an existing lab.
3. A runbook is a procedure, not another reading track.
4. A lecture must point to its primary laboratory and evidence artifact.
5. A book chapter must explain the mechanism and decision; it must not duplicate the lecture verbatim.
6. Every real-data experiment records source, revision, split, license/access basis, and preprocessing.
7. Every model comparison holds the relevant budget and evaluation protocol constant.
8. Every major claim must have a measurement path.

## 7. Definition of curriculum completeness

The curriculum is structurally complete when every major stage has:

**concept → lecture → book → real artifact → executable experiment → evaluation → failure mode → engineering decision → reproducible evidence**

Content can continue to evolve; the graph should remain stable.