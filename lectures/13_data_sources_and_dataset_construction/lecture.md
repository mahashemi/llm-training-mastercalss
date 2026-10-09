# Lecture 13 — Data Sources and Dataset Construction

**Lab:** [Dataset Curation Pipeline](./lab.ipynb)

## Outcome

You learn to treat a dataset as an engineered artifact with provenance, transformations, rights, composition, and measurable quality.

## First principle: the training objective determines the schema

There is no single row format that is ideal for every stage. Keep two layers separate:

1. **Canonical analysis record:** a source-independent record for inspection, filtering, deduplication, statistics, provenance, and splitting.
2. **Objective-specific training example:** the exact structure consumed by the training objective.

A useful analysis record keeps, at minimum:

```json
{
  "record_id": "stable-source-id",
  "source_id": "wiki-en",
  "source_revision": "snapshot-or-date",
  "language": "en",
  "content_type": "document",
  "text": "The original normalized text...",
  "license_or_access_basis": "recorded separately; never guessed",
  "quality_flags": [],
  "split_group_id": "document-or-near-duplicate-cluster",
  "metadata": {}
}
```

Use stable IDs and retain a pointer to the source record. Keep raw text and normalized text distinguishable so a transformation can be reproduced. Do not silently drop the source, license/access basis, language, or processing version when exporting a training file.

## Which examples does each training method need?

### 1. Causal language-model pretraining: usually no human-written Q&A

For ordinary next-token pretraining, a document is enough. The tokenizer turns it into tokens, and the training pipeline creates shifted targets: the model sees a prefix and learns to predict the next token. The labels are generated automatically from the text.

For tokens (x_1, x_2, \ldots, x_T), the model learns to predict (x_{t+1}) from the preceding tokens. Human annotation is not required for this objective, but source curation, deduplication, language balance, contamination checks, and rights review still matter.

### 2. Supervised fine-tuning (SFT): prompt/context plus a desired response

A chat-style example can use a messages array:

```json
{"messages":[
  {"role":"user","content":"Explain gradient descent in one sentence."},
  {"role":"assistant","content":"Gradient descent updates parameters to reduce a loss."}
]}
```

Training usually masks the loss on user/system context and computes it on the intended assistant target, according to the trainer's configuration. Verify the actual loss mask: merely placing messages in JSON does not guarantee the correct tokens are supervised.

The target may be written by an expert, carefully selected from existing responses, or generated synthetically and then filtered/reviewed. Synthetic does not automatically mean correct.

### 3. Preference optimization: two candidate responses and a comparison

```json
{"prompt":"Explain gradient descent simply.",
 "chosen":"It adjusts parameters to reduce prediction error.",
 "rejected":"It randomly changes every parameter without using a loss."}
```

The label says which response is preferred for this prompt; it does not necessarily prove the chosen response is factually correct. Record who or what produced the comparison, the rubric, confidence or adjudication status where available, and the reason for the preference.

### 4. Other objectives need their own targets

- **Classification/routing:** input plus a defined label set and label provenance.
- **Tool use:** structured assistant tool-call messages, tool name/arguments, tool result, and the expected continuation; validate arguments against the tool schema.
- **Math/reasoning SFT:** problem plus the target answer and any reasoning traces that are deliberately part of the training target. Do not assume every available trace is correct or that exposing it is always desirable.
- **Multimodal:** message content plus media references and modality-specific metadata (for example, image/video references, timestamps, audio segments, and text alignment). Preserve licensing and consent constraints for media too.

**Decision rule:** if the objective supplies its own target automatically (such as next-token prediction), human labels may be unnecessary. If the model must learn a desired action, category, response, ranking, or structured behavior, you need a defensible target or comparison signal. Annotation is a quality-control process, not a mandatory column added to every dataset.

## Split before fitting or tuning

Create train/validation/test partitions by document, source group, conversation, user or near-duplicate cluster as appropriate—not by randomly splitting overlapping chunks from the same source. Fit learned filters and tune thresholds on training/validation data, and protect the final test set. For benchmark-like tasks, also check temporal and benchmark contamination.


## Same source, different corpus

Start with a web crawl.

Ask:

> Is the raw crawl the training set?

No. Parsing, filtering, deduplication, language identification, rights review, and sampling transform it.

## Source inventory

For each source record:

- source ID;
- acquisition date;
- language/domain;
- provenance;
- rights basis;
- raw size;
- processing version.

## Transformation accounting

Example:

**20B raw → 12B after filtering → 9B after dedup → 7B after final selection**

The learner must be able to explain every reduction.

## Break it

Introduce a filter that removes one target language disproportionately.

Detect the failure with per-language accounting.

## Engineering decision

Dataset readiness means:

**provenance + rights + quality + distribution + version + evaluation implications**

not “we have many tokens.”

## Exit challenge

What is the smallest metadata set you need to reproduce the exact corpus?

## Research bridge

Use current data-processing documentation from the referenced implementation ecosystem and compare it with the simplified classroom pipeline.



## Required real-data laboratory

Do not substitute the four-row toy dataset for the real exercise. Run the [Real Dataset Corpus Bench](./lab.ipynb).

You must inspect multiple source schemas, normalize them into a common schema, measure distributions, run filtering, check cross-source exact duplicates, and construct two competing mixtures.

Minimum sources:

- FineWeb
- FineWeb-Edu
- Wikipedia
- OpenWebMath
- Aya

Then inspect one Kaggle source such as Tashkeela or RUFND.

### Evidence

Produce:

**source registry + schema map + source statistics + filter survival + dedup report + mixture A/B + downstream hypothesis**.


## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 05 — Attention Alternatives and MoE](../05_attention_alternatives_and_moe/lecture.md) · [Next: Lecture 07 — Filtering, Deduplication, Mixing and Synthetic Data →](../14_filtering_deduplication_mixing_and_synthetic_data/lecture.md)

</div>
## Video companions

[Video companions: LLM dataset construction](https://www.youtube.com/results?search_query=LLM+dataset+construction+data+curation+lecture)

## Navigation

[← Previous](../12_evaluation/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../14_filtering_deduplication_mixing_and_synthetic_data/lecture.md)
