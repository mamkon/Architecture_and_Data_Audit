# AI Use Declaration

CIND 820: Big Data Analytics Project
Mamkon Mercy Oyeleke | Student Number: 501279489

## AI Tools and Permitted Uses

The AI tools used in this project are Claude (Anthropic) and ChatGPT
(OpenAI), for the following purposes only:

- Brainstorming analytical approaches and structuring research questions at
  the early planning stage.
- Drafting and editing written sections for clarity, grammar, and
  professional tone, with all underlying analysis and reasoning originating
  with the student.
- Clarifying terminology, statistical concepts, and citation formatting
  conventions.
- Reviewing draft sections for structural coherence against rubric criteria.

## What AI Did Not Do

- Generate, fabricate, or supplement data or analytical results. All figures,
  tables, and statistics in this repository were produced by running the
  scripts in `notebooks/` against the raw data in `data/raw/`.
- Perform statistical calculations presented as the student's own work
  without the student running and reviewing the underlying code.
- Produce references without independent verification against the original
  source.
- Replace the student's reasoning, interpretation, or professional judgment.

## Failure-Mode Mitigations Applied This Milestone

- **Hallucinated dataset details**: every dataset reference (URLs, sheet
  names, column names, region labels) was verified by directly downloading
  and inspecting the source files (`CIHI_Wait_Times_Priority_Procedures_2025.xlsx`,
  `PHO_Chronic_Disease_Inc_Prev_Snapshot_2014_2023.xlsx`).
- **Overconfident causal framing**: the RQ3 regional join (r = 0.61, n = 6)
  is explicitly described as a preliminary signal, not a statistically
  significant finding, given the small sample size.
- **Granularity mismatch**: the audit identified that CIHI's regional
  reporting for Ontario covers only 2 of 14 indicators and uses 6 broad
  regions rather than PHO's 37 PHU geography. This constraint is documented
  in Chapter 2 and directly shapes what RQ3 can claim.

## Verification Commitment

Every result in this repository is reproducible by running the three scripts
in `notebooks/` in order, against the two files in `data/raw/`. All region
mappings, filters, and the composite burden score methodology are documented
inline in `03_pho_cihi_join_rq3.py`. The student accepts full academic
responsibility for all content in this repository.
