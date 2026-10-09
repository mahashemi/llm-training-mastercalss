# Student Research Project Catalog

## From first experiment to publishable evidence

This catalog is the **research-project layer of the LLM Training Masterclass**.

It is intentionally different from a collection of Kaggle exercises. A good project here is not defined by the model used. It is defined by a **question that can be answered with evidence**.

The catalogue is designed around one progression:

> **Build → Reproduce → Measure → Break → Explain → Intervene → Ablate → Generalize → Communicate → Release**

A learner may begin with a small CPU/Colab experiment and keep the same research question as the project grows. The final project does not have to train a huge model. A careful small-scale study, benchmark, dataset contribution, negative result, or reproducibility study can be valuable when the evidence is strong.

> **Publication is never guaranteed.** The goal is to teach a research process that produces work worth evaluating for publication.

---

## 1. The project ladder

Do not interpret **Beginner / Intermediate / Advanced** as three unrelated lists.

Each project can move through the ladder:

| Level | Learner does | Minimum evidence | Typical output |
|---|---|---|---|
| **P0 · Build** | Implement a known method | Working implementation + sanity checks | Reproducible notebook |
| **P1 · Reproduce** | Reproduce a published/reference result | Correct protocol + comparison | Reproduction report |
| **P2 · Measure** | Change one controlled variable | Baseline/intervention table | Experimental report |
| **P3 · Break** | Find failure modes | Slice/error analysis | Failure taxonomy |
| **P4 · Explain** | Test why the failure occurs | Diagnostic experiment | Mechanistic analysis |
| **P5 · Intervene** | Propose a targeted improvement | Baseline + intervention | Research report |
| **P6 · Ablate** | Determine what actually matters | Ablation matrix | Paper-quality evidence |
| **P7 · Generalize** | Test another dataset/domain/language/model | Cross-setting evidence | Benchmark/study |
| **P8 · Communicate** | Write the scientific story | Figures/tables/limitations | Paper or technical report |
| **P9 · Release** | Make the work reusable | Code/data/config/model cards | Public research package |

### The important rule

**Do not jump from P0 to “invent a new architecture.”**

A learner should first be able to show that the baseline works, understand its failure modes, and isolate the variable responsible for the claimed improvement.

---

# 2. Project selection map

Choose a project by the skill you want to develop, not by the fashionable model.

| If you want to learn… | Start with… | Then grow into… |
|---|---|---|
| Neural-network fundamentals | P01, P02 | optimization/architecture study |
| Representation learning | P03, P04 | probing + transfer study |
| Tokenization | P05, P06 | multilingual/Persian tokenizer paper |
| Dataset engineering | P07, P08 | data-mixture/data-quality study |
| Pretraining | P09, P10 | scaling/data-law experiment |
| SFT/PEFT | P11, P12 | efficiency/generalization paper |
| Preference optimization | P13 | preference-data/evaluation study |
| Evaluation | P14, P15 | benchmark or failure-analysis paper |
| Reliability | P16, P17 | robustness/calibration study |
| Multilingual NLP | P18, P19 | low-resource transfer study |
| Persian NLP | P20–P24 | Persian-first research program |
| Islamic text | P27–P29 | provenance/retrieval/evaluation study |
| Multimodal learning | P30, P31 | compositional/generalization study |
| Systems | P32–P34 | efficiency/serving benchmark |
| Agents/tools | P35, P36 | reliability/evaluation research |
| Research methodology | P37–P48 | independent paper / benchmark / dataset / systems study |

---

# 3. Foundation projects — learn to ask scientific questions

These replace the traditional “MNIST/Cats vs Dogs” project list with experiments that teach a transferable research skill.

## P01 · Can a tiny neural network learn the mechanism we think it learns?

**Question:** When a small network memorizes a dataset, what changes as we increase width, depth, regularization, or data?

**Data:** MNIST or Fashion-MNIST.

**Build:** MLP from scratch and in PyTorch.

**Research ladder:**
- P0: reproduce training.
- P2: width/depth sweep.
- P3: compare training vs validation behavior.
- P4: inspect memorization on shuffled labels.
- P5: test regularization.
- P6: repeat across seeds.

**Evidence:** learning curves, parameter count, train/validation gap, seed variance, compute.

---

## P02 · What actually makes backpropagation work?

