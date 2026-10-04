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



## Start with alignment, not “more modalities”

Suppose an image encoder produces

$$
V\in\mathbb{R}^{N_v\times d_v}
$$

while a language model expects embeddings of width $d_t$.

A multimodal system needs a mechanism that maps or aligns these representations:

$$
Z=V W,\qquad W\in\mathbb{R}^{d_v\times d_t}.
$$

Now image information can enter the language model's representation space.

This tiny equation captures a major engineering issue: different modalities have different information structures, scales, and tokenization schemes.

## Three common design patterns

| Pattern | Main idea | Trade-off |
|---|---|---|
| encoder + projector | encode modality, map into LM space | simple, limited interaction |
| cross-attention | LM attends to modality features | richer interaction, more compute |
| unified token space | represent multiple modalities as tokens | elegant interface, expensive token budgets |

The architecture should follow the task rather than the desire to call a model “multimodal.”

## A concrete failure case

Ask an image-language model:

> “What is the text on this small sign?”

Failure may come from:

- image resolution;
- visual encoder capacity;
- projection/alignment;
- OCR difficulty;
- language decoding;
- insufficient training examples.

The final wrong answer does not identify which subsystem failed.

## Real-world connection

Multimodal systems make the token-budget problem more complicated. A video can contain many frames, each containing many visual tokens.

Therefore a production design must reason about:

**quality → visual/audio tokens → memory → latency → cost**

not merely whether the model can accept an image.

## Research extension

Hold the language model fixed and vary only visual resolution or frame sampling. Measure task quality, token count, latency, and cost. This creates a controlled study of the quality-efficiency frontier.

## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 19 — RL with Verifiable Rewards](../16_reinforcement_learning_with_verifiable_rewards/lecture.md) · [Next: Lecture 21 — Safety, Robustness and Failure Analysis →](../21_safety_robustness_and_failure_analysis/lecture.md)

</div>
## Video companions

[Video companions: multimodal language models](https://www.youtube.com/results?search_query=multimodal+language+models+vision+language+lecture)

## Navigation

[← Previous](../16_reinforcement_learning_with_verifiable_rewards/lecture.md) · [Course 2 home](../../courses/02_llm_engineering_and_training/README.md) · [Next →](../18_lora_qlora_and_peft/lecture.md)
