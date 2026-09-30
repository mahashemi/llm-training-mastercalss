# Persian Dataset Track

Persian is a **longitudinal case study** in the LLM Trainer Masterclass, not merely an extra dataset in the registry.

The track deliberately separates three things that are easy to confuse:
1. **a Persian model** — e.g. IbnSina-1.5B;
2. **a large Persian corpus** — e.g. Naab, CulturaX-fa, FineWeb2-HQ-fa;
3. **a Persian evaluation/instruction dataset** — e.g. PersianMedQA, ParsiNLU, synthetic-persian-v1.

## 1. The anchor resources

| Resource | Type | Scale / current card | Role in the course | Access / license note |
|---|---|---|---|---|
| [IbnSina-1.5B](https://huggingface.co/ibnsina-llm/ibnsina-1.5b) | Model | 1.48B parameters; 46B training tokens according to the model card | Persian-first model case study; tokenizer, training recipe, evaluation, serving | Apache-2.0 model/code; training-source terms vary |
| [IbnSina Synthetic Persian v1](https://huggingface.co/datasets/ibnsina-llm/synthetic-persian-v1) | Dataset | 883k documents; 2.075B tokens | synthetic-data quality, filtering, decontamination, reasoning/STEM supplementation | Apache-2.0 |
| [SLPL/naab](https://huggingface.co/datasets/SLPL/naab) | Dataset | ~130GB; ~250M paragraphs; ~15B words | large cleaned Persian corpus; corpus engineering and streaming | inspect current dataset/source terms |
| [uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX) — fa | Dataset | 59.5M docs; 45.95B tokens in the published language table | multilingual-to-Persian scale comparison | gated; underlying mC4/OSCAR terms apply |
| [epfml/FineWeb2-HQ](https://huggingface.co/datasets/epfml/FineWeb2-HQ) — fas_Arab | Dataset | 5.1M docs; 69GB in current card | quality-filtered Persian web comparison | inspect current upstream terms |
| [Persian Corpus (Merged)](https://huggingface.co/datasets/PersianML/persian-text-corpus) | Dataset | 14.7M rows; ~5.1B tokens | convenient multi-source Persian corpus; aggregation/provenance audit | MIT on the published card; inspect component provenance |
| [TLPC](https://huggingface.co/datasets/Targoman/TLPC) | Dataset | >75M docs; >41B tokens according to the card | scale/provenance case study; compare corpus claims and licensing | inspect source terms carefully |
| [PersianMedQA](https://huggingface.co/datasets/MohammadJRanjbar/PersianMedQA) | Evaluation dataset | 20,785 items; 23 medical specialties | Persian evaluation, bilingual evaluation, contamination discipline | gated; non-commercial academic research per card |
| [ParsiNLU](https://huggingface.co/datasets/persiannlp) | Evaluation/task family | multiple Persian NLU tasks | multilingual evaluation and task-specific adaptation | licenses vary by subset |
| [Persian space/ZWNJ correction](https://huggingface.co/datasets/PerSpaCor/bijankhan-peykare-annotated) | Dataset | 424,181 annotated examples | Persian normalization, ZWNJ, tokenization preprocessing | inspect current card |

## Important naming correction

The **“1.5B” you remembered is IbnSina-1.5B, a model**, not a 1.5-billion-token Persian dataset. Its model card reports 1.48B parameters and 46B training tokens. The separate IbnSina synthetic corpus is 2.075B tokens. The larger Persian corpus candidates above are much larger.

## 2. Why multiple Persian corpora?

Do not simply pick the largest number.

| Question | Candidate evidence |
|---|---|
| How much Persian web data exists? | CulturaX-fa, FineWeb2-HQ-fa, Naab, TLPC |
| How much is actually usable after quality filtering? | Naab / FineWeb2-HQ / CulturaX methodology |
| Does a merged corpus preserve provenance? | Persian Corpus (Merged) |
| Can synthetic data fill sparse STEM/medical/reasoning domains? | IbnSina Synthetic Persian v1 |
| Does synthetic data introduce stylistic/teacher artifacts? | synthetic-vs-real ablation |
| Does Persian tokenization waste sequence budget? | CulturaX-fa / Naab samples + tokenizer lab |
| Does Persian adaptation improve without damaging English/multilingual capability? | bilingual regression evaluation |
| Can we evaluate Persian capability independently of training data? | PersianMedQA / ParsiNLU and held-out custom sets |

## 3. Longitudinal labs using existing notebooks

We do **not** create a new notebook for every Persian dataset.

### Lab A — Persian tokenizer audit

Use:
- `notebooks/tokenizer_design_and_measurement.ipynb`
- `notebooks/open_weight_model_audit.ipynb`

Compare Persian against English and at least one additional language.
Measure characters/token, words/token, tokens/word, sequence expansion, ZWNJ/spacing behavior, and Arabic/Persian Unicode variants.

### Lab B — Persian corpus audit

Use:
- `notebooks/real_dataset_corpus_bench.ipynb`
- `notebooks/dataset_curation_pipeline.ipynb`
- `notebooks/dedup_and_data_mixing.ipynb`

At minimum compare small/streamed samples from Naab, CulturaX-fa, FineWeb2-HQ-fas_Arab, IbnSina Synthetic Persian v1, and one merged corpus.

Record: **source → revision → sample → schema → language → quality → duplicates → license/access → mixture weight.**

### Lab C — Real vs synthetic Persian

Hold model, tokenizer, token budget, and training procedure fixed.

Compare real-only Persian, synthetic-only Persian, and real + synthetic.

Measure held-out perplexity, Persian task performance, domain slices, contamination, repetition/style, and English/multilingual regression.

The conclusion must be evidence-based; the synthetic corpus is described by its authors as a supplement rather than a replacement for real Persian text.

### Lab D — Persian SFT / PEFT

Use the existing SFT, LoRA/QLoRA, and full-FT notebooks.
Keep the training budget fixed while comparing **SFT → LoRA → QLoRA → full FT** and evaluate both target Persian capability and retained general/multilingual capability.

### Lab E — Persian evaluation

Use ParsiNLU task subsets, PersianMedQA where access is appropriate, and held-out custom Persian evaluation data.
Never train on the evaluation split.

For each benchmark record: **dataset revision → split → prompt/template → decoding → metric → uncertainty → contamination status.**

## 4. Persian capstone question

> **Given a fixed compute budget, what combination of real Persian data, synthetic Persian data, tokenizer/model choice, continued pretraining, and PEFT produces the most defensible capability improvement without unacceptable regression or data-governance risk?**

This turns Persian into a complete miniature version of the entire LLM training program:

**data → tokenizer → training → adaptation → evaluation → serving → economics → program design**

## 5. Data-governance rule

Large Persian web corpora are not automatically interchangeable merely because their Hugging Face cards are downloadable.

For every source, students must distinguish hosting/access terms, dataset license, underlying-source terms, personal/sensitive-information risk, commercial-use restrictions, redistribution rights, and evaluation-only versus training suitability.

The repository stores **metadata and experiment manifests**, not multi-terabyte corpora.

## 6. Reproducibility record

```yaml
dataset:
  name:
  host:
  config:
  split:
  revision:
  acquired_at:
  license:
  access_basis:
  source_terms:

sampling:
  rows:
  token_budget:
  seed:
  language_mix:

processing:
  normalization:
  filtering:
  deduplication:
  tokenizer:

training:
  model:
  objective:
  sequence_length:
  steps:
  effective_tokens:

evaluation:
  benchmarks:
  split:
  prompt_template:
  decoding:
  contamination_check:

artifact:
  experiment_card:
  metrics:
  failures:
  decision:
```