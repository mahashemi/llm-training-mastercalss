# Maintenance and Release Policy

This repository is intended to remain useful as LLM methods, models, datasets, tools, hardware, and evaluation practices evolve.

## Principles

- Prefer stable concepts over transient tooling details.
- Date time-sensitive claims.
- Version important configurations and experiments.
- Preserve historical results rather than silently rewriting them.
- Record reasons for substantive curriculum changes.
- Remove dead links and obsolete instructions.
- Keep examples runnable where practical.

## Source hierarchy

For important technical claims, prioritize:

1. primary papers;
2. official technical reports;
3. official documentation;
4. original course materials;
5. reputable secondary sources.

## Versioning

Stable curriculum releases use semantic versioning where practical:

- MAJOR: substantial restructuring or incompatible changes;
- MINOR: new lectures, chapters, labs, or major capabilities;
- PATCH: corrections, broken-link fixes, or small reproducibility fixes.

## Release checklist

Before a release:

- validate citation metadata;
- review time-sensitive claims;
- check notebook execution and links;
- review important references;
- update the changelog;
- document known limitations;
- identify significant experiment/configuration changes.

## Deprecation

When a method or tool becomes outdated:

1. mark it as historical or deprecated;
2. explain why;
3. point to the maintained alternative;
4. preserve older material when it retains educational or historical value.

## Research integrity

Do not modify historical reported results to match later findings. New evidence should be documented as a new experiment, correction, erratum, or release.

## Roadmap

Major additions should be tracked through GitHub issues, milestones, or release planning.
