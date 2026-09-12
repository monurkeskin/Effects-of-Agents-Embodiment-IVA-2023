"""Independent oracle: Methodology, tbl-preferences, first and second sessions."""

import json
from pathlib import Path

import pytest

from negotiator.domain import Preference
from negotiator.examples import builtin_domain

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("watermelon", "banana", "orange", "apple")
# Transcribed directly from the paper, not generated from the configuration.
TABLE = (((12, 8, 4, 1), (4, 1, 12, 8)), ((4, 1, 12, 8), (12, 8, 4, 1)))


@pytest.mark.parametrize("session", [0, 1])
@pytest.mark.parametrize("actor", ["human", "agent"])
def test_every_allocation_matches_published_points(session, actor):
    spec = json.loads(
        (ROOT / "configs/protocol-template.json").read_text(encoding="utf-8")
    )
    domain = builtin_domain("fruits")
    condition = [c for c in spec["conditions"] if not c.get("practice")][session]
    profile = Preference.from_dict(domain, condition[f"{actor}_profile"])
    points = TABLE[session][0 if actor == "human" else 1]
    count = 0
    for bid in domain.bids():
        owned = [bid[name] if actor == "human" else 4 - bid[name] for name in NAMES]
        expected = (
            sum(p * quantity for p, quantity in zip(points, owned, strict=True)) / 100
        )
        assert profile.utility(bid, actor) == pytest.approx(expected, abs=1e-12)
        count += 1
    assert count == 625


def test_no_resource_means_zero_points_not_a_rank_offset():
    spec = json.loads(
        (ROOT / "configs/protocol-template.json").read_text(encoding="utf-8")
    )
    domain = builtin_domain("fruits")
    for condition in spec["conditions"]:
        if condition.get("practice"):
            continue
        for actor, quantity in [("human", 0), ("agent", 4)]:
            profile = Preference.from_dict(domain, condition[f"{actor}_profile"])
            assert (
                profile.utility(domain.bid(dict.fromkeys(NAMES, quantity)), actor) == 0
            )