**Question:** Which optimization choices materially change convergence?

**Data:** UCI Banknote or a controlled synthetic classification task.

**Build:** manual forward/backward pass → autograd implementation.

**Interventions:** initialization, learning rate, optimizer, batch size, normalization.

**Research extension:** compare theoretical gradient expectations against measured gradients and identify instability regimes.

---

## P03 · Do learned representations preserve structure?

**Question:** Does a latent representation preserve class information, neighborhood structure, or nuisance information?

**Data:** MNIST, UCI-HAR, or another small real dataset.

**Methods:** PCA, autoencoder, supervised encoder.

**Research extension:** probe the same representation with multiple lightweight classifiers and distance metrics.

**Evidence:** reconstruction, probe accuracy, neighborhood preservation, visualization, failure cases.

---

## P04 · When does a CNN learn the object versus the background?

**Question:** How sensitive is a vision model to controlled changes in background, texture, crop, and corruption?

**Data:** CIFAR-10 plus CIFAR-10-C or a controlled augmentation split.

**Research extension:** train identical models under different augmentation/data regimes and test out-of-distribution slices.

**Paper path:** robustness analysis rather than another image-classification tutorial.

---

# 4. Tokenization and language representation

Tokenization is one of the strongest places for a course project to become real research.

## P05 · Tokenization efficiency across languages

**Question:** How does tokenizer design change the amount of computation required to represent the same information?

**Data:** matched samples from English, Persian, Arabic, Urdu, Turkish, or another language family.

**Compare:** at least two tokenizer families/configurations.

**Measure:**
- vocabulary size;
- tokens per byte;
- tokens per Unicode character;
- tokens per whitespace-delimited word;
- sequence-length expansion;
- rare-script behavior;
- ZWNJ/diacritic/punctuation behavior;
- estimated attention cost.

**Research extension:** test whether tokenizer fertility predicts downstream task degradation.

---

## P06 · Can a tokenizer be good on average but bad for a language?

**Question:** Does global corpus optimization hide systematic inefficiency for low-resource scripts?

**Data:** multilingual corpus with controlled language-balanced samples.

**Intervention:** train/reconfigure tokenizer with language-aware sampling.

**Ablations:** language mixture, vocabulary size, normalization, byte fallback.

**Deliverable:** tokenizer card + fertility benchmark + qualitative tokenization atlas.

---

# 5. Data is a model component

## P07 · Does “better data” beat “more data”?

**Question:** Under a fixed compute budget, which data-quality interventions provide the largest improvement?

**Data:** a manageable open corpus subset.

**Interventions:** deduplication, language filtering, quality filtering, document-length filtering, contamination removal.

**Critical rule:** keep token budget fixed when comparing mixtures.

**Evidence:** downstream score, training loss, unique-document count, duplicate rate, token composition, cost.

---

## P08 · Synthetic data: when does more become worse?

**Question:** At what mixture of human and synthetic instruction data does synthetic data stop helping?

**Data:** public instruction data plus generated examples.

**Intervention:** 0%, 10%, 25%, 50%, 75%, 100% synthetic mixture.

**Ablations:** generator model, filtering, diversity, difficulty.

**Evidence:** task performance, diversity, repetition, contamination checks, failure taxonomy.

---

# 6. Pretraining and scaling

## P09 · Does a small scaling law predict the next experiment?

**Question:** Can a controlled family of small language models predict how loss changes with model size, data, and compute?

**Build:** several tiny decoder-only models.

**Measure:** training tokens, parameters, FLOPs, wall time, validation loss.

**Research extension:** fit scaling relationships, hold out a configuration, predict it, then measure the prediction error.

**Deliverable:** scaling-law report with uncertainty and resource assumptions.

---

## P10 · Data quality versus parameter count under fixed compute

**Question:** When compute is limited, should resources go toward a larger model or better training data?

**Design:** matched compute budget with multiple model/data combinations.

**Key requirement:** compare equalized training budgets.

**Evidence:** loss, downstream tasks, data composition, compute efficiency.

**Paper path:** controlled empirical study.

---

# 7. Adaptation and efficient fine-tuning

## P11 · LoRA rank: does more rank actually help?

**Question:** How does adapter rank affect quality, trainable parameters, memory, time, and generalization?

**Model:** a small open-weight language model.

