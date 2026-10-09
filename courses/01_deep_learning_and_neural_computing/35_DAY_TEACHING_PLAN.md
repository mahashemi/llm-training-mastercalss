# Course 1 — 35-Day Teaching Plan (70 Contact Hours)

**Format:** 35 instructor-led teaching days × 2 hours/day = 70 contact hours  
**Audience:** 30 learners, from early-stage programmers to engineering students  
**Purpose:** build deep-learning understanding through intuition, explicit mathematics, implementation, controlled experiments, and research habits.

This is the day-by-day delivery plan for Course 1. It maps the existing 12 chapters into 35 teaching sessions; it does not replace their chapter content or notebook labs. Research starts on Day 1, the midterm is on Day 18, Boltzmann machines receive one historically contextualized session, and the final week is reserved for controlled experiments, reporting, presentation, and submission. Each session is designed to fit a two-hour class. Longer coding runs, reading, and capstone work happen between sessions.

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

| Day | Focus | Two-hour teaching focus | In-class practical / evidence of learning |
|---:|---|---|---|
| 1 | 01 Neural computation + course launch | What learning means; course roadmap; how a neural model turns examples into parameters; the research journey from curiosity to evidence | Calculate a neuron output; browse the project catalogue; write one question you would genuinely like to investigate |
| 2 | 01 Neural computation | Perceptron vs. Adaline; hard decisions vs. continuous scores; loss as measurable error | Implement both updates and compare behavior on the same examples |
| 3 | Research launch | From broad interest to a testable question; tour of the 48-project catalogue; selecting a feasible Course 1 project family | Submit a one-paragraph interest statement and a first candidate question |
| 4 | 02 Feedforward + backprop | Why multilayer networks; affine transforms, activations, tensor shapes, XOR and learned representations | Forward-pass a tiny network by hand and in code |
| 5 | 02 Feedforward + backprop | Derivatives, partial derivatives, gradients, chain rule and backpropagation; introduce the study-report assignment | Derive a simple gradient and submit a short study-report topic + 2 starter references |
| 6 | 02 Feedforward + backprop | Gradient descent, SGD/minibatches, momentum/Adam, initialization and learning-rate behavior | Numerically check a gradient; compare two learning rates under a controlled setup |
| 7 | Research milestone | Project proposal clinic: question, hypothesis, dataset, baseline, metric, intervention, risks and compute budget | Submit a one-page project proposal; instructor approves or narrows scope |
| 8 | 03 Competitive learning + SOM | Unsupervised organization, winner-take-all learning, best matching unit and neighborhood updates | Implement winner selection and a numerical neighborhood update |
| 9 | 03 Competitive learning + SOM | SOM topology, schedules, interpretation, evolving maps and limits of visualizations | Train and visualize a SOM; report what the map preserves and what it does not |
| 10 | 04 CNNs | Images as tensors; convolution, channels, stride, padding and output shapes | Calculate a convolution and output dimensions by hand |
| 11 | 04 CNNs | Receptive fields, parameter sharing, pooling and CNN training | Compare a small CNN with a dense baseline; record parameter count and behavior |
| 12 | 04 CNNs | Residual connections, gradient flow, DenseNet feature reuse and compute/memory trade-offs | Compare plain, residual and dense-style blocks under a declared budget |
| 13 | 05 Autoencoders | Encoder/decoder, bottleneck, reconstruction objective and latent representations | Train an autoencoder; inspect original and reconstructed examples |
| 14 | 05 Autoencoders | Denoising/sparse/contractive ideas; representation evaluation, leakage and reconstruction pitfalls | Compare a learned representation against a simple baseline; submit a project baseline plan |
| 15 | 06 Generative models | Generative vs. discriminative learning; latent-variable models; VAE objective and ELBO intuition | Explain each VAE loss term and run a small experiment |
| 16 | 06 Generative models | GAN generator/discriminator game, alternating updates, instability and mode collapse | Inspect losses and samples; diagnose a failure rather than relying on loss alone |
| 17 | 06 Generative models | Diffusion: forward noising, denoising target, schedules, sampling and compute-quality trade-offs | Visualize a noising trajectory; study-report outline and project progress check |
| 18 | Midterm examination | Individual assessment of foundational understanding and experimental reasoning | Closed-book/controlled-resource exam: concepts, worked calculations, interpretation and short debugging/reasoning tasks |
| 19 | 07 Recurrent networks | Sequences, recurrent state, shared parameters, unrolling and sequence tasks | Trace hidden states across a tiny sequence |
| 20 | 07 Recurrent networks | Backpropagation through time; vanishing/exploding gradients and truncation | Measure gradient norms over sequence length and explain a failure |
| 21 | 07 Recurrent networks | LSTM gates and cell state; why gated memory was introduced | Calculate gate effects in a numerical example |
| 22 | 07 Recurrent networks | GRU mechanics; compare simple RNN, LSTM and GRU under a controlled budget | Compare models and interpret quality/complexity trade-offs |
| 23 | 08 Sequence architectures + forecasting | Elman/Jordan/fully recurrent architectures; forecast horizons, chronological splits and leakage | Build a leakage-safe forecasting pipeline with a naive baseline |
| 24 | 10 Attention + Transformer bridge | From recurrence to attention; queries, keys, values, scaling and softmax | Calculate attention weights and weighted values by hand |
| 25 | 09 Boltzmann machines — historical lens | Energy-based models, RBMs, contrastive divergence and DBN layer-wise pretraining; why these ideas mattered historically and why they are not the modern default | Compute energies for a tiny model; compare historical motivation with modern end-to-end learning |
| 26 | 10 Attention + Transformer bridge | Multi-head attention, positional information, residuals, normalization, feed-forward blocks and causal masks | Trace tensor shapes through a Transformer block and test causal visibility |
| 27 | 10 Attention + Transformer bridge | BERT-style masked prediction vs. GPT-style causal prediction; encoder/decoder distinction | Compare objective and information access; submit a project interim result table |
| 28 | 11 Deep reinforcement learning | States, actions, rewards, returns, value functions, Bellman equation, Q-learning and DQN overview | Work through a small MDP and calculate a value update |
| 29 | Research studio | Project clinic: debug the baseline, check data splits, freeze evaluation contract and identify one controlled intervention | Submit baseline evidence and a reproducibility checklist |
| 30 | Study report workshop | Critical reading: claim, method, evidence, limitations and relation to the student's project | Submit a complete study-report draft with figures/notes and references |
| 31 | Research studio | Run the main controlled intervention; plan ablations; check seeds, metrics, resource budget and failure slices | Submit a preregistered experiment update and first results table |
| 32 | Research studio | Error analysis, uncertainty, robustness and paper-ready visualization | Produce one defensible figure and one error-analysis table |
| 33 | Research communication | Short research talks, peer review, claim calibration and actionable feedback | Each team presents question, method, evidence, limitations and next step |
| 34 | Submission day | Final project package and study report; reproducibility, citation, licensing and responsible public release | Submit code/configs/results, project report or paper draft, and individual contribution statement |
| 35 | Final examination + synthesis | Individual final exam spanning course concepts and research judgment; reflect on next research steps | Final exam; students leave with a documented next-step plan for improving or extending the project |
## Assessment checkpoints and milestone calendar

