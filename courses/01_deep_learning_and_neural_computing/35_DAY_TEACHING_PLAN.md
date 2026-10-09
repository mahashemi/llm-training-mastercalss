# Course 1 — 35-Day Teaching Plan (70 Contact Hours)

**Format:** 35 instructor-led teaching days × 2 hours/day = 70 contact hours  
**Audience:** 30 learners, from early-stage programmers to engineering students  
**Purpose:** build deep-learning understanding through intuition, explicit mathematics, implementation, controlled experiments, and research habits.

This is the day-by-day delivery plan for Course 1. It maps the existing 12 chapters into 35 teaching sessions; it does not replace their chapter content or notebook labs. Each session is designed to fit a two-hour class. Longer coding runs, reading, and capstone work happen between sessions.

## Session design

Use this rhythm as a default, adapting it to the topic:

- **0–10 min — Retrieval and motivation:** revisit one prior idea and introduce a concrete problem.
- **10–30 min — Intuition and visual model:** explain the mechanism before notation.
- **30–60 min — Mathematics and worked example:** define every symbol, show shapes where relevant, and calculate at least one example by hand.
- **60–90 min — Live implementation:** trace a minimal mechanism from scratch, then connect it to a framework implementation.
- **90–110 min — Experiment and failure mode:** predict, change one variable, measure, and explain.
- **110–120 min — Mastery check:** short exit questions, answer discussion, and bridge to the next session.

The schedule is a teaching guide, not a reason to rush. If students cannot explain a mechanism, reduce optional breadth rather than skipping the worked example or failure analysis.

## Day-by-day schedule

| Day | Existing chapter | Two-hour teaching focus | In-class practical / evidence of learning |
|---:|---|---|---|
| 1 | 01 Neural computation | What learning means; examples, features, targets, parameters; linear neuron and decision boundary | Calculate neuron outputs by hand; identify weights, bias, inputs, and output |
| 2 | 01 Neural computation | Perceptron vs. Adaline; hard decisions vs. continuous scores; loss as a measurable error | Implement perceptron and Adaline updates; compare what each learns from the same examples |
| 3 | 02 Feedforward + backprop | Why multilayer networks; affine transforms, activations, shapes, XOR, representation learning | Forward-pass a tiny network by hand and in code |
| 4 | 02 Feedforward + backprop | Derivatives, partial derivatives, gradients, chain rule, backpropagation, gradient descent | Derive and check gradients numerically; explain each term in a parameter update |
| 5 | 02 Feedforward + backprop | Training dynamics: SGD/minibatches, momentum/Adam, initialization, normalization, regularization, validation and generalization | Run a controlled overfitting experiment; compare train and validation curves |
| 6 | 03 Competitive learning + SOM | Why unsupervised organization; winner-take-all learning and competitive units | Implement winner selection and weight updates on a small dataset |
| 7 | 03 Competitive learning + SOM | Self-organizing maps: best matching unit, neighborhood, schedule, topology and interpretation | Train and visualize a SOM; explain what the map preserves and what it does not |
| 8 | 03 Competitive learning + SOM | Evolving SOMs; growth/pruning intuition, model selection, limits and fair comparisons | Compare a fixed SOM with a growing/evolving map using a documented metric and visual inspection |
| 9 | 04 CNNs | Images as tensors; convolution/cross-correlation, kernels, channels, stride, padding and output shapes | Calculate output dimensions and a small convolution by hand |
| 10 | 04 CNNs | Receptive fields, parameter sharing, pooling, translation-related inductive bias, CNN training | Train a small CNN; compare parameter count and behavior with a dense baseline |
| 11 | 04 CNNs | Residual connections: degradation, identity paths, gradient flow, ResNet blocks | Implement a residual block and test tensor shapes and gradient flow |
| 12 | 04 CNNs | DenseNet connections, feature reuse, compute/memory trade-offs, controlled architecture comparison | Compare a plain, residual, and dense-style block under a fixed budget; interpret limitations |
| 13 | 05 Autoencoders | Encoder/decoder, bottleneck, reconstruction objectives, latent representation and baselines | Train a basic autoencoder; inspect original/reconstructed examples |
| 14 | 05 Autoencoders | Denoising, sparse, and contractive ideas; regularization as a change in what representation is encouraged | Corrupt inputs or alter regularization; compare reconstruction and latent behavior |
| 15 | 05 Autoencoders | Representation evaluation, latent-space pitfalls, leakage, reconstruction vs. useful features | Evaluate representations without treating low reconstruction error as proof of usefulness |
| 16 | 06 Generative models | Generative vs. discriminative learning; latent-variable models and probability foundations | Draw the data-generation story and inspect a simple latent-variable model |
| 17 | 06 Generative models | VAE: encoder distributions, reparameterization, reconstruction term, KL term, ELBO intuition | Trace the VAE objective term by term and run a small training experiment |
| 18 | 06 Generative models | GANs: generator/discriminator game, alternating updates, instability, mode collapse and evaluation | Inspect losses and samples; diagnose a failure rather than relying on loss alone |
| 19 | 06 Generative models | Diffusion: forward noising, denoising target, noise schedule, sampling and cost-quality trade-offs | Visualize a noising trajectory and train/inspect a small denoising experiment |
| 20 | 07 Recurrent networks | Sequences, recurrent state, shared parameters, unrolling, many-to-one and many-to-many tasks | Unroll a tiny recurrent network and trace hidden states across tokens/time steps |
| 21 | 07 Recurrent networks | Backpropagation through time; vanishing/exploding gradients and truncation | Measure gradient norms over sequence length; deliberately create a failure |
| 22 | 07 Recurrent networks | LSTM gates and cell state; why gated memory was introduced | Calculate gate effects on a small numeric example and inspect gate activations |
| 23 | 07 Recurrent networks | GRU mechanics; LSTM/GRU/simple RNN comparison and when extra complexity is justified | Compare models under a controlled parameter/data/training budget |
| 24 | 08 Sequence architectures + forecasting | Elman, Jordan, and fully recurrent architectures; state feedback and architectural differences | Sketch and implement small recurrence variants; identify information paths |
| 25 | 08 Sequence architectures + forecasting | Forecast horizons, chronological splits, leakage, scaling, naive baselines and metrics | Build a leakage-safe forecasting pipeline and compare against a naive baseline |
| 26 | 09 Boltzmann machines | Energy-based models; probability from energy; visible/hidden units and stochastic states | Compute energies for a tiny configuration table and explain relative probabilities |
| 27 | 09 Boltzmann machines | Restricted Boltzmann machines; conditional independence, contrastive divergence and sampling | Implement a tiny RBM update/sampling loop and inspect reconstruction behavior |
| 28 | 09 Boltzmann machines | Deep belief networks, layer-wise pretraining, historical context and limitations | Diagram the stack; compare the historical motivation with modern end-to-end training |
| 29 | 10 Attention + Transformer bridge | From recurrence to attention; queries, keys, values, score scaling and softmax | Calculate attention weights and weighted values for a tiny sequence by hand |
| 30 | 10 Attention + Transformer bridge | Multi-head attention, positional information, residuals, normalization and feed-forward blocks | Trace tensor shapes through a Transformer block; test causal masking |
| 31 | 10 Attention + Transformer bridge | Encoder/decoder distinction; BERT-style masked-language modeling vs. GPT-style causal prediction | Compare objectives and information access; run a tiny objective demonstration |
| 32 | 11 Deep reinforcement learning | Agent/environment, states, actions, rewards, returns, policies, value functions and Bellman equation | Work through a tiny Markov decision process and calculate one value update |
| 33 | 11 Deep reinforcement learning | Q-learning, DQN, replay buffer, target network, exploration, policy-gradient overview and evaluation variance | Train or inspect a small environment; compare seeded runs and identify instability |
| 34 | 12 Research capstone | Turn a question into a falsifiable hypothesis; baseline, data split, metric, controls, ablations and reproducibility | Teams submit a one-page experiment contract and run a pilot/baseline |
| 35 | 12 Research capstone | Results, uncertainty, error analysis, limitations, paper-ready communication and course synthesis | Team presentations; peer review; individual oral/written mastery check |

