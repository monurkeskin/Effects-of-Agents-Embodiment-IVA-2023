# Analyze this paper's session records

The analysis unit is the **participant**. Two counterbalanced fifteen-minute main sessions, five-minute break, practice before each, 40-point target. Exclude a participant pair if either negotiation has fewer than five individual committed offers (human and agent combined).

## Available example

```bash
negotiator reproduce reproduction/paired-example.json --output paired-output
```

The three synthetic participant pairs have differences 0.4, 0.1 and -0.2; their
mean is 0.1. This number is a hand-checkable fixture, not a result from the paper.
`paired-output/results.csv` contains computed group summaries and interval bounds;
`table.tex` formats those same values and `paired-contrasts.svg`/`.pdf` plots them.
Rounding is applied only when formatting the table. Full precision remains in JSON/CSV.

## Input dictionary

For the paper's normalized product score, use `normalized_utility_product` from
the framework's session report. It is `(U_h * U_a) / max_b(U_h(b) * U_a(b))`.
The denominator is recomputed from each recorded profile and outcome space; both
published fruit profiles give 0.64 across their 625 allocations. The separate
`utility_sum` field is not the paper's normalized product. The source is the
Evaluation section, paragraph defining the normalized utility product in the
[IVA 2023 paper](https://doi.org/10.1145/3570945.3607362).

`tests/test_paper_profiles.py` checks both complete outcome spaces against an
independent points-table calculation. This establishes the measure's arithmetic,
not the original participant averages or inferential results. Supply the selected
measure explicitly to an analysis recipe; the existing paired example remains a
synthetic utility fixture.

| Field | Meaning |
| --- | --- |
| `study_id`, `participant_id`, `session_id` | Stable identities; participants are paired within one study |
| `condition`, `cohort`, `domain` | Experimental condition and distinct design groups |
| `rounds` | Legacy column name: number of individual committed human and agent offers combined |
| `utility` | Selected normalized outcome measure in [0,1], or null when missing |
| `practice` | Excluded from main-condition inference |

Choose explicitly whether the intended outcome is raw agreement utility or the
game payoff. Failure/no agreement and missing/incomplete measurement are different
states. Never turn missing data into zero. The example rejects duplicated session
or participant-condition identities; it excludes the complete pair when either
required member is missing or contains fewer than five individual offers. Acceptance
does not add an offer. A third human offer in human-first alternation is the fifth
offer and passes this criterion. Do not divide the count by two for this paper;
the independent analysis unit remains the participant, not the offer.

Cohorts and domains remain separate unless a protocol justifies a named domain
mapping. Inspect counts and exclusion reasons before any inference. Do not select a
significance test by searching for a favorable result. The paper's original decisions
and records are required to claim exact recomputation of its tables or figures.
The modern percentile bootstrap in the example is a separate declared analysis.
