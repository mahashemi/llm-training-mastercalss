# Data Resources

## Start here

- [Real Dataset Registry](REAL_DATASET_REGISTRY.md) — human-readable source catalog.
- [Machine-readable registry](dataset_registry.json) — exact dataset IDs/configs/roles/licenses/access notes.
- [Real Dataset Corpus Bench](../notebooks/real_dataset_corpus_bench.ipynb) — stream/sample multiple real sources and build competing mixtures.
- [Dataset Curation Runbook](../runbooks/01_dataset_curation_runbook.md) — operational acquisition/processing procedure.

## Important rule

Third-party corpora are not copied into this repository. The notebooks acquire small samples or stream from the original host. This keeps the course lightweight and preserves the upstream dataset's licensing/access model.

## Dataset families

Foundation/pretraining candidates: FineWeb, FineWeb-Edu, Dolma, Wikimedia Wikipedia, CulturaX, OpenWebMath.

Instruction/reasoning: Aya Dataset, OpenR1-Math-220k.

Kaggle language/domain examples: Tashkeela Clean Arabic, RUFND Roman-Urdu, Gita Verses.

Every experimental report must record the exact source, configuration/split, version/revision, acquisition date, license/access basis, and preprocessing commit.