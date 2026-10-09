# Curriculum Integrity Report

Audit date: 2026-09-30

## Resource inventory

| Layer | Count |
|---|---:|
| textbook chapters | 76 |
| numbered lectures | 24 |
| notebooks | 28 |
| runbooks | 14 |
| projects | 4 |
| templates | 10 |

## Integrity checks

- Textbook laboratory references were audited; Chapter 1 now has an immediate Notebook 01 link next to its prediction exercise.
- Shared textbook laboratories are explicitly documented in BOOK_LAB_MAP.md.
- All 24 numbered lectures have explicit notebook links and evidence contracts.
- The 28 notebooks on the audited branch parse as valid JSON.
- Core notebooks now include quantitative experiments and deliberate break cases.
- Runbooks include preflight, resource accounting, smoke tests, recovery, acceptance, and release procedures.
- Projects and templates now require measured baselines, resource metrics, failure analysis, and reproducibility metadata.
- README, INDEX, COURSE_MAP, BOOK_TOC, lecture index, notebook map, and the new Learning Graph were aligned around one practical training spine.
- The real-data layer now includes a Persian longitudinal case with corpus, synthetic-data, evaluation, tokenizer, SFT/PEFT, and continued-pretraining connections.
- The repository does not vendor large Persian corpora; experiments use streamed/sample slices and record source revisions and access/license basis.

## Curriculum invariant

predict → explain → implement → measure → break → diagnose → decide → reproduce

## Practical hardware spine

tiny GPT → Qwen3-0.6B/free Colab → 1.7B/4B single GPU → 7B/8B H100 → Qwen3.8-27B case study → multi-GPU H100 → foundation-model planning

## Maintenance

Model releases, APIs, hardware specifications, pricing, and Colab availability change. Date operational claims and pin exact revisions for experiments.

## Course 1 follow-up verification — 2026-10-09

The 12-chapter Neural Computing course received a focused visual and execution pass.

- Every Course 1 lecture now embeds a chapter-specific static SVG concept diagram and retains its Mermaid mechanism diagram.
- All 12 labs include experiment-derived plotting cells; executed notebooks are uploaded as GitHub Actions artifacts so the resulting figures and outputs can be inspected without committing volatile notebook outputs.
- The full clean-kernel workflow completed successfully for all 12 labs in run [37882928859](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37882928859). The run produced 12 unexpired executed-notebook artifacts.
- The workflow caught and drove fixes for an obsolete Hugging Face dataset loader, a missing `Ridge` import, and invalid artifact naming. Those failures were corrected before the successful run.
- Worked numerical examples were added for convolution, autoencoders, recurrent-state updates, time-series evaluation, SOM updates, VAE/GAN/diffusion objectives, RBM energy, attention, and Bellman updates.
- Duplicate laboratory footer blocks were removed from affected lectures; direct video companions were curated for several core topics.

This execution result verifies that the labs run in the current Python 3.11 GitHub Actions environment. It does not replace pedagogical review of every explanation, nor does one seed establish statistical robustness for any experiment.

The invariant remains:

**predict → explain → implement → measure → break → diagnose → decide → reproduce**

## Course 1 instructor-readiness follow-up — 2026-10-09

