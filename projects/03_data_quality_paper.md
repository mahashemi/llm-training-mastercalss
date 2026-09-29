# Project 3 — Data Quality Research Study

## Mission

Test one data intervention while isolating it from architecture and optimizer changes.

## Candidate questions

- Does near-deduplication improve held-out perplexity?
- Does multilingual rebalancing improve low-resource slices?
- Does synthetic-data filtering improve diversity?
- Does a quality threshold remove more useful than harmful data?

## Required design

Define before running:

**hypothesis → independent variable → controlled variables → metric → failure criterion**

Keep architecture and training-token budget approximately fixed.

## Minimum experiment matrix

| Run | Data intervention | Target metric | Regression metric | Resource |
|---|---|---:|---:|---:|
| A | baseline | measure | measure | measure |
| B | intervention | measure | measure | measure |
| C | ablation/control | measure | measure | measure |

## Data accounting

Report raw, filtered, deduplicated, and sampled tokens by source and language.

## Required failure analysis

At least one result must be investigated where the intervention behaved differently from the prediction.

## Deliverables

- dataset card;
- transformation statistics;
- contamination audit;
- experiment card;
- quantitative results;
- figure/table;
- failure analysis;
- reproduction instructions;
- limitations.

## Publication path

Convert the result into a 4–8 page research report with explicit distinction between measured evidence and interpretation.



## Real datasets are mandatory

The study must use at least **three real source families**, not synthetic Python lists.

Recommended combination:

**FineWeb + FineWeb-Edu + Wikipedia/OpenWebMath**, with one multilingual or domain source such as **Aya, Tashkeela, or RUFND**.

### Minimum research design

Run a source-mixture experiment in which total training-token budget is fixed while the source composition changes.

Then run a second experiment changing only one filtering or deduplication variable.

### Required evidence

Include:

- exact dataset IDs and versions;
- acquisition date;
- source licenses/access conditions;
- schema reconciliation;
- raw/sample/usable token accounting;
- per-language statistics;
- cross-source overlap;
- mixture definitions;
- model/evaluation result;
- failure analysis;
- reproduction instructions.
