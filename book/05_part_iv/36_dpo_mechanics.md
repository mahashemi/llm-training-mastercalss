# Chapter 36 — DPO Mechanics

**Part:** Part IV

## 1. What DPO is trying to learn

Direct Preference Optimization learns from pairs:

(x, y_w, y_l)

where y_w is preferred over y_l for the same input x.

A common objective is:

L_DPO = - log σ(β [ log π(y_w|x) - log π_ref(y_w|x) - log π(y_l|x) + log π_ref(y_l|x) ])

The key idea is **relative preference**, not simply “make the chosen answer probable.”

Reference:
https://arxiv.org/abs/2305.18290

## 2. What the terms do

| Term | Role | Practical question |
|---|---|---|
| Policy π | model being trained | Is it moving toward preferred outputs? |
| Reference π_ref | anchor | How far is the policy moving? |
| Chosen response | preferred sample | Is it actually better? |
| Rejected response | contrast sample | Is rejection meaningful? |
| beta | preference strength | How strongly should the pair affect training? |

## 3. Preference data is the real bottleneck

A DPO run can fail even with excellent optimization if the preference pairs are weak.

Bad pair:

chosen = longer answer  
rejected = shorter answer

If length is irrelevant, the model may simply learn verbosity.

Better pair:

chosen = correct, concise, grounded  
rejected = plausible but unsupported

The pair should isolate the behavior you want.

## 4. Dataset quality matrix

| Failure in preference data | Likely learned behavior |
|---|---|
| chosen always longer | verbosity |
| chosen always safer | excessive refusal |
| chosen always more formal | style over substance |
| narrow annotator group | annotator-specific preferences |
| inconsistent criteria | unstable learning |
| synthetic self-preferences | teacher artifacts |

## 5. DPO vs SFT

| Property | SFT | DPO |
|---|---|---|
| Data | demonstrations | chosen/rejected pairs |
| Signal | imitate target | prefer one response over another |
| Main use | behavior | preference/alignment |
| Annotation burden | target writing | pairwise judgment |
| Failure risk | imitation errors | preference bias |
| First baseline | prompting | SFT |

Do not skip SFT and assume preference optimization is a substitute for good demonstrations.

## 6. Worked example — medical response quality

For one patient question:

Rejected:

“Your symptoms are definitely harmless. No need to see anyone.”

Chosen:

“Based on the information provided, this may have several causes. Seek urgent care if warning signs X or Y occur.”

The preference should be grounded in the evaluation rubric:

- uncertainty handling;
- safety;
- actionability;
- factual support.

Then test whether DPO changes these dimensions without increasing unnecessary refusal.

## 7. beta and over-optimization

The beta parameter controls the strength of the preference signal in the objective.

Do not choose it from folklore.

Sweep:

| Run | beta | Hypothesis |
|---|---:|---|
| A | low | gentle preference shift |
| B | medium | balanced |
| C | high | stronger preference pressure |

Hold data and training budget comparable.

Measure:

- preference win rate;
- task correctness;
- verbosity;
- refusal rate;
- safety;
- regression.

## 8. Failure analysis

### Preference win rate rises, factuality falls

Likely proxy optimization or reward preference mismatch.

### Human preference rises, benchmark falls

The benchmark may not capture the desired behavior or preference labels may overfit style.

### Training becomes unstable

Check data quality, batch composition, learning rate, reference/policy scoring, and implementation.

### Model becomes too agreeable

Inspect whether chosen responses systematically reward compliance.

## 9. Evaluation design

Use at least:

**in-domain preference set**  
**held-out preference set**  
**objective capability set**  
**safety set**  
**human audit**

Do not use the same preference data for both optimization and final claims.

## 10. Research exercise

Construct 2,000 synthetic preference pairs for a narrow task.

Create three subsets:

- style-only preference;
- correctness preference;
- safety preference.

Run the same DPO training setup on each.

Measure which behavior changes and which unrelated behaviors move.

The research question is:

**What exactly did the preference data teach?**

## Laboratory

[dpo_and_distillation_concepts.ipynb](../../notebooks/dpo_and_distillation_concepts.ipynb)

## References

https://arxiv.org/abs/2305.18290