- Added [the 35-day instructor-readiness audit](COURSE1_35_DAY_READINESS_AUDIT.md), mapping the day plan to the actual chapters and separating verified execution from remaining pedagogical gaps.
- The audit identifies full LSTM/GRU equations, Evolving SOM mechanics, multi-head attention and BERT/GPT objective comparisons, policy-gradient coverage, and several controlled comparison protocols as substantive next gates—not as already completed work.
- The equation-readability and video-companion pass was merged in [PR #22](https://github.com/mahashemi/llm-training-mastercalss/pull/22).
- Removed duplicate chapter 11/12 navigation footers and corrected the capstone's Course 2 destination to the canonical course README.
- The current status is **execution-verified, pedagogical review ongoing**. The 35-day plan's instructor-readiness gate remains the standard for declaring the course complete.

## Course 1 targeted teaching pass — 2026-10-09

- Chapter 7 now gives full LSTM gate/cell equations, a numerical cell-state calculation, and a standard GRU formulation with a note that gate conventions vary across implementations.
- Chapter 3 now explains that Evolving SOM is a family of variants and requires each experiment to name its growth/pruning rule and compare against a declared baseline.
- Chapter 11 now introduces policy-gradient objectives and distinguishes direct policy learning from DQN's value-based approach.
- These are lecture improvements, not proof that every associated lab covers each concept. The [35-day readiness audit](COURSE1_35_DAY_READINESS_AUDIT.md) records the remaining lab-verification gates.

## Course 1 SOM lab update — 2026-10-09

- Chapter 3's lab now fits feature scaling on the training partition, evaluates prototype/SOM quantization on held-out examples, and includes an explicit growing 1-D SOM-family demonstration with a capacity-vs-error comparison.
- The growing-map example is clearly labeled educational and variant-specific; it is not presented as a canonical implementation of every Evolving SOM algorithm.
- The updated notebook was merged in [PR #25](https://github.com/mahashemi/llm-training-mastercalss/pull/25), and the later full execution run [#7](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37885701865) completed successfully on the resulting notebook version. All 12 clean-kernel jobs succeeded and all 12 executed-notebook artifacts were published, including the changed SOM lab.



## Course 1 Lecture 1 math rendering audit — 2026-10-09

- Replaced inline-math expressions in section headings with plain-language labels so headings remain readable in Markdown renderers that do not typeset math inside heading text.
- Restored consistent display-math delimiters for the gradient vector, gradient-descent updates, the chain-rule dependency path, and the layer-composition equation.
- Made the gradient vector explicit as the list of partial derivatives for each weight, rather than leaving \(\nabla_w L\) unexplained as a standalone symbol.
- Corrected the chapter title to identify it as Chapter 1 and removed the duplicate Course 1 home link from its navigation.
- Audited the edited source for unmatched display-math delimiters, standalone single-dollar display delimiters, and math expressions in headings; no such issues remain in the edited file.

## Course 1 cross-chapter math and attention follow-up — 2026-10-09

- The first audit caught malformed standalone single-dollar display delimiters in Chapters 4, 6, 7, 10, and 11. These were restored to proper display-math delimiters.
- Chapters 2–10 now have explicit chapter numbers in their top-level headings; Chapter 1's inline-math headings and duplicate home link were corrected in [PR #28](https://github.com/mahashemi/llm-training-mastercalss/pull/28).
- Chapter 10 now walks through multi-head attention tensor shapes using \(B=2\), \(T=3\), \(d_{\mathrm{model}}=4\), and \(H=2\), from projections through per-head scores, concatenation, and output projection.
- The attention lab now isolates BERT-style bidirectional versus GPT-style causal information access using a shared illustrative score matrix, with assertions checking that the causal row assigns zero probability to future positions.
- The updated attention lab passed clean-kernel execution in [full run #37915074150](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915074150), which completed all 12 jobs successfully and published executed notebooks.

## Course 1 controlled CNN experiment — 2026-10-09

- Chapter 4's lab now compares plain and residual convolutional blocks with the same learned layers and parameter count. For each of three seeds, both variants use the same initialization and minibatch order.
- The notebook records per-epoch training loss, final held-out loss/accuracy, and seed variability, with plots for optimization curves and final accuracy.
- The updated CNN lab's clean-kernel job passed in [run #37915247406](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915247406); the full 12-job workflow was still in progress at the time of this ledger update. This experiment is intentionally modest and does not yet constitute a full DenseNet-versus-ResNet benchmark.

## Course 1 generative objective and metric pass — 2026-10-09

- Chapter 6 now works through a numeric GAN discriminator loss and non-saturating generator loss, emphasizing that neither is a direct sample-quality or mode-coverage score.
- The GAN lab reports generated spread, fractions near each mode in its two-mode toy distribution, an explicit two-mode coverage fraction, update count, and environment-specific training time.
- The VAE and diffusion sections already include worked numeric objective/noising examples; the readiness audit now distinguishes those from the remaining need for a defensible sample-fidelity evaluation.
- The updated GAN lab's clean-kernel job passed in [run #37915461396](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915461396); that full workflow was still in progress at the time of this ledger update.

## Course 1 autoencoder regularization and representation pass — 2026-10-09

- Chapter 5 now defines sparse and contractive autoencoder objectives and works a numeric example for each penalty.
- The lab now freezes a trained encoder and evaluates latent vectors with a logistic-regression linear probe. It compares the trained encoder with raw pixels and an untrained random encoder using the same train/test examples.
- The lab uses a fixed seed for the baseline autoencoder and fits feature scaling only within each probe's training data via a pipeline.
- The updated autoencoder lab's clean-kernel job passed in [run #37915707503](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915707503). The linear-probe comparison is diagnostic and still needs repeated-seed uncertainty analysis.



## Validation ledger refresh — 2026-10-09

- **Attention lab:** all 12 notebooks passed in full run [#37915074150](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915074150), including the BERT/GPT visibility assertions.
- **CNN lab:** the updated plain/residual experiment's individual job passed in run [#37915247406](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915247406); the complete workflow was still running.
- **GAN lab:** the updated toy mode-coverage experiment's individual job passed in run [#37915461396](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915461396); the complete workflow was still running.
- **Autoencoder lab:** the updated frozen-encoder probe's individual job was still running in [#37915707503](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915707503). Do not mark it execution-verified until its job completes successfully.


## Autoencoder job completion — 2026-10-09

- The new frozen-encoder linear-probe notebook cell passed clean-kernel execution in [run #37915707503](https://github.com/mahashemi/llm-training-mastercalss/actions/runs/37915707503).
- That 12-job run is still in progress, so this records the individual autoencoder job as successful, not the entire latest suite as complete.


## Course 1 recurrent architecture and leakage pass — 2026-10-09

- Chapter 8 now works through two timesteps numerically for Elman-style hidden-state recurrence and Jordan-style output feedback, using explicitly stated toy weights and initial states.
- It distinguishes these layouts from the broader family of fully recurrent connectivity patterns without implying one universal equation.
- The forecasting protocol now states preprocessing-fit boundaries, target-time cutoff rules, permissible historical context in test windows, and rolling-origin evaluation.
- This lecture-only change does not require notebook execution; the remaining practical gate is an executable leakage demonstration and controlled recurrence comparison.

## Course 1 forecasting leakage lab correction — 2026-10-09

- A code review found that the forecasting lab standardized the full time series before the chronological split, allowing future-period statistics to influence training. The setup now defines the temporal cutoff first and fits `StandardScaler` on training-period values only.
- Window targets are assigned explicit timestamps; assertions verify that training targets precede the cutoff and test targets occur after it.
- The intentionally random overlapping-window split is labeled as an invalid diagnostic, not a deployment-valid estimate. The chronological holdout remains the primary metric.
- Because notebook code changed, the forecasting lab must pass a fresh clean-kernel execution before this correction is considered verified.

## Course 1 RBM probability and Gibbs-sampling pass — 2026-10-09

- Chapter 9 now enumerates all four states of a one-visible/one-hidden RBM, calculates the partition function and normalized joint probabilities, and computes conditional activation probabilities.
- It explains CD-\(k\) as a positive-minus-negative association-statistic update and outlines classic greedy layer-wise RBM pretraining for a DBN without treating a stacked RBM as one undifferentiated model.
- The lab's Gibbs intervention now alternates actual hidden and visible sampling, compares sampled hidden-visible association statistics with data statistics, and records environment-specific sampling time. It no longer labels distance from the starting image as a reconstruction-quality measure.
- Notebook code changed; fresh clean-kernel execution is required after merge. Repeated seeds and stronger distributional evaluation remain open evidence-quality work.

