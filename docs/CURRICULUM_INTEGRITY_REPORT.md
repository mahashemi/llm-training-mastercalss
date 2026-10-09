# Curriculum Integrity Report

Audit date: 2026-09-30

## Resource inventory

| Layer | Count |
|---|---:|
| textbook chapters | 76 |
| numbered lectures | 24 |
| notebooks | 28 |
| runbooks | 14 |
| projects | 4 |
| templates | 10 |

## Integrity checks

- Textbook laboratory references were audited; Chapter 1 now has an immediate Notebook 01 link next to its prediction exercise.
- Shared textbook laboratories are explicitly documented in BOOK_LAB_MAP.md.
- All 24 numbered lectures have explicit notebook links and evidence contracts.
- The 28 notebooks on the audited branch parse as valid JSON.
- Core notebooks now include quantitative experiments and deliberate break cases.
- Runbooks include preflight, resource accounting, smoke tests, recovery, acceptance, and release procedures.
- Projects and templates now require measured baselines, resource metrics, failure analysis, and reproducibility metadata.
- README, INDEX, COURSE_MAP, BOOK_TOC, lecture index, notebook map, and the new Learning Graph were aligned around one practical training spine.
- The real-data layer now includes a Persian longitudinal case with corpus, synthetic-data, evaluation, tokenizer, SFT/PEFT, and continued-pretraining connections.
- The repository does not vendor large Persian corpora; experiments use streamed/sample slices and record source revisions and access/license basis.

## Curriculum invariant

predict → explain → implement → measure → break → diagnose → decide → reproduce

## Practical hardware spine

tiny GPT → Qwen3-0.6B/free Colab → 1.7B/4B single GPU → 7B/8B H100 → Qwen3.8-27B case study → multi-GPU H100 → foundation-model planning

## Maintenance

Model releases, APIs, hardware specifications, pricing, and Colab availability change. Date operational claims and pin exact revisions for experiments.

## Course 1 follow-up verification — 2026-10-09

The 12-chapter Neural Computing course received a focused visual and execution pass.

- Every Course 1 lecture now embeds a chapter-specific static SVG concept diagram and retains its Mermaid mechanism diagram.
- All 12 labs include experiment-derived plotting cells; executed notebooks are uploaded as GitHub Actions artifacts so the resulting figures and outputs can be inspected without committing volatile notebook outputs.
- The full clean-kernel workflow completed successfully for all 12 labs in run [37882928859](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37882928859). The run produced 12 unexpired executed-notebook artifacts.
- The workflow caught and drove fixes for an obsolete Hugging Face dataset loader, a missing `Ridge` import, and invalid artifact naming. Those failures were corrected before the successful run.
- Worked numerical examples were added for convolution, autoencoders, recurrent-state updates, time-series evaluation, SOM updates, VAE/GAN/diffusion objectives, RBM energy, attention, and Bellman updates.
- Duplicate laboratory footer blocks were removed from affected lectures; direct video companions were curated for several core topics.

This execution result verifies that the labs run in the current Python 3.11 GitHub Actions environment. It does not replace pedagogical review of every explanation, nor does one seed establish statistical robustness for any experiment.

The invariant remains:

**predict → explain → implement → measure → break → diagnose → decide → reproduce**
