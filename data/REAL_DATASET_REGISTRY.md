# Real Dataset Registry

**Audit date:** 2026-09-30

This is the concrete dataset layer for the LLM Trainer Masterclass. The repository does not vendor multi-terabyte datasets. Students stream or sample them from the original host, record the exact dataset revision/version, and build a local experiment artifact.

## Tier A — Foundation/pretraining corpus candidates

| Dataset | Host / exact ID | Language(s) | Approx. scale | Key fields | License / access | Classroom role |
|---|---|---|---|---|---|---|
| FineWeb | [HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) | English | >18.5T tokens | text, url, metadata | ODC-BY 1.0; review upstream terms | general web baseline |
| FineWeb-Edu | [HuggingFaceFW/fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) | English | 1.3T tokens (v1) | text + source metadata | ODC-BY | quality-filtered educational web |
| Dolma | [allenai/dolma](https://huggingface.co/datasets/allenai/dolma) | English | v1.7: 4.5 TB gzip | text + source/provenance metadata | ODC-BY | open-model corpus design |
| CulturaX | [uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX) | 167 languages | 6.3T tokens | text + language/source information | gated; accept current HF access conditions | multilingual corpus case study |
| Wikipedia | [wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia) | 300+ language subsets | millions of articles | id, url, title, text | CC BY-SA 3.0 / GFDL | reference corpus |
| OpenWebMath | [open-web-math/open-web-math](https://huggingface.co/datasets/open-web-math/open-web-math) | English | 6.3M docs / 14.7B tokens | text, url, date, metadata | ODC-BY; also Common Crawl ToU | math corpus |

The FineWeb and FineWeb-Edu repositories expose smaller sample configurations such as 10BT/100BT/350BT, which are useful for classroom streaming experiments rather than downloading full corpora.

## Tier A-P — Persian-first corpus, synthetic data, and evaluation

Persian is a first-class longitudinal case study. Do not confuse the **IbnSina-1.5B model** with a dataset: the model has 1.48B parameters, while its public model card reports 46B training tokens. The separate IbnSina synthetic corpus contains 2.075B tokens.

| Dataset / model | Host / exact ID | Approx. scale | Key role | License / access |
|---|---|---:|---|---|
| IbnSina-1.5B | [Hugging Face model](https://huggingface.co/ibnsina-llm/ibnsina-1.5b) | 1.48B parameters; 46B training tokens reported by model card | Persian-first model case study; tokenizer, training mix, SFT, serving | Apache-2.0 model/code; source terms vary |
| IbnSina Synthetic Persian v1 | [ibnsina-llm/synthetic-persian-v1](https://huggingface.co/datasets/ibnsina-llm/synthetic-persian-v1) | 883k docs / 2.075B tokens | synthetic-data filtering, decontamination, reasoning/STEM supplementation | Apache-2.0 |
| Naab | [SLPL/naab](https://huggingface.co/datasets/SLPL/naab) | ~130GB / ~250M paragraphs / ~15B words | large cleaned Persian corpus; streaming and corpus engineering | review current dataset/source terms |
| CulturaX — Persian | [uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX), config `fa` | 59.5M docs / 45.95B tokens | multilingual-to-Persian scale comparison | gated; mC4/OSCAR terms apply |
| FineWeb2-HQ — Persian | [epfml/FineWeb2-HQ](https://huggingface.co/datasets/epfml/FineWeb2-HQ), subset `fas_Arab` | 5.1M docs / 69GB | high-quality Persian web comparison | review current upstream terms |
| Persian Corpus (Merged) | [PersianML/persian-text-corpus](https://huggingface.co/datasets/PersianML/persian-text-corpus) | 14.7M rows / ~5.1B tokens | multi-source aggregation and provenance audit | MIT on card; inspect component provenance |
| Targoman Large Persian Corpus | [Targoman/TLPC](https://huggingface.co/datasets/Targoman/TLPC) | >75M docs / >41B tokens claimed by card | corpus-scale/provenance case study | review source terms carefully |
| PersianMedQA | [MohammadJRanjbar/PersianMedQA](https://huggingface.co/datasets/MohammadJRanjbar/PersianMedQA) | 20,785 items / 23 specialties | Persian bilingual medical evaluation | gated; non-commercial academic research per card |
| ParsiNLU | [persiannlp datasets](https://huggingface.co/datasets/persiannlp) | multiple task-specific datasets | Persian NLU evaluation | license varies by subset |
| PerSpaCor | [PerSpaCor/bijankhan-peykare-annotated](https://huggingface.co/datasets/PerSpaCor/bijankhan-peykare-annotated) | 424,181 examples | Persian spacing/ZWNJ normalization | review current dataset card |

**Why this matters:** the largest raw corpus is not automatically the best training corpus. Students compare scale, quality, provenance, token efficiency, license/access, domain coverage, and evaluation contamination.

## Tier B — Multilingual instruction / reasoning

| Dataset | Host / exact ID | Scale | Key fields | License | Classroom role |
|---|---|---:|---|---|---|
| Aya Dataset | [CohereLabs/aya_dataset](https://huggingface.co/datasets/CohereLabs/aya_dataset) | 204k human-annotated prompt/completion pairs | inputs, targets, language, language_code, annotation_type, user_id | Apache 2.0 | multilingual SFT |
| OpenR1-Math-220k | [open-r1/OpenR1-Math-220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k) | default ~94k; extended ~131k; multi-trace corpus | problem, solution, answer, source, correctness fields, messages | Apache 2.0 | reasoning/SFT/rejection-sampling |

## Tier C — Kaggle domain/language datasets

These are deliberately included because a real data engineer should be able to work across both Hugging Face and Kaggle.

| Dataset | Kaggle link | Scale / structure | License | Classroom role |
|---|---|---|---|---|
| Tashkeela Clean Arabic Diacritized Corpus | [Kaggle](https://www.kaggle.com/datasets/ahmedmohsen2002/tashkeela-clean-arabic-diacritized-corpus) | ~2.6M sentences; MSA + Classical Arabic; train/validation/test | GPL-2.0 | Arabic normalization/tokenization |
| RUFND Cleaned test/train | [Kaggle](https://www.kaggle.com/datasets/zainabnoor02/rufnd-cleaned-testtrain-data-files) | 3,500 Roman-Urdu news items; 2,450 train / 1,050 test | CC BY 4.0 | Roman-Urdu domain/data-quality study |
| Gita Verses | [Kaggle](https://www.kaggle.com/datasets/ashishk1331/gita-verses) | Sanskrit + Hindi + English text files | Community Data License Agreement — Sharing v1.0 | multilingual alignment/domain corpus study |

## Why the registry contains different dataset types

### General web
FineWeb / Dolma are used for source mixture, filtering, deduplication, token-budget allocation, and temporal/source analysis.

### Educational
FineWeb-Edu is used for quality-model experiments, synthetic-label effects, and quality-versus-coverage trade-offs.

### Reference
Wikipedia is used for high-authority text, multilingual comparisons, temporal snapshots, and contamination exercises.

### Specialized
OpenWebMath is used for domain-mixture experiments and math capability enrichment.

### Multilingual web
CulturaX is used for language balancing, target-language fertility, low-resource exposure, and gated-data governance.

### Instruction
Aya is used for SFT, multilingual behavior, instruction-data coverage, and annotation-quality analysis.

### Reasoning
OpenR1-Math-220k is used for reasoning SFT, verified versus unverified traces, preference construction, rejection sampling, and verifier concepts.

### Kaggle language/domain sources
Tashkeela, RUFND, and Gita are used for second-platform acquisition, schema reconciliation, license recording, language/script normalization, and small domain-specific experiments.

## Acquisition rule

Do not use a dataset only as `load_dataset('name')` and then forget where it came from.

Every experiment records:

host → dataset ID → config/subset → split → revision/version → acquisition date → license/access basis → preprocessing commit

## First classroom corpus

## Persian classroom path

The Persian track is intentionally longitudinal rather than a new notebook family. Use the existing tokenizer, real-dataset, curation, deduplication, SFT/PEFT, and evaluation notebooks.

See **[Persian Dataset Track](PERSIAN_DATASET_TRACK.md)** for the exact progression and reproducibility record.

The recommended first real corpus is intentionally small:

| Source | Role | Example training allocation |
|---|---|---:|
| FineWeb sample | general | 50% |
| FineWeb-Edu sample | educational | 20% |
| Wikipedia language slices | reference/multilingual | 10% |
| OpenWebMath sample | technical/math | 10% |
| Aya language slices | instruction | 10% |

This mixture is not a universal training recipe. It is a controlled classroom mixture for teaching source weighting. Students must compare it with at least one alternative mixture.

## Important licensing note

A hosting license does not automatically remove rights attached to underlying documents. Review the dataset card and source terms before operational use. OpenWebMath explicitly notes Common Crawl terms; CulturaX is gated; Wikipedia carries its stated Wikimedia licensing.

## Source facts

Dataset facts in this registry were checked against the dataset cards/pages available on 2026-09-29. Re-check them before operational use.