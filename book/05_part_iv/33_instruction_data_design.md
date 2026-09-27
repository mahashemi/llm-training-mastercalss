# Chapter 33 — Instruction Data Design

**Part:** Part IV

## Core concepts
1. **Prompt diversity** — Cover task forms and difficulty levels.
2. **Response quality** — Prefer correct, useful, well-formatted demonstrations.
3. **Conversation structure** — Role and turn order are part of the model input.
4. **Negative examples** — Can expose undesirable behavior when handled carefully.

## Formal view
SFT estimates p(y|x) from demonstrations. The empirical distribution over prompts and responses determines which behaviors receive gradient pressure.

## Engineering workflow
Baseline → intervention → evaluation → profiling → failure analysis → decision.

## Laboratory
[sft_with_a_small_open_model.ipynb](../../notebooks/sft_with_a_small_open_model.ipynb)

## Critical thinking
**Question:** What could make the method appear to work while the real objective gets worse?

**Answer:** Proxy optimization, data leakage, benchmark contamination, distribution shift, or resource-side regressions can all produce misleading gains.

**Question:** What should the next experiment be?

**Answer:** The cheapest experiment that tests the highest-impact uncertainty.

## Research prompt
State a falsifiable claim and design a minimum-cost test that could reject it.

## References
https://huggingface.co/docs/trl/sft_trainer