**Data:** one general instruction dataset plus one domain dataset.

**Sweep:** multiple ranks with fixed training protocol.

**Ablations:** target modules, rank pattern, learning rate.

**Evidence:** quality/resource Pareto frontier.

---

## P12 · LoRA versus QLoRA versus full fine-tuning

**Question:** Under a fixed quality target, which adaptation method reaches it with the least resource cost?

**Control:** same base model, dataset, training steps, evaluation suite.

**Measure:** trainable parameters, peak memory, throughput, wall time, quality, forgetting.

**Deliverable:** reproducible efficiency benchmark.

---

## P13 · Preference optimization: does the preference data matter more than the algorithm?

**Question:** How much of an improvement attributed to DPO/preference optimization comes from preference-pair quality?

**Interventions:** pair difficulty, margin, annotator agreement, synthetic vs human-derived pairs.

**Ablation:** algorithm held constant while preference data changes.

**Research value:** separates “algorithm effect” from “data effect.”

---

# 8. Evaluation as a research discipline

## P14 · Can aggregate scores hide important failures?

**Question:** Does an overall benchmark score conceal systematic failures on specific capabilities?

**Build:** evaluation harness with predefined slices.

**Slices:** length, language, domain, negation, numbers, rare entities, formatting, multi-step reasoning.

**Evidence:** aggregate score + slice matrix + error taxonomy.

---

## P15 · Benchmark contamination and evaluation validity

**Question:** How much can benchmark familiarity or overlap change apparent performance?

**Study:** create controlled near-duplicate/overlap cases and compare evaluation outcomes.

**Deliverable:** contamination protocol, detection methodology, and interpretation guide.

---

## P16 · Calibration of language-model confidence

**Question:** When a model expresses confidence, does confidence track correctness?

**Tasks:** multiple-choice QA, classification, or structured prediction.

**Measure:** calibration error, reliability diagrams, selective accuracy, abstention curves.

**Interventions:** temperature scaling, prompting, self-consistency, verifier.

---

## P17 · Can an evaluator distinguish good from bad answers?

**Question:** How reliable are automatic judges compared with reference-based metrics and human labels?

**Study:** create paired responses with known quality differences.

**Measure:** judge agreement, positional bias, verbosity bias, language bias, sensitivity to factual errors.

**Research extension:** evaluator ensemble or rubric intervention.

---

# 9. Multilingual and low-resource research

## P18 · Cross-lingual transfer under equal data budgets

**Question:** What happens when languages receive the same token budget rather than the same document count?

**Languages:** choose 3–5 languages with different scripts/resources.

**Compare:** multilingual model, language-adapted model, and balanced-data variant.

**Evidence:** task performance per language, tokenizer fertility, training cost.

---

## P19 · Does continued pretraining improve a low-resource language?

**Question:** When does domain/language continued pretraining help, and when does it cause forgetting?

**Base:** open-weight multilingual model.

**Data:** controlled low-resource corpus.

**Measure:** target-language gains + unrelated-language regression.

**Ablations:** corpus size, learning rate, training duration, mixture with original-language data.

---

# 10. Persian research track

Persian should not be a decorative example. It can become a longitudinal research program across the entire course.

## P20 · Persian tokenizer atlas

**Question:** Which tokenizer behaviors create the largest computational penalty for Persian?

**Study:** Persian corpora across news, literature, web, educational, technical, and conversational text.

**Measure:** fertility, sequence length, ZWNJ handling, Arabic/Persian character variants, numerals, punctuation, rare words.

**Research extension:** design a Persian-aware tokenizer intervention and evaluate downstream impact.

---

## P21 · Persian corpus quality versus quantity

**Question:** Which corpus transformations most improve a fixed-token Persian training mixture?

**Interventions:** normalization, deduplication, quality filtering, boilerplate removal, document balancing.

**Control:** fixed token budget.

**Evidence:** corpus statistics + language-model loss + downstream Persian evaluations.

---

## P22 · Persian instruction-data scaling

**Question:** How does instruction-data quantity, diversity, and synthetic proportion affect Persian instruction following?

**Mixtures:** small human set, filtered synthetic set, mixed sets.

**Ablations:** diversity, difficulty, source domain, synthetic generation model.

---

## P23 · Persian evaluation benchmark construction

