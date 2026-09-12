"""Paper-specific study contracts, independently executable without a robot."""

import json
from pathlib import Path
import pytest
from negotiator.application.contracts import StudySpec
from negotiator.application.protocol import (
    ordered_conditions,
    protocol_digest,
    protocol_readiness,
)

ROOT = Path(__file__).resolve().parents[1]
CONFIGS = list((ROOT / "configs").glob("protocol*.json"))


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_published_templates_pin_behavior_and_expose_unrecovered_evidence(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    assert spec.purpose == "published-protocol"
    assert spec.protocol.configuration_sha256 == protocol_digest(spec)
    assert spec.protocol.requirements
    assert protocol_readiness(spec), (
        "Historical evidence is still unrecovered; do not imply a runnable original experiment."
    )
    assert not spec.synthetic


def test_demo_is_explicit_and_device_free():
    spec = StudySpec.model_validate_json(
        (ROOT / "configs/synthetic.json").read_text(encoding="utf-8")
    )
    assert spec.purpose == "demonstration"
    assert spec.synthetic
    assert spec.output == "text"
    assert all(c.output in (None, "text", "avatar") for c in spec.conditions)
    assert not spec.speech_device and not spec.perception_device


def test_embodiment_practice_blocks_and_timed_break():
    spec = StudySpec.model_validate_json(
        (ROOT / "configs/protocol-template.json").read_text(encoding="utf-8")
    )
    conditions = ordered_conditions(spec)
    assert [c["practice"] for c in conditions] == [True, False, True, False]
    assert [c["duration_seconds"] for c in conditions] == [300, 900, 300, 900]
    assert conditions[1]["break_after_seconds"] == 300
    assert spec.order == "counterbalanced"
    assert spec.position_profiles[0].human_profile["weights"]["watermelon"] == 0.48
    reversed_spec = spec.model_copy(update={"participant_index": 2})
    reversed_conditions = ordered_conditions(reversed_spec)
    assert reversed_conditions[1]["label"] != conditions[1]["label"]
    assert reversed_conditions[1]["human_profile"] == conditions[1]["human_profile"]


@pytest.mark.parametrize("path", CONFIGS, ids=lambda p: p.stem)
def test_paper_score_target_does_not_prohibit_below_target_agreement(path):
    spec = StudySpec.model_validate_json(path.read_text(encoding="utf-8"))
    for condition in spec.conditions:
        if condition.practice:
            continue
        assert condition.human_profile["reservation"] == 0
        assert condition.score_targets["human"] == 0.4
        assert condition.reward_minimums == {"human": 0.4}
