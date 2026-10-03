# Learning Graph — LLM Trainer Masterclass

This is the dependency graph for the curriculum. It explains the progression; the **README Master Course Matrix** contains the detailed lecture → chapter → lab → dataset → runbook → evidence connections.

**[Open the single Master Course Matrix](../README.md#master-course-matrix--the-single-curriculum-control-plane)**

## 1. The learner's path

```text
ORIENT
  │
  ▼
NEURAL COMPUTING FOUNDATION
  │
  ├─ perceptron → backprop → SOM
  ├─ CNN → autoencoder → generative models
  ├─ RNN/LSTM/GRU → forecasting
  ├─ RBM/DBN → attention/Transformer
  └─ deep RL → research capstone
  │
  ▼
LLM FOUNDATIONS
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

## 2. Stage contract

Every stage uses one learner-facing unit:

**intuition → explanation → experiment → measurement → failure → decision → reproducibility**

The README matrix is the authoritative answer to “which material do I open next?”

The stages are:

- **-1 · Neural Computing Foundation** — 12 units covering classical and modern neural computation, with executable real-data laboratories and a publication-oriented capstone.

- **0 · Orient** — open-weight workflow, reproducibility, model audit.
- **1 · Foundations** — probability, tokenization, Transformer mechanics, attention, MoE.
- **2 · Training systems** — resource accounting, GPUs, kernels, efficient attention, distributed training, scaling, instrumentation.
- **3 · Evaluation contract** — metrics, slices, statistical discipline, and release gates before expensive training.
- **4 · Real data** — acquisition, schema, quality, deduplication, mixing, provenance.
- **5 · Train + adapt** — SFT, full fine-tuning, continued pretraining, LoRA, QLoRA.
- **6 · Align** — RLVR, preference optimization, DPO, and distillation.
- **7 · Extend + release** — multimodality, robustness, safety, failure analysis, release gates.
- **8 · Serve + decide** — inference, KV cache, RAG, tools, API economics, training-method choice.
- **9 · Program + research** — resource planning, research, governance, funding, capstone.

## 3. Material relationship

There is deliberately one learner path:

**Lecture → embedded Lab → real data → evaluation → decision → evidence**

The textbook and runbooks remain optional reference layers; they do not create additional navigation steps.

A laboratory may serve several lectures or chapters. Reuse is intentional; a new notebook is justified only when an existing experiment cannot demonstrate the required mechanism.

## 4. Persian longitudinal case

Persian is not a one-off dataset example. It is a thread through the course:

```text
Persian text → tokenizer fertility → corpus provenance / filtering
→ Persian data mixture → continued pretraining / Persian-first training
→ SFT / PEFT → Persian evaluation → multilingual regression
→ serving / deployment economics → language-model program design
```

See the [Persian Dataset Track](../data/PERSIAN_DATASET_TRACK.md).

## 5. Evidence artifacts

A stage is complete only when the learner can save the relevant artifact:

- **model audit:** checkpoint/config/tokenizer/resource record
- **tokenization:** fertility analysis and examples
- **data:** immutable source manifest + schema map + quality/dedup report
- **training:** loss/resource/checkpoint record
- **adaptation:** baseline vs intervention results
- **evaluation:** benchmark protocol + slice results + error taxonomy
- **serving:** latency/memory/TCO record
- **decision:** alternatives + evidence + gate
- **program:** Model Program Dossier

## 6. Rules that prevent curriculum sprawl

1. A new dataset must attach to an existing lecture and lab.
2. A new notebook must live inside the lecture that owns the experiment.
3. A runbook is a procedure, not another learner track.
4. A lecture must contain or directly expose its primary laboratory and evidence artifact.
5. A book chapter explains mechanism and decision; it does not duplicate the lecture verbatim.
6. Every real-data experiment records source, revision, split, license/access basis, and preprocessing.
7. Comparisons hold the relevant budget and evaluation protocol constant.
8. Every major claim has a measurement path.

## 7. Definition of curriculum completeness

The curriculum is complete when every major stage has:

**concept → lecture → embedded experiment → real artifact → evaluation → failure mode → engineering decision → reproducible evidence**

Content can evolve; the graph and the single curriculum matrix should remain stable.
