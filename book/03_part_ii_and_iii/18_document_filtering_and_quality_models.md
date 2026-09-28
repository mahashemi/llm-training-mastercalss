# Chapter 18 — Document Filtering and Quality Models

**Part:** Part III

## 1. Filtering changes the training distribution

A filter decides which documents survive.

Therefore a filter is not only a data-cleaning step. It changes the probability distribution the model learns from.

For source i:

usable_i = raw_i × survival_rate_i

Track this by language, domain, and source—not only in aggregate.

## 2. Filter categories

| Filter | Goal | Possible mistake |
|---|---|---|
| language ID | select target languages | remove multilingual text |
| quality score | remove low-quality pages | remove valuable niche material |
| length | remove tiny/huge docs | delete useful short facts |
| profanity/safety | reduce problematic data | erase legitimate contexts |
| boilerplate | remove navigation/templates | remove useful structure |
| metadata | exclude restricted sources | incomplete metadata |

## 3. Precision vs recall of a filter

Think of a filter as a classifier.

**Precision:** among removed documents, how many were truly undesirable?

**Recall:** among undesirable documents, how many were removed?

A very aggressive filter may have high recall but poor precision.

## 4. Worked threshold experiment

Suppose a quality classifier produces:

| Threshold | Survival | Estimated noise | Target score |
|---|---:|---:|---:|
| 0.2 | 90% | high | 76 |
| 0.5 | 65% | medium | 79 |
| 0.8 | 35% | low | 77 |

The medium threshold may be promising because aggressive filtering starts removing useful signal.

The actual conclusion requires downstream evaluation.

## 5. Human calibration

Sample documents around the threshold and have experts label:

**keep / remove / uncertain**

Then estimate:

- precision;
- recall;
- disagreement;
- language-specific error.

A filter can have very different accuracy across languages.

## 6. Quality model bias

A classifier trained mostly on English web text can mis-score:

- poetry;
- legal documents;
- religious texts;
- dialectal writing;
- low-resource languages.

Therefore validate the filter on the actual corpus.

## 7. Filtering economics

Suppose 100B raw tokens require expensive processing.

A filter that removes 50% can reduce downstream:

- storage;
- deduplication work;
- tokenization;
- training.

But if it removes high-value data, the apparent compute saving can reduce model quality.

Optimize:

**downstream value per processed token**

not just tokens removed.

## 8. Research exercise

Build a small human-labeled quality set.

Evaluate three thresholds.

Report:

**precision → recall → survival → per-language survival → target score → processing cost**

Then identify the threshold that deserves a larger-scale test.

## Laboratory

[dataset_curation_pipeline.ipynb](../../notebooks/dataset_curation_pipeline.ipynb)

## Reference

https://cs336.stanford.edu/
