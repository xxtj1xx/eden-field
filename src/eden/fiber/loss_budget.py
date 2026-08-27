"""Simple optical loss budget calculator.

Numbers are conservative field defaults, not a substitute for the
manufacturer spec sheet or the carrier's design package. Tune the
constants if your plant uses different connectors, splices, or fiber.
"""

from __future__ import annotations

from dataclasses import dataclass


# Default unit losses (dB). These are typical planning values.
DEFAULT_CONNECTOR_DB = 0.50
DEFAULT_SPLICE_DB = 0.10
DEFAULT_SAFETY_MARGIN_DB = 2.00

# Attenuation defaults by wavelength (dB/km)
ATTEN_DB_PER_KM = {
    1310: 0.35,
    1550: 0.25,
    1625: 0.28,
}


@dataclass(frozen=True)
class LossBudgetInput:
    length_km: float
    wavelength_nm: int = 1550
    connectors: int = 2
    splices: int = 0
    connector_db: float = DEFAULT_CONNECTOR_DB
    splice_db: float = DEFAULT_SPLICE_DB
    safety_margin_db: float = DEFAULT_SAFETY_MARGIN_DB
    fiber_db_per_km: float | None = None


@dataclass(frozen=True)
class LossBudgetResult:
    fiber_loss_db: float
    connector_loss_db: float
    splice_loss_db: float
    safety_margin_db: float
    total_db: float
    atten_used_db_per_km: float


def calculate_loss_budget(inp: LossBudgetInput) -> LossBudgetResult:
    if inp.length_km < 0:
        raise ValueError("length_km cannot be negative")
    if inp.connectors < 0 or inp.splices < 0:
        raise ValueError("connectors and splices must be >= 0")

    atten = inp.fiber_db_per_km
    if atten is None:
        atten = ATTEN_DB_PER_KM.get(inp.wavelength_nm)
        if atten is None:
            raise ValueError(
                f"No default attenuation for {inp.wavelength_nm} nm. "
                "Pass fiber_db_per_km explicitly."
            )

    fiber_loss = inp.length_km * atten
    connector_loss = inp.connectors * inp.connector_db
    splice_loss = inp.splices * inp.splice_db
    total = fiber_loss + connector_loss + splice_loss + inp.safety_margin_db

    return LossBudgetResult(
        fiber_loss_db=round(fiber_loss, 3),
        connector_loss_db=round(connector_loss, 3),
        splice_loss_db=round(splice_loss, 3),
        safety_margin_db=round(inp.safety_margin_db, 3),
        total_db=round(total, 3),
        atten_used_db_per_km=atten,
    )