**Question:** What important Persian capabilities are absent from existing benchmarks?

**Build:** a documented evaluation set covering language, reasoning, factuality, cultural context, safety, and instruction following.

**Research contribution:** benchmark/data paper with annotation guidelines, provenance, splits, licensing basis, and contamination controls.

---

## P24 · Persian versus multilingual regression

**Question:** Can Persian adaptation improve Persian performance without silently damaging other languages?

**Measure:** Persian gains, multilingual regression, tokenizer changes, representation drift, and compute cost.

**Deliverable:** language-regression dashboard.

---

# 11. Persian literature, OCR, and historical text

## P25 · OCR error propagation into language-model training

**Question:** Which OCR errors matter most downstream?

**Data:** scanned Persian books with OCR text and manually verified samples where licensing permits.

**Study:** characterize substitutions, missing words, spacing/ZWNJ errors, punctuation loss, and sentence corruption.

**Intervention:** targeted correction versus generic cleaning.

**Research output:** OCR error taxonomy + downstream impact study.

---

## P26 · Historical Persian text normalization

**Question:** Does normalization make historical text more useful, or erase valuable linguistic information?

**Study:** preserve an original layer and create controlled normalization variants.

**Measure:** retrieval, language-model loss, tokenization, named entities, historical vocabulary retention.

---

# 12. Islamic text research track

This track emphasizes **provenance, textual integrity, retrieval, attribution, and evaluation** rather than treating religious text as ordinary web text.

## P27 · Provenance-aware retrieval over Islamic texts

**Question:** Can a system answer a question while reliably identifying the exact source passage?

**Corpus:** legally usable/openly distributable Qur'an, hadith, tafsir, fiqh, history, or scholarly texts.

**Build:** lexical retrieval → dense retrieval → hybrid retrieval.

**Measure:** retrieval recall, attribution accuracy, citation completeness, exact-source recovery.

**Research extension:** provenance-aware reranking.

---

## P28 · Retrieval versus memorization for religious QA

**Question:** Does retrieval actually improve factual/source-grounded answers?

**Compare:** parametric-only, retrieval-augmented, and citation-constrained systems.

**Evaluate:** answer correctness separately from source attribution.

**Important:** preserve source editions, metadata, and textual variants rather than collapsing them into one undifferentiated corpus.

---

## P29 · Hadith/textual attribution benchmark

**Question:** Can a model distinguish “supported by the cited source,” “contradicted by the source,” and “not found in the source”?

**Build:** a provenance-grounded evaluation set.

**Research value:** tests attribution rather than generic language fluency.

---

# 13. Multimodal projects

## P30 · Image-text matching and hard negatives

**Question:** What makes a negative example genuinely difficult for a multimodal model?

**Data:** Flickr30k/COCO or another permitted image-text dataset.

**Interventions:** random negatives, semantic hard negatives, compositional hard negatives.

**Measure:** retrieval metrics + qualitative compositional failures.

---

## P31 · OCR-to-VLM pipeline for historical documents

**Question:** How does OCR quality propagate through multimodal retrieval or question answering?

**Pipeline:** image → OCR → text retrieval → answer.

**Intervention:** OCR correction, layout-aware extraction, image-native model.

**Research output:** end-to-end error attribution rather than a single final score.

---

# 14. Systems and efficiency research

## P32 · KV-cache economics

**Question:** How do context length, batch size, precision, and model architecture affect inference memory and latency?

**Measure:** TTFT, inter-token latency, throughput, peak memory.

**Deliverable:** reproducible serving benchmark.

---

## P33 · Quantization quality/resource frontier

**Question:** How much quality can be traded for memory and throughput?

**Compare:** multiple precision/quantization configurations on the same workload.

**Evaluate:** task quality, generation behavior, latency, memory, and failure slices.

---

## P34 · Attention implementation study

**Question:** Which attention implementation choices matter at different sequence lengths?

**Study:** naive attention, optimized kernels, grouped/multi-query variants where applicable.

**Evidence:** correctness checks + memory + throughput + sequence-length scaling.

---

# 15. Agents, tools, and reliable systems

## P35 · Tool-use reliability under adversarial instructions

**Question:** Can an agent distinguish user instructions from untrusted tool output?

**Build:** controlled tool environment.

**Measure:** task success, unsafe tool calls, instruction confusion, recovery behavior.

