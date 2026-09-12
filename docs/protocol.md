# Configure and conduct this protocol

Two counterbalanced fifteen-minute main sessions, five-minute break, practice before each, 40-point target. Exclude a participant if either negotiation has fewer than five rounds.

## First inspection

Run `negotiator gui`, open **New study**, import `configs/protocol-template.json`, and inspect
Study, Preferences, Sessions and Review. The conductor sees protocol readiness;
the participant sees only their own preferences, offers, timer and current phase.
Use pseudonymous participant IDs. The application serves the two views locally,
including separate monitors; it is not a remote Internet study service.

| Position | Condition | Role | Deadline | Following break |
| --- | --- | --- | --- | --- |
| 1 | Illustrative practice 1 | practice | 300 s | 0 s |
| 2 | NAO | main | 900 s | 300 s |
| 3 | Illustrative practice 2 | practice | 300 s | 0 s |
| 4 | Virtual representation | main | 900 s | 300 s |

Alternative order files are listed in [CONFIGURATIONS](../CONFIGURATIONS.md).
Where profiles change by position, changing condition order does not swap the
position-specific score table. Practice blocks remain attached to their main
condition. The break follows the preceding session's result and any scheduled
questionnaire. A restart conservatively restarts the full break and records this fact.

## Before using a published-protocol template

- Original practice task, instructions/video, seventeen-item instruments and licensed virtual embodiment assets.
- Historical definition of a round and its session-record conversion.
- Permitted complete paired records and original exclusion ledger.

The templates contain hash-pinned scientific configuration and named evidence
requirements. Supply only validated local files and their SHA-256 for the appropriate
requirement. File integrity alone does not establish scientific or hardware validity.
Resolve the method/protocol choices and configure approved questionnaire wording and
timing before starting. [protocol-schedule.json](../protocol-schedule.json) records
what is known and unknown. Missing original questionnaire text is not replaced with
invented questions. Synthetic examples remain demonstrations.

## During and after the session

Use **Start session** after preferences and required surveys. Follow the selected
turn protocol. Notifications and rejected offers do not create additional offers.
Duplicate or delayed commands must refer to the same session and displayed offer.
The application records agreement, deadline, withdrawal, interruption and operator
termination distinctly. A recording failure requires conductor attention before
continuing; restarting an interrupted session does not invent elapsed time.

After completion use **Build report**, or run `negotiator report PATH --output NEW_DIR`.
Keep original records and the generated report together, and export citations using
`negotiator cite PATH --format bibtex`. [Analysis guide](analysis.md).
