# Lecture 11 — Training System Design and Instrumentation

**Duration:** 25 minutes  
**Lab:** [Training Loop Instrumentation](`./lab.ipynb`)

## Outcome

Students can turn a Python training loop into an observable system and identify whether a failed run is statistical, numerical, or systems-related.

## 0–4 — A training run is a state machine

Draw:

**data → forward → loss → backward → optimizer → checkpoint → evaluate**

Ask:

> If the run crashes at step 48, what state is required to resume correctly?

Not just model weights.

## 4–9 — Training state

A serious checkpoint can require:

- model parameters;
- gradients when needed by the implementation;
- optimizer state;
- scheduler state;
- scaler state if applicable;
- RNG state;
- dataloader position/metadata;
- training step/configuration.

## 9–14 — Observability

Log at minimum:

- loss;
- learning rate;
- gradient norm;
- tokens/sec;
- step time;
- memory;
- data-loader time;
- checkpoint duration;
- validation loss.

Explain why averages can hide pathological spikes.

## 14–19 — Laboratory

Instrument a tiny model.

Produce a table and plot of:

**step → loss → LR → step time → memory**

Then intentionally slow data loading and demonstrate the difference between a GPU bottleneck and an input bottleneck.

## 19–22 — Break it

Interrupt training during a checkpoint and restart.

Ask:

> Which artifacts make the resume trustworthy?

## 22–24 — Engineering decision

Observability is not decoration. It changes what failures can be diagnosed before expensive scaling.

## 24–25 — Exit challenge

Name the three measurements you would require before approving a 100× longer run.

## Research bridge

Compare your checkpoint state with the state required by the chosen training framework and document any assumptions.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
