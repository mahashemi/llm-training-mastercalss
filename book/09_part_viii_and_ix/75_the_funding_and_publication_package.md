# Chapter 75 — The Funding and Publication Package

**Part:** Part IX

## 1. One project, two audiences

A funding package answers:

**Why should resources be released?**

A publication package answers:

**What does the evidence establish, and can another researcher inspect it?**

They can share experiments and artifacts, but they have different standards.

## 2. Funding package

A strong package contains:

| Section | Required evidence |
|---|---|
| Mission | measurable problem |
| Baseline | current capability + gap |
| Proposed work | experiment/system plan |
| Resources | compute/data/people |
| Budget | assumptions + TCO |
| Milestones | evidence gates |
| Risks | owners + triggers |
| Deliverables | concrete artifacts |
| Governance | data/security/release controls |

## 3. Publication package

A research package contains:

- hypothesis;
- prior work;
- method;
- exact configuration;
- dataset/version;
- model/checkpoint;
- hardware/software;
- evaluation protocol;
- statistical analysis;
- failure analysis;
- limitations;
- artifacts.

## 4. Keep the experimental unit consistent

A common failure is:

**proposal claims:** model quality  
**paper reports:** benchmark score  
**production cares about:** successful tasks and latency

Connect them.

Example:

| Level | Metric |
|---|---|
| Training | validation loss |
| Model | benchmark |
| System | grounded task success |
| Product | successful task + p95 latency + cost |

## 5. Budget-to-evidence mapping

Every budget line should have a purpose.

| Spend | Question answered |
|---|---|
| Data acquisition | Does better/targeted data close the gap? |
| Training pilot | Does the hypothesis work? |
| Scale experiment | How does quality scale? |
| Serving pilot | Can the model meet SLOs? |
| Human evaluation | Does automated score match user/domain judgment? |
| Safety work | Are critical failure modes controlled? |

This makes the proposal auditable.

## 6. Proposal reviewer objections

Prepare explicit evidence for:

- Why not an API?
- Why not RAG?
- Why not tools?
- Why not SFT/PEFT?
- Why continued pretraining?
- Why this model size?
- Why this architecture?
- Why this hardware?
- Why this budget?
- What happens if the experiment fails?

Each answer should point to a measured result, cited source, or planned experiment.

## 7. Milestone funding

A useful sequence is:

**baseline → data gate → pilot gate → scaling gate → product gate → full program**

Release additional resources only when the preceding evidence supports the next question.

## 8. Worked example

Suppose the program asks for 500k currency units.

Instead of requesting all resources immediately:

| Phase | Example allocation | Evidence |
|---|---:|---|
| Baseline/data | 50k | gap + rights + data quality |
| Training pilot | 100k | target improvement |
| Scale experiment | 125k | scaling curve |
| Product pilot | 100k | task/SLO evidence |
| Final program | 125k | integrated case |

The amounts are illustrative. The important design is the evidence-gated release.

## 9. Negative results

A failed experiment can be a useful publication artifact if it records:

- hypothesis;
- baseline;
- method;
- exact configuration;
- result;
- uncertainty;
- failure analysis;
- what the evidence rules out.

This prevents repeated mistakes.

## 10. Open science and lawful release

Release what can legally and safely be released:

- code;
- configuration;
- evaluation;
- derived statistics;
- model weights where permitted;
- data documentation;
- reproduction instructions.

When raw training data cannot be redistributed, release provenance, statistics, processing code, and reproducible access instructions where lawful.

## Research exercise

Create a complete package for one hypothetical model project:

**six-page technical proposal + one-page budget + milestone table + risk register + paper outline + reproduction manifest**

Then audit every major claim:

**measured evidence / source / assumption / unresolved experiment**

## Laboratory

[capstone_model_program.ipynb](../../notebooks/capstone_model_program.ipynb)

## Reference

https://allenai.org/olmo2