**Research extension:** structured tool policies or provenance labels.

---

## P36 · When should an application use RAG, tools, or training?

**Question:** Under what workload characteristics does each intervention provide measurable value?

**Variables:** knowledge freshness, private data, latency, task repeatability, structured actions, context size.

**Build:** the same application three ways.

**Deliverable:** controlled decision matrix with TCO and failure analysis.

---

# 16. Advanced research projects

These are intentionally open-ended. The learner must first establish a strong baseline.

## P37 · Data mixture optimization

Learn whether a fixed compute budget should contain more high-quality general data, domain data, multilingual data, or synthetic data.

**Core contribution:** a controlled mixture experiment with held-out evaluation.

---

## P38 · Representation drift during continued pretraining

Measure how internal representations change as a model adapts to a new language/domain.

**Possible analyses:** probes, activation similarity, parameter changes, forgetting, layer-wise effects.

---

## P39 · Adapter composition and interference

Study what happens when multiple LoRA/adapters trained for different tasks or languages are composed or merged.

**Research variables:** rank, layer targets, merge strategy, task similarity, language similarity.

---

## P40 · Distillation under a fixed inference budget

Compare different teacher-student strategies while holding student size and inference budget constant.

**Question:** what information transfers, what is lost, and what data makes distillation effective?

---

## P41 · Long-context failure analysis

Do not ask only “can the model handle 32k/128k tokens?”

Ask:
- which information is lost;
- where does retrieval degrade;
- what happens with distractors;
- how does position affect recall;
- how does attention/memory cost scale?

Produce a diagnostic benchmark rather than one context-length score.

---

## P42 · Small-model reasoning efficiency

Study whether a smaller model can achieve a target reasoning quality through better data, verifier use, retrieval, or distillation rather than simply increasing parameters.

**Contribution:** quality/latency/cost frontier.

---

# 17. Publication-grade capstones

These projects are not “harder notebooks.” They are complete scientific studies.

## P43 · Build a benchmark

Create a narrowly defined benchmark that exposes a real failure not visible in existing aggregate metrics.

Minimum:
- task definition;
- dataset card;
- annotation protocol;
- train/dev/test policy;
- contamination policy;
- baseline suite;
- metrics;
- error taxonomy;
- reproducible evaluator.

---

## P44 · Build a dataset

Create a useful, documented dataset rather than merely downloading one.

Minimum:
- source inventory;
- licensing/access analysis;
- provenance;
- filtering;
- deduplication;
- schema;
- quality measurements;
- known biases;
- versioning;
- dataset card;
- baseline experiment.

---

## P45 · Reproduce and challenge a paper

Select one published claim.

1. reproduce the core experiment;
2. verify the implementation;
3. test sensitivity to seeds/hyperparameters;
4. identify hidden assumptions;
5. attempt one controlled challenge;
6. report whether the original conclusion survives.

A successful reproduction and a well-supported non-reproduction are both legitimate outcomes.

---

## P46 · Efficiency paper

Find a fixed-quality target and minimize one of:
- training compute;
- inference latency;
- GPU memory;
- energy;
- data volume;
- trainable parameters.

The paper must report the quality/resource Pareto frontier, not just one “best” configuration.

---

## P47 · Evaluation/failure-analysis paper

Take an existing model and systematically characterize where it fails.

A strong result can come from discovering a failure mode that existing benchmarks do not expose.

Required:
- failure taxonomy;
- controlled slices;
- baseline comparison;
- statistical uncertainty where appropriate;
- proposed diagnostic;
- mitigation attempt.

---

## P48 · Persian-first foundation-model study

A capstone combining the course's longitudinal Persian track:

**corpus → tokenizer → data quality → mixture → continued pretraining/adaptation → SFT → evaluation → multilingual regression → serving economics.**

The goal is not “train the biggest Persian model.”

The goal is to answer a precise question about how language, data, architecture, training, evaluation, or systems choices affect Persian capability.

---

# 18. A reusable research question generator

When a learner has an idea but no paper yet, use this transformation:

### Task → scientific question

> “I want to fine-tune Qwen.”

becomes:

> “Under a fixed token and GPU budget, how does adapter rank affect Persian instruction-following quality and multilingual regression?”

### Dataset → scientific question

> “I found a Persian dataset.”

