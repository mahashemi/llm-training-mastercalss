# Chapter 61 — API Privacy and Data Governance

**Part:** Part VII

## 1. Treat the data path as part of architecture

An API architecture is not simply:

user → model → answer

It is:

**user data → application → provider boundary → model → logs/telemetry → downstream systems**

The decision requires a data-flow map.

## 2. Data-boundary matrix

| Data class | Example | Question before sending |
|---|---|---|
| Public | published article | Can it be sent without restriction? |
| Internal | operating procedure | Is external processing allowed? |
| Confidential | customer record | What contractual/control boundary applies? |
| Sensitive | health/financial data | What minimization, access, retention, and security controls are required? |
| Secret | credentials | Should never enter model context |

Do not put secrets into prompts simply because a model can process them.

## 3. Provider review checklist

Record, for the exact service and contract:

- data retention;
- use of submitted data;
- logging;
- training/feedback use;
- region/location;
- encryption;
- access controls;
- deletion behavior;
- incident handling;
- subprocessors;
- audit/contract terms;
- version/deprecation policy.

These are provider-specific and change over time. Capture the date and source of every assumption.

## 4. Minimize before you transmit

A practical transformation is:

raw record → select required fields → redact/minimize → authorization check → model request

Example:

Instead of sending a complete patient record for a question about appointment scheduling, send only the fields required by the scheduling workflow.

Data minimization reduces:

- privacy exposure;
- token cost;
- accidental leakage;
- debugging burden.

## 5. RAG privacy architecture

RAG does not automatically solve privacy.

The correct boundary is:

**identity → authorization filter → retrieval → permitted evidence → model context**

Do not retrieve first and filter later if unauthorized text could already reach the model.

Test with synthetic records that deliberately share similar terms but have different access permissions.

## 6. Tool privacy and side effects

Tools may expose more sensitive information than the model itself.

For every tool define:

- who can call it;
- which resources it can access;
- read vs write;
- maximum scope;
- audit record;
- confirmation requirement;
- failure behavior.

A model should not be granted a broader permission scope than the user or workflow requires.

## 7. API vs self-hosted governance

| Dimension | External API | Self-hosted |
|---|---|---|
| Data leaves organization | potentially | can avoid |
| Infrastructure control | lower | higher |
| Security responsibility | shared | more internal responsibility |
| Provider dependency | higher | lower |
| Operational burden | lower infrastructure burden | higher infrastructure burden |
| Migration path | provider-specific | model/stack-specific |
| Audit model | contract + logs + provider controls | internal controls + infra audit |

Neither architecture is automatically safer. The relevant question is **which boundary meets the actual policy and risk requirements**.

## 8. Worked example

Requirement:

“Analyze internal clinical notes and produce a structured summary.”

Data-flow choices:

### Option A — external API

Requires explicit review of:

- allowed data;
- provider controls;
- retention;
- logging;
- region;
- contract.

### Option B — local model

Requires:

- local inference;
- GPU capacity;
- model lifecycle;
- patching;
- monitoring;
- access controls.

The correct decision compares both the data boundary **and** the engineering TCO.

## 9. Governance tests

Create automated assertions for:

**Access:** unauthorized user cannot retrieve protected source.

**Minimization:** prohibited field never enters the model request.

**Retention:** logs do not contain fields that policy prohibits.

**Deletion:** deleted source no longer appears in retrieval results.

**Audit:** every sensitive action has an attributable event.

These should be tested like software.

## 10. Risk-based decision matrix

| Condition | Extra control |
|---|---|
| public data | standard controls |
| internal data | provider/contract review |
| sensitive data | minimization + access + audit |
| high-impact decision | human review + strong evaluation |
| irreversible action | explicit confirmation + deterministic control |

The exact controls depend on applicable law, policy, contract, and system context.

## Research exercise

Draw a data-flow diagram for:

**user → app → API → RAG → tool → database**

Label every boundary with:

- data class;
- authorization;
- encryption;
- logging;
- retention;
- responsible owner.

Then identify the three highest-impact controls and write tests for them.

## Laboratory

[build_vs_buy_decision_lab.ipynb](../../notebooks/build_vs_buy_decision_lab.ipynb)

## Reference

https://cs336.stanford.edu/
