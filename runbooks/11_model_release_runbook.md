# Model Release Runbook

## Objective

Release a model/checkpoint with enough evidence that users and researchers can understand what it is, what it can do, and how it was produced.

## Identity
- [ ] model name/version
- [ ] base model/revision
- [ ] tokenizer/revision
- [ ] parameter count
- [ ] training/post-training stages

## Data
- [ ] dataset version
- [ ] provenance
- [ ] license/access basis
- [ ] synthetic-data disclosure
- [ ] sensitive-data review

## Evaluation
- [ ] predeclared evaluation suite
- [ ] baseline comparison
- [ ] task-level results
- [ ] safety/robustness results
- [ ] multilingual results where relevant
- [ ] representative failure cases

## Reproducibility
- [ ] code commit
- [ ] configuration
- [ ] environment
- [ ] hardware
- [ ] random seeds where relevant
- [ ] reproduction instructions

## Serving
- [ ] supported precision
- [ ] inference requirements
- [ ] latency/throughput measurements
- [ ] known serving limitations

## Documentation
- [ ] model card
- [ ] dataset card
- [ ] citation information
- [ ] limitations
- [ ] license/usage constraints

## Block release when

- evaluation is not trustworthy;
- provenance is unresolved;
- critical safety findings are unknown;
- the artifact cannot be identified reproducibly;
- usage rights are unclear.

Use a Git tag/release and archive stable releases with a DOI service where possible.


## Release artifact checklist

A releasable model package should identify:

- model ID and revision;
- tokenizer;
- license;
- training method;
- dataset description and rights basis;
- configuration;
- evaluation protocol;
- known limitations;
- safety/robustness results;
- intended usage;
- adapter/base relationship if PEFT;
- quantization details if quantized;
- reproducibility metadata.

### Reproducibility test

From a clean environment:

1. obtain the documented base/model artifact;
2. obtain tokenizer/config;
3. load the model;
4. reproduce a small inference set;
5. reproduce the headline evaluation where feasible.

### Release gates

Do not publish based on one benchmark. Require target quality, protected regressions, critical safety checks, and artifact integrity.
