"""The 2023 exclusion rule counts offers, while inference pairs participants."""

import json
from pathlib import Path

import pytest

from negotiator.application.session import Session, SessionConfig
from negotiator.domain.actions import Accept, Offer
from negotiator.events.projection import replay
from negotiator.examples import builtin_domain, example_profiles
from negotiator.reproduction.operations import paired_summary

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("short_condition", ["NAO", "Virtual representation"])
@pytest.mark.parametrize("offers, included", [(4, False), (5, True), (6, True)])
def test_fifth_individual_offer_meets_the_paired_exclusion_rule(short_condition, offers, included):
    schedule = json.loads((ROOT / "protocol-schedule.json").read_text())
    assert schedule["round_definition"] == "individual-offers"
    recipe = json.loads((ROOT / "reproduction/paired-example.json").read_text())
    assert (
        recipe["parameters"]["minimum_rounds"] == schedule["minimum_rounds_in_either_session"] == 5
    )
    records = [
        {
            "study_id": "boundary-fixture",
            "participant_id": "synthetic-pair",
            "session_id": condition,
            "condition": condition,
            "cohort": "synthetic",
            "domain": "fruits",
            "rounds": offers if condition == short_condition else 6,
            "utility": 0.6,
        }
        for condition in recipe["parameters"]["conditions"]
    ]
    result = paired_summary({"records": records}, recipe["parameters"]).results
    assert result["complete_pairs"] == int(included)
    assert len(result["excluded_pairs"]) == int(not included)
    if not included:
        assert result["excluded_pairs"][0]["reason"] == "below_prespecified_round_threshold"


def test_confirmed_offer_definition_no_longer_requires_an_external_file():
    spec = json.loads((ROOT / "configs/protocol-template.json").read_text())
    assert all(
        "definition of a round" not in r["description"] for r in spec["protocol"]["requirements"]
    )


@pytest.mark.parametrize("offer_count", [4, 5])
def test_acceptance_does_not_add_an_offer_or_change_the_exclusion_boundary(tmp_path, offer_count):
    domain = builtin_domain("fruits")
    human, agent = example_profiles(domain)
    session = Session.create(tmp_path, SessionConfig("synthetic", "P1", "S1"), human, agent)
    bid = next(domain.bids())
    for index in range(offer_count):
        actor = "human" if index % 2 == 0 else "agent"
        identity = f"offer-{index}"
        session.submit(Offer(identity, actor, bid), identity)
    acceptor = "human" if offer_count % 2 == 0 else "agent"
    session.submit(Accept(acceptor, f"offer-{offer_count - 1}"), "accept")
    restored = replay(session.journal.read())
    assert restored.outcome["reason"] == "agreement"
    assert len(restored.offers) == offer_count
    assert sum(e.kind == "offer.committed" for e in session.journal.read()) == offer_count
