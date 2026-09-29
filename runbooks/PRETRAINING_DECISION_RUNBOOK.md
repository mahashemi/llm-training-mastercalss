# Pretraining Decision Runbook

## Gate 0 — Do we actually need pretraining?

Before committing to pretraining, test prompting, structured outputs, tools, RAG, SFT/PEFT, and continued pretraining against the actual requirement.

## Gate 1 — Define the capability

Write measurable target capabilities and unacceptable failures.

## Gate 2 — Build evaluation first

Create frozen development and holdout evaluation sets before the expensive run.

## Gate 3 — Inventory data

Record source, license/rights, language, domain, token count, quality, duplication, and provenance.

## Gate 4 — Decide model/data budget

Estimate compute using `C ≈ 6ND` as a first-order dense-LM estimate, then apply architecture/system overheads and a contingency budget.

## Gate 5 — Run scaling experiments

Train several smaller models/data budgets to determine whether the planned allocation behaves as expected.

## Gate 6 — Production pretraining

Lock configuration, checkpointing, monitoring, evaluation cadence, and rollback/recovery procedures.

## Gate 7 — Post-training

Use SFT and preference methods as appropriate; do not use post-training to compensate for a fundamentally inadequate pretraining corpus when the problem is broad language modeling capability.

## Gate 8 — Release decision

Require evaluation, safety review, licensing/provenance review, deployment validation, and a maintenance plan.


## Pretraining decision gate

Before requesting from-scratch compute, document:

1. capability gap;
2. strongest existing-model baseline;
3. RAG/tool baseline where applicable;
4. SFT/PEFT result;
5. continued-pretraining result if representation is suspected;
6. tokenizer and data evidence;
7. scaling-law/resource evidence;
8. distributed throughput/recovery evidence;
9. data rights/governance;
10. staffing and operational ownership.

### Kill criteria

Define measurable conditions such as:

- insufficient target-language/domain gain;
- unacceptable retained-capability regression;
- throughput below economic requirement;
- unresolved data rights;
- inability to evaluate reliably.

### Decision artifact

Produce:

**evidence → remaining uncertainty → proposed run → resources → success gate → fallback → kill criterion**
