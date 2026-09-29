# Funding and Program Proposal Runbook

## Objective

Convert technical evidence into a fundable, measurable LLM program.

## Required sections

1. problem and users;
2. baseline;
3. measurable target;
4. data/resource constraints;
5. technical approach;
6. experiments already completed;
7. compute and infrastructure;
8. staffing;
9. safety/governance;
10. budget;
11. milestones;
12. risks and kill criteria;
13. publication/open-science plan.

## Evidence standard

Every major claim must be:
- measured by the team;
- sourced to an authoritative reference; or
- labeled as an assumption/forecast.

## Budget structure

Separate:
- accelerator compute;
- storage/network;
- software;
- personnel;
- data acquisition/curation;
- evaluation;
- security/governance;
- contingency.

## Milestone logic

Each funding tranche should buy a measurable artifact.

Example:

| Stage | Artifact | Gate |
|---|---|---|
| 0 | baseline system | target metrics defined |
| 1 | data pilot | quality/provenance accepted |
| 2 | training pilot | measurable gain |
| 3 | scale run | resource/quality economics demonstrated |
| 4 | deployment | SLA/safety evaluation passed |

## Final question

> What would cause us to stop spending?

A serious proposal answers this explicitly.


## Evidence-first proposal protocol

### Section 1 — Mission

Write the user/task/capability gap without choosing a model first.

### Section 2 — Baseline

Document the strongest tested existing approach, including RAG/tools where relevant.

### Section 3 — Evidence ladder

Show the progression:

**baseline → small intervention → measured gain → remaining gap → next experiment**

### Section 4 — Resources

Derive:

**tokens/model → FLOPs → measured throughput → wall time → accelerator-hours → infrastructure → staffing → TCO**

### Section 5 — Gates

For every funding milestone define:

**success metric + threshold + artifact + owner + next release condition**

### Section 6 — Failure plan

State:

- kill criteria;
- fallback;
- data/rights risks;
- budget ceiling;
- recovery plan.

A fundable proposal is a sequence of testable claims, not a large hardware request.
