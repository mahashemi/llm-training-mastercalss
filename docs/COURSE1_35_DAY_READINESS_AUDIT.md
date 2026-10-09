# Course 1 — 35-Day Instructor-Readiness Audit

Audit date: 2026-10-09

## Purpose and scope

The 35-day plan promises 70 contact hours. This document connects that plan to the 12 existing lecture/lab chapters and records the next substantive teaching improvements. It is an **actionable preliminary content audit**, not a claim that all 35 sessions have already passed instructor-readiness review.

The clean-kernel execution gate is green for all 12 lab notebooks in [workflow run 37882928859](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37882928859). That proves the notebooks execute in the tested environment; it does not prove that every promised concept is explained deeply enough for a beginner or that each comparison is statistically robust.

## Priority key

- **P0 — correctness/access:** broken navigation, rendering, or executable failure.
- **P1 — teaching completeness:** the 35-day plan promises a mechanism that the chapter only names or sketches.
- **P2 — evidence quality:** strengthen controls, repeated runs, uncertainty, or interpretation.

## Chapter-to-session audit

| Days | Chapter | Existing evidence and next teaching gate | Priority |
|---|---|---|---|
| 1–2 | 01 Neural computation | The chapter explicitly teaches weights, bias, perceptron/Adaline, loss, gradient, learning rate, and numerical updates. Next: verify the notebook's answer key and the comparison of hard perceptron decisions against Adaline's continuous score. | P2 |
| 3–5 | 02 Feedforward + backprop | The chapter includes a numerical forward pass, chain-rule path, gradient descent, mini-batches, gradient checking, and generalization. Next: make the Day 5 optimizer/initialization/normalization/regularization comparisons explicit and ensure each is paired with a controlled experiment rather than a glossary. | P1 |
| 6–8 | 03 Competitive learning + SOM | Winner selection and a numerical BMU/neighborhood update are explained. The lecture now explains variant-specific Evolving SOM growth/pruning and fair baselines. The lab now includes a minimal growing 1-D SOM variant, held-out quantization error, and unit-count comparison. Remaining gate: repeat across seeds and add topology-preservation evidence before drawing general conclusions. | P1 |
| 9–12 | 04 CNNs | Convolution, output shape, parameter sharing, residual correction, and dense connectivity are explained with a hand-computed example. Next: explicitly teach gradient-flow/degradation motivation for residual blocks and make the plain-vs-residual-vs-dense comparison budget-matched and interpretable. | P1 |
| 13–15 | 05 Autoencoders | Encoder/decoder, reconstruction loss, denoising target, bottleneck trade-offs, and the difference between reconstruction quality and downstream representation quality are covered. Next: provide a concrete sparse/contractive objective example and a reproducible frozen-encoder/linear-probe protocol. | P1 |
| 16–19 | 06 Generative models | VAE, GAN, and diffusion objectives and failure modes are introduced; the lab visualizes their distinct mechanisms. Next: add a worked numeric interpretation for each objective and explicitly separate sample quality, diversity/mode coverage, and compute cost; do not compare unlike losses as if they were a common metric. | P1 |
| 20–23 | 07 Recurrent networks | Hidden-state recurrence, gradient shrinkage/growth intuition, and gate roles are covered. Next: The lecture now gives full LSTM gate/cell equations, a numerical cell-state trace, and a standard GRU formulation. Remaining gate: verify the lab measures gradient behavior across sequence lengths and compares RNN/LSTM/GRU under a controlled budget. | P1 |
| 24–25 | 08 Sequence architectures + forecasting | Chronological split, leakage, recursive forecast error, and naive baselines are explained. Next: include a side-by-side worked state update for Elman and Jordan recurrence, explain the fully recurrent case's extra dependencies, and specify preprocessing-fit boundaries for leakage-safe evaluation. | P1 |
| 26–28 | 09 Boltzmann machines | RBM energy, probability intuition, and hidden-unit conditional probability now have beginner-oriented notation explanations. Next: work through a tiny configuration table with relative probabilities, then explicitly connect Gibbs sampling, contrastive divergence's approximation, and layer-wise DBN pretraining. | P1 |
| 29–31 | 10 Attention + Transformer bridge | Scaled dot-product attention now explains score scaling, softmax weights, and value mixing; the lab tests causal masking. Next: work a complete tiny multi-head tensor-shape example and compare BERT-style masked-token prediction with GPT-style next-token prediction, including what information each objective can access. | P1 |
| 32–33 | 11 Deep reinforcement learning | Return, value functions, Bellman target, Q update, replay, target network, and seeded evaluation motivation are taught. Next: The lecture now contrasts policy gradients with value-based DQN. Remaining gate: verify that the lab reports multi-seed results and uncertainty for stabilization ablations; policy gradients are not a full implementation lab here. | P1 |
| 34–35 | 12 Research capstone | Falsifiable hypotheses, evaluation contracts, ablations, uncertainty, error analysis, and report structure are covered. Next: provide one fully filled example experiment contract and one compact paper-ready result section, then assess individual mastery as well as team output. | P1 |

## Cross-course quality gates

Before marking Course 1 instructor-ready, verify each item against the actual chapter **and** notebook:

- [ ] Each of the 35 days has a stated learning outcome, a worked in-class example, a lab task, and a mastery check.
- [ ] Every important equation has symbol definitions, an English reading, and a worked calculation or derivation.
- [ ] The lab demonstrates the exact mechanism taught in the chapter; code is not a substitute for the explanation.
- [ ] Each comparison uses a declared baseline and controls the relevant data, parameter/training budget, and evaluation protocol.
- [ ] Real-data provenance, access/license basis, preprocessing, split, and metric are recorded.
- [ ] Failure cases are intentional and interpreted mechanistically.
- [ ] Where results are stochastic, report repeated runs and uncertainty rather than a best seed alone.
- [ ] Video links are supplemental, relevant to the exact concept, and checked before they are described as recommended resources.
- [ ] All relative links, equation rendering, images, and previous/next navigation are checked.
- [ ] A fresh notebook execution run is triggered after any notebook code change.

## Completed improvements recorded in this pass

- All 12 lab notebooks passed clean-kernel execution in the recorded workflow run.
- Every lecture has a chapter-specific static SVG and a Mermaid mechanism diagram.
- A follow-up pass improved equation formatting and beginner-first explanations in CNNs, autoencoders, RNNs, forecasting, RBMs, and attention; focused video companions were added where appropriate in [PR #22](https://github.com/mahashemi/llm-training-mastercalss/pull/22). The next teaching pass added full LSTM/GRU equations with a numerical cell-state trace, clarified Evolving SOM variant-specific mechanics, and introduced policy-gradient notation alongside DQN.
- Duplicate navigation footers and the incorrect Course 2 link in the capstone were corrected in this follow-up.

## Completion policy

Do not label the entire course “complete” solely because every notebook executes or because every chapter has a diagram. Completion means all 35 day-level promises are supported by teachable explanations, worked examples, reliable labs, answer keys, and evidence-based interpretation. Resolve P0 issues first, then P1 teaching gaps, then P2 evidence improvements. Update this audit as each gap is closed.
