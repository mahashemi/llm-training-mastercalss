# Research Project Specification

Use this template for every serious student project.

## 1. Project identity

- **Title:**
- **Project ID:**
- **Course stage:**
- **Research family:**
- **Difficulty:** Foundation / Intermediate / Advanced / Capstone
- **Primary learner skill:**

## 2. Research question

> State one falsifiable question.

## 3. Hypothesis

> State what you expect, why, and what observation would disconfirm it.

## 4. Prior work

- 3–10 most relevant papers/resources:
- What is already known?
- What remains uncertain?

## 5. Data

- Dataset(s):
- Version/snapshot:
- Source:
- License/access basis:
- Schema:
- Split policy:
- Preprocessing:
- Deduplication:
- Contamination controls:
- Known limitations:

## 6. Baseline

Describe the strongest reasonable baseline that can be run under the available budget.

Record:
- model/checkpoint;
- tokenizer;
- hyperparameters;
- training budget;
- evaluation protocol;
- compute.

## 7. Intervention

What exactly changes relative to the baseline?

## 8. Controlled variables

List what must remain fixed so that the comparison is interpretable.

## 9. Evaluation contract

Before running the expensive experiment, define:
- primary metric;
- secondary metrics;
- important slices;
- statistical/uncertainty procedure;
- success/failure criterion.

## 10. Experiment matrix

| Experiment | Variable | Baseline | Intervention | Budget | Expected observation |
|---|---|---|---|---|---|
| E0 | sanity | | | | |
| E1 | main effect | | | | |
| E2 | ablation | | | | |
| E3 | robustness | | | | |
| E4 | generalization | | | | |

## 11. Failure analysis

Record failures by category rather than only listing bad examples.

## 12. Resource accounting

- Hardware:
- GPU memory:
- Training time:
- Inference time:
- Peak memory:
- Tokens:
- Estimated cost:
- Energy measurement, if available:

## 13. Reproducibility

- Git commit:
- Environment:
- Dataset manifest:
- Configuration:
- Random seeds:
- Exact commands:
- Artifact locations:

## 14. Results

Prefer tables and figures that directly answer the research question.

## 15. Interpretation

Separate:
- observation;
- explanation;
- speculation.

## 16. Limitations

State what the experiment cannot establish.

## 17. Conclusion

Answer the research question in one paragraph and bound the claim to the evidence.

## 18. Release package

- [ ] README
- [ ] code
- [ ] configuration
- [ ] dataset card/manifest
- [ ] model card if applicable
- [ ] results
- [ ] figures
- [ ] reproducibility instructions
- [ ] license
- [ ] paper/report
