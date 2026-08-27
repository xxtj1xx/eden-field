from eden.stack import PRESETS, recommend
from eden.tco import PROFILES, estimate


def test_phone_preset_has_phase_one():
    recs = recommend(PRESETS["phone-8gb"])
    assert recs[0].phase.startswith("1")
    assert "llama.cpp" in recs[0].engine


def test_phone_only_tco_beats_subscription():
    result = estimate(PROFILES["phone-only"])
    assert result.cheaper == "local"
    assert result.local_total_usd < result.cloud_total_usd
