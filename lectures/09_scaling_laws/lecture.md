# Lecture 09 — Scaling Laws: Spend Compute Where It Buys Information

**Lab:** [Scaling-law Fit](`./lab.ipynb`)  
**Primary anchor:** Chinchilla — https://arxiv.org/abs/2203.15556

## Outcome

You learn to treat model size and training-token budget as coupled variables and to distrust extrapolation outside the measured regime.

## The allocation problem

Suppose you have a fixed compute budget.

Would you train:

- a small model for many tokens;
- a large model for fewer tokens?

There is no answer from parameter count alone.

## Scaling-law intuition

Introduce empirical power-law behavior:

$L(N,D) \approx A N^{-\alpha}+B D^{-\beta}+C$

where N and D represent model/data scale in a simplified teaching formulation.

Explain that scaling laws are empirical approximations over a regime, not laws of nature.

## Compute coupling

For dense-model planning:

**FLOPs ≈ 6ND**

If compute is approximately fixed:

$N \times D \approx \mathrm{constant}$

Increasing N therefore reduces D unless compute grows.

Connect this to undertraining large models and overtraining small models.

## Laboratory

Fit a simple scaling curve from measured or simulated runs.

Then produce:

- loss vs parameters;
- loss vs tokens;
- loss vs compute.

Students must identify whether their extrapolation is inside or outside the observed regime.

## Break it

Remove one data regime or add noisy measurements.

Ask:

> How stable is the extrapolated optimum?

This teaches uncertainty in scaling studies.

## Engineering decision

A useful scaling report contains:

**data range → model range → compute range → fitted relationship → uncertainty → proposed next point**

Do not report a single “optimal” model size without the assumptions behind the fit.

## Exit challenge

If you double model size, what must you ask about the token budget?

## Research bridge

Compare your fitted trend with Chinchilla-style compute-optimal reasoning and identify which parts of your result are empirical measurements versus extrapolation.


## Lab — run it here

**Primary laboratory:** [Open the lab notebook](./lab.ipynb)

The experiment is part of this lecture. Record a baseline, controlled intervention, quantitative result, failure/edge case, resource measurement, interpretation, and next experiment.
