from eden.fiber.color_code import color_for_fiber, pair_from_fiber
from eden.fiber.loss_budget import LossBudgetInput, calculate_loss_budget


def test_first_twelve_colors():
    assert color_for_fiber(1) == "Blue"
    assert color_for_fiber(12) == "Aqua"
    assert color_for_fiber(13) == "Blue"


def test_tube_wraps_with_group():
    tube, fiber = pair_from_fiber(13)
    assert tube == "Orange"
    assert fiber == "Blue"


def test_loss_budget_1550():
    result = calculate_loss_budget(
        LossBudgetInput(length_km=10, wavelength_nm=1550, connectors=2, splices=4)
    )
    # 10 * 0.25 + 2*0.5 + 4*0.1 + 2.0 = 2.5 + 1 + 0.4 + 2 = 5.9
    assert result.total_db == 5.9
    assert result.fiber_loss_db == 2.5
