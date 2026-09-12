# Method and evidence

Associated paper: [Effects of Agent's Embodiment in Human-Agent Negotiations](https://doi.org/10.1145/3570945.3607362).

## Scientific contract

Hybrid bidding with additive fruit utility; physical NAO versus recorded virtual embodiment.

Two counterbalanced fifteen-minute main sessions, five-minute break, practice before each, 40-point target. Exclude a participant if either negotiation has fewer than five rounds.

The machine-readable [paper map](paper-map.json) links selected manuscript labels,
source hashes and locations to implementation, independent tests, configurations
and result targets. Only the selected active LaTeX entry was used. Manuscript
working files, inactive drafts and reviewer correspondence are not redistributed.


## Point-profile correction

The earlier maintained template contained synthetic rank profiles. Release 2.0
uses the published `tbl-preferences`: first-session human points (12,8,4,1),
agent (4,1,12,8), in watermelon/banana/orange/apple order; the second session swaps
these assignments. All 625 allocations per actor/session are checked independently.
No resources means zero additive points. Profiles follow session position when
embodiment order changes. The browser avatar is a functional demo, not the historical
recorded virtual embodiment.

## Utility, targets and game scores

A bid always states the human share. Agent utility uses the complementary allocation.
Utility is computed at full precision; rendering multiplies by 100 for display.
A target score is distinct from a reservation constraint. In the fruit papers,
a human agreement below 40 points is permitted but earns zero game points;
raw utility and game payoff remain separate logged fields. The Jennifer papers'
30-point goal is not silently turned into a prohibition on lower agreements.
The short Solver and Appearance examples do not claim those fruit reward rules.

## Remaining evidence gaps

The generic mood policy preserves the inspected legacy experiment branch's
warning schedule (.60, .73, .86), whereas the paper describes .40, .60 and .80.
The branch uses Convinced/Content labels where the paper uses Hopeful/Pleased.
These are presentation differences to resolve against the study configuration,
not consequences of restricted participant-data access. The original branch also
selects successive gesture files per mood; the maintained bridge uses a configured
mapping and does not recreate that sequence automatically.

- Original practice task, instructions/video, seventeen-item instruments and licensed virtual embodiment assets.
- Historical definition of a round and its session-record conversion.
- Permitted complete paired records and original exclusion ledger.

Unknown inputs are not filled with simulated participants or invented historical
constants. The existing templates are inspectable, but their published-protocol
preflight prevents starting before required evidence is supplied and reviewed.
A custom study has its own declared configuration and cannot inherit a reproduction
claim merely by using the same strategy name.

## Relationship to the research series

The same 625-allocation fruit score tables are reused by the 2025 study. This does not make embodiment and emotion conditions equivalent.

The common engine owns utility, lifecycle, logs, GUI, shared methods and device
contracts. This repository owns paper-specific profiles, protocol choices, analysis
rules, reproduction targets and tests. [framework.json](framework.json) pins the
engine; [NOTICE](NOTICE) preserves original source attribution.
