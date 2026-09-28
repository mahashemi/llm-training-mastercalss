# Chapter 70 — Risk Register and Kill Criteria

**Part:** Part VIII

## 1. Make downside measurable

Large LLM programs can fail through:

- technical instability;
- poor data;
- evaluation leakage;
- safety/security regressions;
- infrastructure failure;
- staffing gaps;
- procurement delays;
- budget growth;
- governance blockers.

A risk register turns concern into an owned decision.

## 2. Risk scoring

For ordinary risks:

expected_exposure = probability × impact

Use this for prioritization, but do not treat rare severe failures as safe merely because their estimated probability is low.

| Risk | Probability | Impact | Owner | Mitigation | Trigger |
|---|---|---|---|---|---|
| data quality collapse | medium | high | data lead | source QA + holdout | quality below threshold |
| training instability | medium | high | ML lead | small-run validation | divergence/NaN |
| cluster outage | medium | medium | systems | checkpoints + recovery | recovery exceeds SLA |
| evaluation leakage | low | high | eval lead | protected holdout | contamination found |
| safety regression | unknown | high | safety lead | dedicated eval gate | critical failure |
| budget overrun | medium | high | program lead | stage-gate spend | forecast above ceiling |

## 3. Define stop conditions before spending

A stop condition should be:

- measurable;
- predeclared;
- tied to the mission;
- difficult to redefine after results are known.

Examples:

**Technical:** target capability does not improve after the agreed experimental budget.

**Economic:** cost per successful task exceeds the program ceiling.

**Quality:** protected capability regression exceeds the limit.

**Governance:** required data rights remain unresolved.

**Safety:** severe failure appears without an acceptable mitigation.

## 4. Pause, pivot, or continue

Possible gate outcomes:

| Outcome | Meaning |
|---|---|
| Continue | evidence supports next stage |
| Continue with correction | target still plausible; fix identified |
| Pivot | original intervention is not addressing the bottleneck |
| Pause | evidence is insufficient |
| Reduce scope | value exists but full target is uneconomic |
| End program | central hypothesis failed |

The important practice is to make the rule before sunk costs distort judgment.

## 5. Worked example

Suppose a continued-pretraining pilot has:

- target-language gain = +2%;
- general-capability change = −1%;
- throughput = 90% of plan;
- spend = 80k currency units.

Predeclared gate:

- target gain ≥ +5%;
- general loss ≤ 2%;
- throughput ≥ 80%.

Two conditions pass, but the primary capability hypothesis fails.

A rational next step could be:

- inspect corpus quality;
- change data mixture;
- test tokenizer;
- compare a different base model.

Simply spending another 80k without a new hypothesis is not evidence-based.

## 6. Leading indicators

Monitor before final evaluation:

- training-loss slope;
- validation loss;
- gradient norms;
- throughput;
- GPU utilization;
- input-pipeline stalls;
- data rejection rates;
- duplicate rates;
- checkpoint failures;
- evaluation drift;
- safety test failures.

Leading indicators can prevent a failed long run from becoming an expensive surprise.

## 7. Dependency risk

Risks are often coupled:

**poor data → poor quality → larger training budget → schedule slip → staffing pressure → higher cost**

Model important chains explicitly.

## Research exercise

Create a 15-risk register.

For each risk specify:

**risk → probability → impact → owner → leading indicator → mitigation → stop condition → contingency**

Then identify which three risks could invalidate the entire program.

## Laboratory

[capstone_model_program.ipynb](../../notebooks/capstone_model_program.ipynb)

## Reference

https://cs336.stanford.edu/