becomes:

> “Which measurable corpus-quality properties predict downstream gains per training token?”

### Model → scientific question

> “I want to compare two models.”

becomes:

> “Under equalized inference memory and evaluation coverage, which architectural property explains the observed difference?”

### Application → scientific question

> “I want to build a medical chatbot.”

becomes:

> “Which combination of retrieval, structured tools, and adaptation reduces unsupported answers while preserving task completion under a fixed latency budget?”

The question should identify a **variable, outcome, population/data regime, and comparison**.

---

# 19. The mandatory project card

Every serious project in this repository should eventually have a card containing:

| Field | Required content |
|---|---|
| Problem | What real problem is being studied? |
| Research question | One falsifiable question |
| Hypothesis | What do you expect and why? |
| Prior work | What has already been established? |
| Dataset | Source, version, license/access, schema |
| Data policy | Filtering, deduplication, splits, contamination |
| Baseline | Strong and fair baseline |
| Intervention | Exactly what changes |
| Controls | What stays fixed |
| Metrics | Why each metric answers the question |
| Seeds | Number and rationale |
| Compute | Hardware, time, memory, energy where feasible |
| Cost | Actual or estimated resource cost |
| Ablations | Which component causes the result? |
| Error analysis | Where does the method fail? |
| Statistics | Uncertainty/tests where appropriate |
| Limitations | What the experiment cannot establish |
| Reproduction | Exact command/configuration |
| Artifact | Code, data manifest, model/config, report |
| Conclusion | Claim bounded by evidence |

---

# 20. The experiment ladder

Every project should accumulate artifacts rather than restarting from scratch.

Question
  ↓
Minimal baseline
  ↓
Sanity checks
  ↓
Reference reproduction
  ↓
Controlled intervention
  ↓
Ablation
  ↓
Failure analysis
  ↓
Second dataset / language / model
  ↓
Robustness + uncertainty
  ↓
Paper figures + tables
  ↓
Reproducibility package

A learner should be able to stop at any level and still have a useful artifact.

---

# 21. What counts as a contribution?

A project does **not** need a brand-new neural architecture.

Possible contributions include:

1. **New dataset** — a well-curated resource with measurable value.
2. **New benchmark** — exposes a failure or capability gap.
3. **New analysis** — explains an important phenomenon.
4. **New empirical finding** — a controlled result that changes engineering understanding.
5. **New method** — a technique that improves a meaningful objective.
6. **New evaluation method** — a better way to measure a capability.
7. **New efficiency result** — same quality at lower resource cost.
8. **Reproducibility result** — confirms, qualifies, or challenges a published claim.
9. **Negative result** — a carefully supported intervention that does not work under stated conditions.
10. **Open artifact** — code/data/configuration that enables others to reproduce or extend a finding.

---

# 22. Anti-patterns: projects we deliberately avoid

This repository should not grow by adding another copy of:

- “Train ResNet on CIFAR-10.”
- “Classify cats and dogs.”
- “Train an LSTM on a tiny sentiment dataset.”
- “Run YOLO and report accuracy.”
- “Fine-tune BERT and print F1.”
- “Compare five models and declare the highest score the winner.”

These can be **warm-up implementations** inside a lecture when pedagogically useful.

They become research projects only after the learner introduces a real question, controlled comparison, failure analysis, and evidence.

---

# 23. Research-quality checklist

Before calling a project “research-ready,” ask:

### Question
- Is the question precise?
- Could the experiment falsify the hypothesis?

### Fairness
- Are baselines credible?
- Are training/data/compute budgets comparable?
- Are hyperparameters treated fairly?

### Data
- Can another researcher identify exactly what was used?
- Are source, version, split, licensing/access, and preprocessing recorded?
- Was contamination considered?

### Measurement
- Does the metric answer the question?
- Are important slices reported?
- Are uncertainty and seed variation visible?

### Explanation
- Is there an ablation?
- Is there failure analysis?
- Can the result be explained rather than merely observed?

### Reproducibility
- Can someone clone the repository and reproduce the experiment?
- Are configuration and environment recorded?
- Are expensive steps separated from cheap validation steps?

### Scientific writing
- Are claims narrower than the evidence?
- Are limitations explicit?
- Does the conclusion survive the strongest counterexample you found?

---

# 24. The final student deliverable