## Assessment checkpoints

- **Days 1–5 — Learning mechanics:** learners can calculate a forward pass, explain loss and gradients, derive a simple update, and distinguish training from generalization.
- **Days 6–8 — Unsupervised structure:** learners can explain competition, SOM neighborhoods, and the assumptions behind map-based visualizations.
- **Days 9–12 — Convolutional design:** learners can calculate shapes, explain parameter sharing, and compare skip/dense connectivity with evidence.
- **Days 13–19 — Representation and generation:** learners can distinguish reconstruction objectives from generative objectives and compare VAE, GAN, and diffusion trade-offs.
- **Days 20–25 — Sequences:** learners can trace recurrence, explain gated memory, and design a leakage-safe forecasting evaluation.
- **Days 26–28 — Energy-based learning:** learners can reason about energy, sampling, RBM learning, and the historical role of DBNs.
- **Days 29–31 — Attention and Transformers:** learners can calculate attention and distinguish BERT-like and GPT-like training objectives.
- **Days 32–33 — Reinforcement learning:** learners can explain the reward/value distinction and diagnose variance or instability in a small experiment.
- **Days 34–35 — Research practice:** each team presents a reproducible experiment with a baseline, a controlled intervention, uncertainty/error analysis, and limitations.

## Homework and lab policy

The two-hour session is not expected to contain every line of notebook work. Each day should have:

1. A **pre-class warm-up** (5–15 minutes): one short reading segment or two retrieval questions.
2. An **in-class worked example** that is completed with the instructor.
3. A **post-class lab task** (typically 30–90 minutes, depending on the day) with a working reference solution.
4. A **short mastery check** that asks learners to explain, calculate, debug, or choose—not merely define.
5. An **optional stretch task** for faster learners, ideally a controlled experiment rather than extra boilerplate.

For a class of 30, use pairs for implementation and groups of 3–4 for the capstone. Require each learner to submit individual answers to key conceptual and mathematical checks so group coding does not conceal gaps.

## Instructor readiness gate

Before the course is advertised as complete, verify each of the 35 sessions against the actual chapter and notebook:

- the chapter supports the session's promised depth and does not merely name the concepts;
- every important equation has plain-language symbol definitions, a derivation or justification, and a worked example;
- the notebook executes from a clean runtime with pinned or documented dependencies and CPU fallback where feasible;
- expected outputs, answer keys, and interpretations are present;
- the real dataset, license/source, split strategy, and evaluation metric are documented;
- at least one controlled intervention and one failure analysis are included where appropriate;
- video links are curated to the specific concept and are supplemental rather than substitutes for teaching;
- navigation, equations, code cells, and references render correctly.

**Important:** this plan allocates all 35 teaching days. It does not by itself certify that every existing lecture and notebook already meets the instructor-readiness gate; that requires chapter-by-chapter content and execution review.
