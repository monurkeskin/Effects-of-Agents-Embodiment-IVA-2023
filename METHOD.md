# Method and evidence

Associated paper: [Effects of Agent's Embodiment in Human-Agent Negotiations](https://doi.org/10.1145/3570945.3607362).

## Scientific contract

Hybrid bidding with additive fruit utility; physical NAO versus recorded virtual embodiment.

Two counterbalanced fifteen-minute main sessions, five-minute break, practice before each, 40-point target. Exclude a participant pair if either negotiation has fewer than five individual committed offers (human and agent combined).

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

The paper's five-round exclusion uses **individual offers**, confirmed by the
maintainer on 13 September 2026 and consistent with the historical offer counter.
With human-first alternation, the third human offer is the fifth offer and meets
this criterion. Acceptance, readiness signals and rejected input are not additional
offers. If either main session has fewer than five, exclude the entire participant
pair. This definition is specific to this paper; it does not determine later studies'
use of the word "round". See the boundary and journal tests in
[test_offer_exclusion.py](tests/test_offer_exclusion.py).

- Original practice task, instructions/video, seventeen-item instruments and licensed virtual embodiment assets.
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

## Presentation choices and historical differences

The generic policy retains the inspected legacy branch's .60/.73/.86 warning
schedule. The paper describes .40/.60/.80 and uses Hopeful/Pleased where the
branch uses Convinced/Content. Those maintained choices remain explicit; a common
agent API does not make the two schedules or mood vocabularies equivalent.
The old branch also selects successive gesture files per mood. The current bridge
uses a configured map, so it does not reconstruct the original clip sequence.
