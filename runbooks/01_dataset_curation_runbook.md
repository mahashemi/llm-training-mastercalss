# Dataset Curation Runbook

## Objective

Produce a versioned, auditable corpus suitable for a defined language-model experiment.

## Gate 0 — Define the target

Record:
- target model family;
- languages/domains;
- intended capabilities;
- expected training token budget;
- evaluation distribution;
- allowed data sources;
- prohibited/sensitive data.

## Gate 1 — Acquire

For every source record:
| Field | Required |
|---|---|
| source identifier | yes |
| acquisition date | yes |
| provenance/license/access basis | yes |
| language/domain | yes |
| raw-data checksum | recommended |
| processing code version | yes |

## Gate 2 — Normalize

Record encoding/Unicode normalization, HTML extraction, boilerplate removal, document boundaries, metadata preservation, and error handling.

## Gate 3 — Filter

Use layered filters:
1. obvious corruption;
2. language identification;
3. length/format sanity;
4. spam/boilerplate;
5. quality classifiers;
6. domain-specific rules.

Keep a held-out audit sample from every filter stage.

## Gate 4 — Deduplicate

Perform exact dedup first. Add near-dedup for high-impact sources. Measure removal rates by language/domain.

## Gate 5 — Split and contamination control

Build train/validation/test sets before model comparison. Check overlap and benchmark contamination. Prefer temporal or source-held-out tests when they answer the real question better.

## Gate 6 — Mix

Define source weights explicitly. Report both raw corpus composition and effective sampled composition.

## Gate 7 — Release a dataset version

Freeze:
- manifest;
- statistics;
- schema;
- preprocessing code;
- hashes/version IDs;
- known limitations.

## Acceptance criteria

A dataset is not “ready” because it is large. It is ready when its provenance, composition, quality controls, version, and evaluation implications are understood.


## Operational worksheet

Before processing, create a manifest with one row per source:

`source_id, uri/location, acquisition_date, language, domain, rights_basis, raw_checksum, parser_version`

After each transformation, write a new versioned artifact rather than silently overwriting the previous stage.

### Required measurements

| Stage | Documents | Tokens | Languages | Duplicate rate | Rejection rate |
|---|---:|---:|---|---:|---:|
| raw | measure | measure | measure | — | — |
| parsed | measure | measure | measure | measure | measure |
| filtered | measure | measure | measure | measure | measure |
| deduped | measure | measure | measure | measure | measure |
| final sampled | measure | measure | measure | measure | measure |

### Sampling audit

Plot source proportions before and after temperature/mixture sampling. Report whether low-resource sources gained exposure and whether high-resource sources lost too much coverage.

### Quality audit

Keep a fixed audit set across versions. Review both retained and rejected samples. A filter is not validated merely because it removes more content.

### Exit artifact

Produce:

**dataset card + manifest + transformation statistics + rights record + quality audit + contamination report + version ID**

Do not begin expensive training without these artifacts.