A graduating researcher should be able to publish a repository containing:

    project/
    ├── README.md
    ├── research_question.md
    ├── literature/
    ├── data/
    │   └── DATASET_CARD.md
    ├── configs/
    ├── src/
    ├── notebooks/
    ├── experiments/
    ├── results/
    │   ├── tables/
    │   └── figures/
    ├── reports/
    │   └── paper.md
    ├── model_card.md
    ├── reproducibility.md
    └── LICENSE

The final report should contain:

**Abstract → Introduction → Related Work → Research Question → Method → Experimental Setup → Results → Ablations → Error Analysis → Limitations → Conclusion → Reproducibility**

---

# 25. How this connects to the Masterclass

The project catalog is downstream of the course rather than a parallel curriculum:

    Neural Computing
          ↓
    LLM Foundations
          ↓
    Data + Tokenization
          ↓
    Training + Adaptation
          ↓
    Evaluation + Failure Analysis
          ↓
    Systems + Serving
          ↓
    Research Project
          ↓
    Paper / Dataset / Benchmark / Open Artifact

The learner should repeatedly reuse earlier course infrastructure.

For example:

**Tokenizer lecture → Persian tokenizer project → corpus-quality experiment → continued pretraining → Persian evaluation → multilingual regression → paper.**

That is the intended experience: **one research thread grows with the learner.**

---

## 26. Suggested flagship project families

For instructors, cohorts, or independent learners who want a longer research journey, these six families can span much of the Masterclass:

| Family | Starting project | Advanced continuation |
|---|---|---|
| **Language efficiency** | P05 | P06 → P18 → P20 → P24 |
| **Data science for LLMs** | P07 | P08 → P10 → P37 |
| **Efficient adaptation** | P11 | P12 → P19 → P39 → P40 |
| **Evaluation science** | P14 | P15 → P16 → P17 → P47 |
| **Persian / Islamic NLP** | P20 or P27 | P21–P29 → P48 |
| **Systems** | P32 | P33 → P34 → P42 → P46 |

A student can therefore keep one research identity while progressing through increasingly difficult material.

---

## 27. Design principle for future additions

When adding a new project to this catalogue, do **not** ask:

> “What other ML tutorial can we add?”

Ask:

> **“What important question can a learner answer here that they could not answer before taking this course?”**

A new project should connect to an existing lecture, use a real dataset or clearly justified controlled environment, expose a measurable phenomenon, and have a credible path from reproduction to deeper research.

This keeps the catalogue from becoming a giant list while allowing it to grow for years.


# Course 1 quick-start: choose a project in the first week

The full catalogue spans both Course 1 (neural computing) and Course 2 (LLM engineering). For Course 1, begin with one of these **four recommended project families**; the instructor can approve another project if its scope fits the 35-day schedule and available compute.

| Starter | Best for | First deliverable by Day 7 | A sensible extension |
|---|---|---|---|
| **P01 · Learning and generalization** | Understanding what changes as width, depth, data or regularization changes | Matched baseline and a falsifiable hypothesis | Shuffled-label memorization, regularization or multi-seed study |
| **P02 · What makes optimization work?** | Connecting gradients and optimizer behavior to measured convergence | Manual/autograd sanity check and controlled optimizer question | Initialization, learning rate, batch size or gradient instability |
| **P03 · Do representations preserve structure?** | Comparing features and latent representations | A representation metric plus a baseline | Linear probes, neighborhood preservation or nuisance sensitivity |
| **P04 · Does a CNN learn the object or its background?** | Investigating inductive bias and robustness | A data-slice plan and a controlled baseline | Background/texture shifts, augmentation or corruption robustness |

### Scope rules for a 35-day project

1. Choose a question answerable with CPU/Colab or the course's documented resources; a large model is not a prerequisite.
2. Define one primary outcome and one primary intervention before running the final experiment.
3. Establish a baseline before claiming an improvement.
4. Record seeds, versions, data provenance, splits, compute, and known limitations.
5. Include failure analysis. If the hypothesis is not supported, report that honestly.
6. Start a LaTeX paper draft early, but do not confuse a paper-shaped document with a publishable contribution.

The broader 48-project catalogue remains available for independent learners and Course 2. The instructor should explicitly approve projects outside P01–P04 for this short Course 1 cycle.
