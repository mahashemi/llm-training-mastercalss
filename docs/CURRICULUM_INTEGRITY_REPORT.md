# Curriculum Integrity Report

Audit date: 2026-09-29

## Resource inventory

| Layer | Count |
|---|---:|
| textbook chapters | 76 |
| numbered lectures | 24 |
| notebooks | 27 |
| runbooks | 14 |
| projects | 4 |
| templates | 10 |

## Integrity checks

- Textbook laboratory references were audited; Chapter 1 now has an immediate Notebook 01 link next to its prediction exercise.
- Shared textbook laboratories are explicitly documented in BOOK_LAB_MAP.md.
- All 24 numbered lectures have explicit notebook links and evidence contracts.
- The 27 notebooks on the audited branch parse as valid JSON.
- Core notebooks now include quantitative experiments and deliberate break cases.
- Runbooks include preflight, resource accounting, smoke tests, recovery, acceptance, and release procedures.
- Projects and templates now require measured baselines, resource metrics, failure analysis, and reproducibility metadata.
- README, INDEX, COURSE_MAP, BOOK_TOC, lecture index, and notebook map were aligned around one practical training spine.

## Curriculum invariant

predict → explain → implement → measure → break → diagnose → decide → reproduce

## Practical hardware spine

tiny GPT → Qwen3-0.6B/free Colab → 1.7B/4B single GPU → 7B/8B H100 → Qwen3.8-27B case study → multi-GPU H100 → foundation-model planning

## Maintenance

Model releases, APIs, hardware specifications, pricing, and Colab availability change. Date operational claims and pin exact revisions for experiments.