# Lecture 17 — Multimodality: Turning Images Into Model Inputs

**Duration:** 25 minutes  
**Lab:** [Multimodal Alignment Map](`./lab.ipynb`)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

Students can explain how a non-text modality becomes usable by a language model and calculate the resulting token/resource budget.

## 0–4 — The representation problem

A language model receives token embeddings.

An image is not a token sequence.

Ask:

> What representation must exist before a language model can reason over an image?

Introduce the modality encoder/projector path.

## 4–9 — Typical architecture

Draw:

**image → vision encoder → visual representations → projector/resampler → language-model token space → decoder**

Then compare against:

**text → tokenizer → token embeddings**

The alignment problem is connecting the two representation spaces.

## 9–14 — Token budget is a systems budget

Suppose an image becomes V visual tokens.

For B examples and context length L:

total positions ≈ text tokens + V

Increasing visual tokens can affect:

- attention memory;
- context occupancy;
- throughput;
- training cost.

The “resolution setting” is therefore not purely a quality parameter.

## 14–19 — Laboratory

Build a small model-flow map and vary visual token count.

Record:

| Visual tokens | total context | estimated attention memory | observed runtime |
|---:|---:|---:|---:|
| low | measure | measure | measure |
| medium | measure | measure | measure |
| high | measure | measure | measure |

## 19–22 — Break it

Use an input whose image encoding consumes most of the context window.

Observe what happens to available textual context.

Then ask whether the failure is:

**representation → context → memory → quality**

## 22–24 — Engineering decision

A multimodal model is a complete system:

**modality encoder + alignment + language model + data + objective + evaluation**

Do not compare multimodal systems on language-model parameter count alone.

## 24–25 — Exit challenge

Explain why “more image tokens” can simultaneously help quality and hurt latency.

## Research bridge

Read one modern vision-language model architecture and identify the encoder, alignment mechanism, language backbone, and training stages.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
