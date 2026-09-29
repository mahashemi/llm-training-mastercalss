# Chapter 60 — API Economics and Total Cost of Ownership

**Part:** Part VII

## 1. The mistake this chapter prevents

Teams often compare API token price with GPU hourly price. That is not total cost.

A practical TCO model is:

TCO =
platform
+ inference
+ training
+ data
+ evaluation
+ engineering
+ operations
+ risk and contingency

The categories differ by architecture, but the principle is stable: count the whole lifecycle.

## 2. Cost anatomy

| Cost line | API | Self-hosted open model | Fine-tuned model | RAG |
|---|---|---|---|---|
| Initial training | usually none | none if using released weights | yes | usually none |
| Model inference | variable | capacity cost | capacity cost | model + retrieval |
| Retrieval | optional | optional | optional | core |
| Data ingestion | app-dependent | app-dependent | often material | core |
| Evaluation | required | required | required | required |
| Monitoring | required | required | required | required |
| Staff | integration/ops | infra + ML | ML + infra | retrieval + ML/ops |
| Vendor dependency | higher | lower but not zero | depends | depends |
| Traffic exposure | token pricing | utilization/capacity | utilization/capacity | model + retrieval |

Do not call one column “cheaper” without workload assumptions.

## 3. API request cost

For N requests/month:

C_API =
N × [
input_tokens/1,000,000 × input_price
+
output_tokens/1,000,000 × output_price
]
+
fixed_application_cost

For RAG:

input_tokens = base_input + retrieved_tokens

Therefore retrieval depth is also a cost variable.

## 4. Self-hosted cost

A simple planning equation:

C_self_hosted =
GPU_hours × blended_GPU_rate
+ storage
+ network
+ orchestration
+ monitoring
+ idle capacity
+ operations

The hidden term is often idle capacity. Peak capacity can be several times normal capacity.

## 5. Training cost

For dense language-model planning, a common first-order heuristic is:

FLOPs ≈ 6ND

where:

- N = parameter count;
- D = training tokens.

Convert to time with measured delivered throughput:

time = total_FLOPs / effective_FLOPs_per_second

Then:

compute_cost = accelerator_hours × blended_rate

The coefficients are planning approximations, not laws. Measure real throughput.

## 6. Worked training example

Suppose:

- N = 7 billion parameters;
- D = 100 billion tokens.

Then:

FLOPs ≈ 6 × 7e9 × 100e9 = 4.2e21

If the actual cluster delivers 5e15 effective FLOPs/s:

time ≈ 4.2e21 / 5e15 ≈ 8.4e5 seconds ≈ 9.7 days

At an illustrative blended rate of 5 currency units/hour for the whole cluster:

compute ≈ 9.7 × 24 × 5 ≈ 1.16k currency units

This is a teaching example, not a current market quote. It excludes storage, retries, evaluation, staffing, networking, and other program costs.

## 7. Fine-tune break-even

Suppose:

- fine-tuning lifecycle cost = C_train;
- fine-tuned model saves s currency units per successful task.

Break-even successful tasks:

N_break_even = C_train / s

Example:

C_train = 1,000  
s = 0.01/task

Break-even ≈ 100,000 successful tasks.

But now add retraining cadence.

Annual training cost is approximately:

updates_per_year × full_update_lifecycle_cost

A stable behavior and a daily-changing knowledge base have very different economics.

## 8. RAG vs retraining

Suppose a content source changes U times/month.

Retraining path:

C_retrain_month ≈ U × (training + evaluation + engineering)

RAG path:

C_RAG_month ≈ indexing + request_count × retrieval_and_extra_context

The crossover depends on:

- update frequency;
- request volume;
- retrieved-token overhead;
- training cost;
- freshness requirement;
- retrieval quality;
- operational staffing.

No universal “RAG is cheaper” rule exists.

## 9. Worked application scenarios

### Scenario A — uncertain prototype

10k requests/month and uncertain product fit.

The primary economic objective is often learning speed and reversible investment, not minimum cost/request.

The experiment should measure:

- quality;
- integration time;
- time-to-first-user;
- cost of discarded work.

### Scenario B — stable high-volume workload

50M short requests/month, stable task, strict latency.

Investigate a small self-hosted or adapted model.

Compare:

- error rate;
- throughput;
- p95 latency;
- GPU utilization;
- cost per million successful tasks.

### Scenario C — frequently changing policies

500k requests/month and daily policy changes.

The architecture must make updates cheap and fast.

Measure:

- freshness after updates;
- retrieval quality;
- extra input tokens;
- p95 latency;
- cost per correctly grounded response.

## 10. Hidden TCO

| Hidden cost | Question |
|---|---|
| Evaluation | Who reruns regression after changes? |
| Security | Who performs red-team and incident response? |
| Reliability | How much capacity is reserved for peaks/failures? |
| Human review | How many expert hours per 10k tasks? |
| Data maintenance | Who cleans/re-licenses/re-indexes data? |
| Vendor migration | What is the exit cost? |
| Deprecation | How quickly can the model be replaced? |
| Opportunity cost | How much engineering time is locked in? |

These can dominate compute.

## 11. Sensitivity analysis

Never give one cost number without a scenario sweep.

Vary:

- request volume: 0.25×, 1×, 4×;
- tokens/request: 0.5×, 1×, 2×;
- hardware utilization: 25%, 50%, 75%;
- training retries: 0, 1, 2;
- update cadence: weekly vs monthly;
- evaluation/engineering overhead: 10%, 25%, 50%.

Report a range and identify the assumptions that could change the architecture.

## 12. Decision artifact

Every proposal should include:

**assumptions → equations → measured throughput → price assumptions → one-time cost → recurring cost → quality target → latency target → risk → sensitivity → break-even**

A transparent calculator is more defensible than a paragraph claiming something is cheap.

## Research exercise

Create a 24-month TCO model for:

1. hosted API;
2. self-hosted open model;
3. RAG + model.

Change one major assumption at a time and identify which assumption changes the decision.

## Laboratory

[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## Reference

Stanford CS336: https://cs336.stanford.edu/

## Deepening: compare architectures at equal useful work

Do not compare “one API call” with “one GPU hour.” Compare systems at a common workload.

Define:

**successful tasks/month**

Then calculate:

- total infrastructure cost;
- total model inference cost;
- retrieval/tool cost;
- training amortization;
- evaluation;
- engineering/operations;
- failure/retry cost.

### Worked break-even table

| Variable | Low | Base | High |
|---|---:|---:|---:|
| requests/month | 0.25× | 1× | 4× |
| input tokens | 0.5× | 1× | 2× |
| output tokens | 0.5× | 1× | 2× |
| GPU utilization | 25% | 50% | 75% |
| retraining cadence | monthly | quarterly | yearly |

Students should calculate the range rather than report a single number.

### Training-specific lesson

For an open-weight model, include:

**download/storage → adaptation → evaluation → deployment → monitoring → retraining**

The “fine-tune cost” is not the total lifecycle cost.

### Decision artifact

The final table should report:

**quality → latency → successful tasks → recurring cost → one-time cost → sensitivity → operational burden**

This makes the economics comparable across API, self-hosted, RAG, and adapted-model architectures.
