# Lecture 13 — Data Sources and Dataset Construction

**Duration:** 25 minutes

## Outcome

Turn raw sources into a versioned training corpus with measurable quality, provenance, licensing, and coverage.

## 0–4 — The data paradox

Give two corpora:

**Corpus A:** 100B noisy web tokens  
**Corpus B:** 10B high-quality domain tokens

Ask which is “larger.”

Then ask which provides more useful evidence for a target task.

The lesson:

**token count is not the same as useful training signal.**

## 4–8 — Data lifecycle

**discover → acquire → rights → parse → normalize → filter → deduplicate → classify → mix → tokenize → shard → evaluate**

Every stage can change the distribution.

## 8–13 — Source quality matrix

| Source | Scale | Authority | Noise | Rights risk | Processing |
|---|---|---|---|---|---|
| curated books | medium | high | low | high | OCR/licensing |
| government docs | medium | high | low | varies | parsing |
| web | huge | mixed | high | varies | heavy filtering |
| community | small/medium | mixed | mixed | contributor terms | review |
| synthetic | huge | teacher-dependent | correlated | model terms | filtering |

Students should score sources explicitly rather than calling the corpus “high quality.”

## 13–17 — Dataset accounting

For each source track:

- raw tokens;
- post-filter tokens;
- post-dedup tokens;
- language;
- domain;
- time;
- license;
- synthetic fraction.

Worked example:

Raw = 20B  
filter survival = 60% → 12B  
dedup survival = 75% → 9B

Only **9B usable tokens** enter the final mix.

## 17–20 — Governance and contamination

Create:

**source ID → rights status → dataset version → training run**

Exclude protected evaluation data.

Test exact and near-duplicate overlap before training.

## 20–22 — Data as an experiment

Change one data variable:

- filter threshold;
- source mixture;
- synthetic fraction;
- dedup threshold.

Keep model/training/evaluation fixed.

Measure:

**validation loss + target score + language slices + cost**

## 22–24 — Failure analysis

If quality improves:

Ask:

- Did useful sources increase?
- Did the model simply see more tokens?
- Did benchmark leakage increase?
- Did one language dominate?

If quality falls:

- inspect rejected sources;
- inspect language distribution;
- inspect duplicate rates;
- compare source-by-source contributions.

## 24–25 — Exit challenge

Build a mini data card containing:

**sources → rights → raw tokens → usable tokens → quality → mixture → evaluation → limitations**

### Research bridge

Use Stanford CS336 data-processing material as the implementation reference:
https://cs336.stanford.edu/
