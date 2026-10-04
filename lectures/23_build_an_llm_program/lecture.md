# Lecture 23 — Build an LLM Program

**Lab:** [national_llm_resource_plan.ipynb](./lab.ipynb)

## Outcome

The learner should be able to turn a model experiment into an operating program with explicit owners, resources, gates, risks, and evidence.

## Start with the mission, not the model

Give the class this requirement:

“Build a useful multilingual assistant in 12 months.”

Ask: what would you budget?

The correct first response is **not a GPU number**.

Convert the mission into:

**users → tasks → target capability → baseline → metric → constraints**

Example:

| Requirement | Example |
|---|---|
| Users | public-service staff |
| Languages | 4 |
| Main task | question answering + summarization |
| Fresh knowledge | yes |
| Latency | p95 < 2 s |
| Deployment | local |
| Budget | fixed |
| Governance | controlled data |

## Build the evidence ladder

Before requesting a large program:

**API/model baseline**  
→ **RAG/tool baseline**  
→ **SFT/PEFT pilot**  
→ **continued-pretraining pilot if needed**  
→ **small-model scaling study**  
→ **program proposal**

Each stage removes one uncertainty.

## Program workstreams

Draw seven parallel tracks:

1. data;
2. model research;
3. training systems;
4. evaluation;
5. serving/product;
6. governance/security;
7. program/procurement.

Then show the handoffs.

| Workstream | Key artifact |
|---|---|
| Data | versioned corpus + data card |
| Research | model/config records |
| Systems | throughput/scaling report |
| Evaluation | scorecard + failure analysis |
| Serving | latency/cost report |
| Governance | rights/risk record |
| Program | budget + milestone plan |

## Resource planning

Teach the resource chain:

**target model/data → FLOPs → measured throughput → wall time → accelerator cost → storage → staffing → total TCO**

First-order dense-LM planning:

FLOPs ≈ 6ND

Then use measured effective throughput.

Example:

7B parameters × 100B training tokens

$\mathrm{FLOPs} \approx 4.2\times10^{21}$

If a pilot cluster delivers 5e15 effective FLOP/s:

$t_{wall} \approx 9.7\ \mathrm{days}$

The point is not the number. The point is that every budget line has an assumption behind it.

## Stage gates

| Stage | Spend | Required evidence |
|---|---:|---|
| Baseline | tiny | measured gap |
| Data pilot | low | quality + rights |
| Training pilot | low–medium | stable learning + target gain |
| Scaling test | medium | scaling curve |
| Product pilot | medium | user/SLO evidence |
| Program | high | integrated technical + economic case |

At every gate define:

**metric → threshold → artifact → owner → next budget**

## Team design

Show a small pilot team:

- technical lead;
- ML/research engineer;
- data engineer;
- evaluator/domain expert;
- platform/infra support;
- part-time program management.

Then ask what changes at scale.

Answer: the functions do not disappear; they become dedicated roles.

## Risk and governance

Create a live risk table:

| Risk | Indicator | Response |
|---|---|---|
| poor data | quality score falls | stop acquisition, improve sources |
| training instability | validation divergence | fix pipeline before scaling |
| regression | protected eval drops | reduce specialization |
| budget growth | forecast exceeds ceiling | reduce scope/pivot |
| data rights | unresolved source | quarantine/remove |
| serving cost | cost/task above limit | distill/smaller model |

## Exit challenge

Produce one page:

**mission → baseline → evidence → workstreams → resources → budget → milestones → risks → release plan**

### Critical-thinking question

Why can a technically excellent model still be a failed program?

Because the program can fail at data rights, evaluation, serving economics, staffing, reliability, or schedule even when the model itself works.

### References

Stanford CS336: https://cs336.stanford.edu/  
OLMo 2: https://allenai.org/olmo2


## Lab contract

Complete the linked laboratory before treating the lecture as mastered. Record a baseline, one intervention, at least one failure, and the next experiment. See the lecture's lab contract.

## Deepening — the model program is a dependency graph

Draw dependencies:

**data rights → data pipeline → training → evaluation → serving**

and parallel tracks:

**governance + security + procurement + staffing**.

A blocked dependency can stop a technically successful model.

### Resource derivation exercise

Start with:

- parameter count;
- training tokens;
- measured tokens/sec/GPU;
- expected scaling efficiency;
- desired wall time.

Derive:

**GPU count → accelerator hours → checkpoint storage → staffing load → TCO**

You must state assumptions next to every number.

### Gate design

For each milestone define:

**metric + threshold + artifact + owner + budget released**

This converts a one-time funding request into a sequence of evidence gates.



## Lab — run it here

**Primary laboratory:** [Open the executable lab notebook](./lab.ipynb)

Run the notebook as part of this chapter: establish the baseline, change one controlled variable, measure the result, inspect a failure or edge case, record the quantitative evidence, explain the result, and propose the next experiment.

---

<div align="center">

[← Previous: Lecture 22 — API vs RAG vs Tools vs Training](../22_api_vs_rag_vs_tools_vs_training/lecture.md) · [Next: Lecture 24 — From Experiment to a Fundable Model →](../24_from_experiment_to_fundable_model/lecture.md)

</div>