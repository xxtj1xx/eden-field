"""Rough 3-year total cost of ownership for a local inference path.

These are planning numbers, not a finance model. Override any line
when you have a real quote.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TCOInput:
    hardware_usd: float
    yearly_power_kwh: float
    usd_per_kwh: float = 0.16
    yearly_maintenance_usd: float = 50.0
    years: int = 3
    cloud_alternative_monthly_usd: float = 20.0


@dataclass(frozen=True)
class TCOResult:
    hardware_usd: float
    power_usd: float
    maintenance_usd: float
    local_total_usd: float
    cloud_total_usd: float
    delta_usd: float
    cheaper: str


def estimate(inp: TCOInput) -> TCOResult:
    if inp.years < 1:
        raise ValueError("years must be >= 1")
    power = inp.yearly_power_kwh * inp.usd_per_kwh * inp.years
    maint = inp.yearly_maintenance_usd * inp.years
    local = inp.hardware_usd + power + maint
    cloud = inp.cloud_alternative_monthly_usd * 12 * inp.years
    delta = local - cloud
    cheaper = "local" if local < cloud else "cloud"
    if abs(delta) < 1:
        cheaper = "toss-up"
    return TCOResult(
        hardware_usd=round(inp.hardware_usd, 2),
        power_usd=round(power, 2),
        maintenance_usd=round(maint, 2),
        local_total_usd=round(local, 2),
        cloud_total_usd=round(cloud, 2),
        delta_usd=round(delta, 2),
        cheaper=cheaper,
    )


# Reference profiles a splicer might actually buy
PROFILES = {
    "phone-only": TCOInput(
        hardware_usd=0,  # already own the work phone
        yearly_power_kwh=15,  # extra charging from local inference
        yearly_maintenance_usd=0,
        cloud_alternative_monthly_usd=20,
    ),
    "used-mini-pc": TCOInput(
        hardware_usd=350,
        yearly_power_kwh=175,  # ~20W average
        yearly_maintenance_usd=40,
        cloud_alternative_monthly_usd=20,
    ),
    "used-gpu-box": TCOInput(
        hardware_usd=900,
        yearly_power_kwh=700,  # 80W average if you leave it up
        yearly_maintenance_usd=80,
        cloud_alternative_monthly_usd=20,
    ),
}
