# Lecture 17 — Multimodality: Turning Images Into Model Inputs

**Lab:** [Multimodal Alignment Map](./lab.ipynb)  
**Primary anchor:** Stanford CS336 — https://cs336.stanford.edu/

## Outcome

You can explain how a non-text modality becomes usable by a language model and calculate the resulting token/resource budget.

## The representation problem

A language model receives token embeddings.

An image is not a token sequence.

Ask:

> What representation must exist before a language model can reason over an image?

Introduce the modality encoder/projector path.

## Typical architecture

Draw:

**image → vision encoder → visual representations → projector/resampler → language-model token space → decoder**

Then compare against:

**text → tokenizer → token embeddings**

The alignment problem is connecting the two representation spaces.

## Token budget is a systems budget

Suppose an image becomes V visual tokens.

For B examples and context length L:

$N_{positions} \approx N_{text} + V$

Increasing visual tokens can affect:

- attention memory;
- context occupancy;
- throughput;
- training cost.

The “resolution setting” is therefore not purely a quality parameter.

## Break it

Use an input whose image encoding consumes most of the context window.

Observe what happens to available textual context.

Then ask whether the failure is:

**representation → context → memory → quality**

## Engineering decision

A multimodal model is a complete system:

**modality encoder + alignment + language model + data + objective + evaluation**

Do not compare multimodal systems on language-model parameter count alone.

## Exit challenge

Explain why “more image tokens” can simultaneously help quality and hurt latency.

## Research bridge

Read one modern vision-language model architecture and identify the encoder, alignment mechanism, language backbone, and training stages.


## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 19 — RL with Verifiable Rewards](../16_reinforcement_learning_with_verifiable_rewards/lecture.md) · [Next: Lecture 21 — Safety, Robustness and Failure Analysis →](../21_safety_robustness_and_failure_analysis/lecture.md)

</div>