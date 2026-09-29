# Project 2 — Domain Adaptation With SFT and PEFT

## Mission

Take a real small open-weight model and adapt it to a defined behavior/domain while proving whether the adaptation was useful.

**Recommended classroom model:** Qwen3-0.6B on free Colab.

## Required baselines

1. base model;
2. strongest prompt-only baseline;
3. SFT;
4. LoRA;
5. QLoRA when hardware permits.

## Experimental controls

Keep constant where possible:

- model revision;
- tokenizer;
- dataset split;
- evaluation set;
- generation settings.

Change one major training variable at a time.

## Required measurements

| Dimension | Measure |
|---|---|
| target quality | yes |
| retained capability | yes |
| safety/edge cases | yes |
| trainable parameters | yes |
| peak memory | yes |
| tokens/sec | yes |
| wall time | yes |
| checkpoint/adapter size | yes |

## Required failure analyses

Investigate at least two:

- target improves but general quality falls;
- training loss falls but target quality does not;
- output format improves but factual correctness does not;
- QLoRA saves memory but changes quality/throughput.

## Deliverables

Dataset card, experiment cards, baseline outputs, evaluation scorecard, model/adapter artifact, resource table, failure analysis, and clean-environment reproduction guide.

## Scale extension

Repeat the same experiment with a larger open-weight model on an H100 and explain which conclusions transferred and which did not.
