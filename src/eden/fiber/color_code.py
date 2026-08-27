"""TIA-598 fiber color code helpers.

Standard 12-fiber buffer/tube sequence used across OSP and indoor plant.
Fiber numbers wrap every 12; tube/group numbers wrap the same way.
"""

from __future__ import annotations

TIA_598_COLORS: tuple[str, ...] = (
    "Blue",
    "Orange",
    "Green",
    "Brown",
    "Slate",
    "White",
    "Red",
    "Black",
    "Yellow",
    "Violet",
    "Rose",
    "Aqua",
)

# Common spoken nicknames in the field
ALIASES = {
    "blu": "Blue",
    "org": "Orange",
    "grn": "Green",
    "brn": "Brown",
    "slt": "Slate",
    "wht": "White",
    "red": "Red",
    "blk": "Black",
    "ylw": "Yellow",
    "vio": "Violet",
    "pnk": "Rose",
    "rose": "Rose",
    "aqua": "Aqua",
}


def color_for_fiber(fiber_number: int) -> str:
    """Return TIA-598 color for a 1-based fiber number."""
    if fiber_number < 1:
        raise ValueError("fiber_number must be >= 1")
    return TIA_598_COLORS[(fiber_number - 1) % 12]


def pair_from_fiber(fiber_number: int) -> tuple[str, str]:
    """Return (tube/group color, fiber color) for a 1-based fiber number.

    Assumes 12-fiber groups. Fiber 1-12 live in Blue tube, 13-24 Orange, etc.
    """
    if fiber_number < 1:
        raise ValueError("fiber_number must be >= 1")
    group_index = (fiber_number - 1) // 12
    fiber_index = (fiber_number - 1) % 12
    return TIA_598_COLORS[group_index % 12], TIA_598_COLORS[fiber_index]


def fiber_table(count: int = 24) -> list[dict[str, str | int]]:
    """Build a printable table of fiber #, tube color, fiber color."""
    if count < 1:
        raise ValueError("count must be >= 1")
    rows: list[dict[str, str | int]] = []
    for n in range(1, count + 1):
        tube, fiber = pair_from_fiber(n)
        rows.append({"fiber": n, "tube": tube, "color": fiber})
    return rows


def resolve_color(name: str) -> str:
    """Normalize a spoken or abbreviated color to the canonical TIA name."""
    key = name.strip().lower()
    if key in ALIASES:
        return ALIASES[key]
    for color in TIA_598_COLORS:
        if color.lower() == key:
            return color
    raise ValueError(f"Unknown color: {name}")