| When | Milestone | What students submit |
|---|---|---|
| Day 1 | Course launch | One research curiosity/question |
| Day 3 | Project exploration | Interest statement + candidate question |
| Day 5 | Study report starts | Topic, research question, two starter references |
| Day 7 | Project proposal | Question, hypothesis, data, baseline, metric, intervention, compute and risk |
| Day 14 | Baseline plan | Feasible baseline and evaluation protocol |
| Day 17 | Progress checkpoint | Study-report outline + project baseline status |
| Day 18 | Midterm | Individual exam |
| Day 27 | Interim result | First controlled result table and next experiment |
| Day 29 | Baseline/evaluation gate | Reproducible baseline and frozen evaluation contract |
| Day 30 | Study report draft | Critical review of a paper or tightly related paper set |
| Day 31 | Main experiment | Intervention results and ablation plan |
| Day 32 | Evidence package | Figure, error analysis, uncertainty and limitations |
| Day 33 | Presentation | Short talk + peer feedback |
| Day 34 | Final submission | Project package + final study report + contribution statement |
| Day 35 | Final exam | Individual summative assessment |

### What belongs before the midterm?

The midterm covers Days 1–14: neuron/perceptron/Adaline, loss and gradient intuition, feedforward networks and backpropagation, optimization and generalization, competitive learning/SOMs, CNNs and residual/dense connections, autoencoders, and experimental reasoning. Students will already have selected a project and should have a proposal and an initial baseline plan. The exam checks individual understanding; the project continues independently of the exam.


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
