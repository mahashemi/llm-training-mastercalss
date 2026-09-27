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
