# LLM Trainer Masterclass

## From Deep Learning Engineer to LLM Training Lead

A free-first, implementation-heavy curriculum for learning how to design, train, evaluate, optimize, deploy, and manage large language models.

**Audience:** high-school graduates, engineers, researchers, and organizations. The course begins from intuition and builds toward systems engineering, research, economics, and national-scale model planning.

## North-star outcome

A graduate of this curriculum should be able to:

- explain a language model from tokens to distributed training;
- build a tiny GPT from scratch and understand every major tensor operation;
- construct and audit a pretraining dataset;
- select between prompting, RAG, tool use, SFT, LoRA, QLoRA, continued pretraining, preference optimization, distillation, or training from scratch;
- estimate model/data/compute requirements and turn them into a resource proposal;
- run reproducible experiments and generate paper-ready tables and figures;
- design evaluation suites before training rather than after;
- diagnose training failures and scaling bottlenecks;
- design a multilingual/national-language data and model program;
- produce a technical + organizational + funding proposal for an LLM initiative.

## Learning engine

Every lesson follows:

**Intuition → visual → mathematics → code → systems → experiment → failure analysis → decision → research question**

Every important concept is taught twice: once for understanding and once for engineering judgment.

## Free-first rule

Practical labs target free Google Colab or CPU fallbacks whenever possible. Colab's free tier provides access to compute resources, including GPUs/TPUs, but availability and limits are dynamic and not guaranteed. Therefore no lab assumes a particular accelerator will always be available.

For large-scale training, the course uses small reproducible runs to teach the method and then converts the same experiment into a scaling proposal with explicit assumptions.

## Repository architecture

- `book/` — textbook chapters and long-form explanations
- `lectures/` — 25-minute lecture scripts and slide plans
- `notebooks/` — executable Colab-first laboratories
- `runbooks/` — operational procedures
- `visuals/` — diagrams and visual teaching assets
- `videos/` — curated public lectures with timestamps, purpose, and critical questions
- `papers/` — paper-reading guides and reproduction plans
- `cheat_sheets/` — compact references
- `projects/` — graded and capstone projects
- `templates/` — experiment cards, paper reports, technical proposals, funding proposals
- `references/` — canonical sources and citations

## Research philosophy

The course treats model training as an experimental science and an engineering discipline. Claims are tied to evidence, configurations are recorded, and every major result is accompanied by a failure analysis and a reproducibility checklist.

## Canonical external foundations

- Stanford CS336, *Language Modeling from Scratch* — full lifecycle: data, architecture, training, evaluation, deployment.
- Andrej Karpathy, *Let's build GPT* and *Let's reproduce GPT-2* — highly practical implementation walkthroughs.
- 3Blue1Brown, attention/transformer visual explanations — mathematical intuition.
- Sebastian Raschka, end-to-end LLM coding workshop — from tokenizer and architecture to pretraining and instruction tuning.
- OLMo / OLMo 2 — open model lifecycle, training data, code, evaluation, and reproducible artifacts.
- Llama 3 technical report — case study in modern large-scale training.
- BLOOM — case study in multilingual, collaborative, large-scale training.
- Dolma / FineWeb / DataComp-LM — case studies in data curation.


## Open research and development resource

This repository is intended to be a living, citable knowledge base for LLM engineering. It is designed for teaching, experimentation, research reproduction, technical planning, and real-world model-development programs.

Readers are encouraged to explore the material, reproduce experiments, report failures, propose corrections, add new experiments, translate explanations, and contribute improved teaching material.

The project values scientific traceability: important claims should point to evidence; experimental results should include configurations and limitations; changing recommendations should be dated; and historical releases should remain referenceable.

## How to cite

Use the repository's CITATION.cff metadata and cite a release or commit when possible. For research claims, cite the underlying primary paper as well as the relevant repository material when both contributed to the work.

## Quality bar

The target is not simply a large collection of tutorials. The target is a durable engineering curriculum in which a learner can progress from intuition to implementation, from implementation to controlled experimentation, and from experimentation to resource planning and organizational decision-making.

The project explicitly aims to teach learners how to build evidence for a model proposal: mission, users, data, architecture, training method, compute, people, evaluation, safety, deployment, budget, milestones, risks, and measurable outcomes.

## Project status

The curriculum is under active development. The field changes quickly, so material may be revised as new papers, models, datasets, training techniques, hardware, and evaluation practices become available. Substantive updates should be recorded in the changelog and associated with a release or commit whenever practical.

## Open licensing

Original educational material is intended to be shared under CC BY 4.0, while source code and code examples are intended to be shared under the MIT License. Third-party material remains under its original terms. See LICENSE.md and LICENSE-CODE.

## Repository health

The project includes contribution guidelines, a code of conduct, security guidance, issue templates, code ownership, a reproducibility standard, maintenance policy, and release checklist. These are designed to keep the repository useful as a living research and engineering reference.

## Current build status

The repository currently contains:

- 24 lecture packages;
- 75 textbook chapters plus chapter template;
- 26 notebooks including orientation, one lab per numbered lecture, and the end-to-end tiny-GPT pretraining campaign;
+ 11 operational runbooks;
- 4 capstone/project briefs;
- research, proposal, model-card, dataset-card, and experiment templates;
- curated lecture/video and paper-reading paths;
- citation, reproducibility, maintenance, governance, security, and contribution standards.

Use `START_HERE.md` for the learner path, `COURSE_MAP.md` for the curriculum map, `BOOK_TOC.md` for the textbook, and `notebooks/README.md` for the Colab laboratory map.

## Mastery standard

Completing a notebook is not mastery. A learner graduates from each major stage only after producing evidence:

**understand → implement → measure → break → explain → decide → reproduce**.

The final standard is the Model Program Dossier in `projects/04_llm_program_dossier.md`.
