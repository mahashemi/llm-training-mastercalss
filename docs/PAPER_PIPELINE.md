# From Experiment to Paper

This repository is structured so practical work can become research output.

## Pipeline

Question → hypothesis → baseline → controlled experiment → ablation → failure analysis → result artifact → paper

## 1. Start with a claim

Write one falsifiable claim.

Bad:
> Better data improves the model.

Better:
> Removing near-duplicate web documents while holding the training token budget constant improves held-out domain perplexity without reducing multilingual capability beyond a predeclared tolerance.

## 2. Freeze the baseline

Record model/revision, tokenizer, dataset/version, evaluation suite, decoding settings, hardware, software, and random seeds where relevant.

## 3. Run the minimum informative experiment

Prefer a cheap pilot before a large run. Ask: What is the smallest experiment that could make me abandon this hypothesis?

## 4. Add an ablation

Remove or change the proposed mechanism while preserving everything else as far as practical.

## 5. Analyze failures

Publish representative failures, not only aggregate scores. Separate data, optimization, capability, evaluation, and systems failures.

## 6. Produce artifacts

At minimum: configuration, metrics, figure, table, experiment card, limitations, and reproduction instructions.

## 7. Draft the paper

Use templates/paper_report.md. Recommended sections: abstract, problem, related work, method, data, experiment, results, ablations, failure analysis, limitations, reproducibility, discussion.

## 8. Cite correctly

Cite the underlying scientific papers and this repository when both materially contributed. Use a specific release or commit of this repository.

## 9. Archive

For stable work: create a GitHub release, archive the release with a DOI service, and record the DOI and release in the paper.

## Research integrity

- Do not change evaluation after seeing results without labeling the change.
- Do not hide failed runs that materially affect interpretation.
- Do not overstate a benchmark result as evidence of a broader capability.
- Distinguish measurement from hypothesis.
- Record known limitations.