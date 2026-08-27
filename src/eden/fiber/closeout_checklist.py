"""Generic fiber closeout checklist.

This is a field-usable starting point, not a carrier-specific packet.
SpliceFlow (https://spliceflow.app) is the productized job/closeout
workflow. This list exists so a splicer standing in a vault with no
signal still has the questions that keep as-builts from falling apart.
"""

from __future__ import annotations

from datetime import date

CLOSEOUT_ITEMS: tuple[tuple[str, str], ...] = (
    ("job", "Job / WO / project ID written on every page and photo set"),
    ("site", "Site, address, and hut/CO/enclosure ID confirmed"),
    ("gps", "GPS captured at enclosure and slack storage"),
    ("before", "Before photos: existing plant, labels, damage, access"),
    ("open", "Enclosure opened photos: trays, buffer tubes, grounding"),
    ("splice", "Splice tray photos after heat shrink, lids on, fibers dressed"),
    ("labels", "Tube, binder, and port labels match the splice matrix"),
    ("matrix", "Splice matrix filled: fiber #, tube color, destination"),
    ("otdr", "OTDR traces saved per span, correct wavelength and pulse"),
    ("power", "Power meter / light source readings if required by spec"),
    ("loss", "Measured loss vs design budget recorded"),
    ("slack", "Slack loops stored, not pinched, radius respected"),
    ("ground", "Grounding / bonding verified where metallic plant exists"),
    ("weather", "Enclosure sealed, grommets seated, no unplugged ports"),
    ("after", "After photos: closed case, lock, restored site"),
    ("waste", "Fiber scraps and alcohol wipes packed out"),
    ("packet", "Photos + traces + matrix staged for the closeout packet"),
)


def checklist_markdown(
    job_id: str = "",
    site: str = "",
    tech: str = "",
    day: str | None = None,
) -> str:
    """Render a printable markdown checklist."""
    when = day or date.today().isoformat()
    lines = [
        "# Fiber Closeout Checklist",
        "",
        f"- Job: {job_id or '_'} ",
        f"- Site: {site or '_'} ",
        f"- Tech: {tech or '_'} ",
        f"- Date: {when}",
        "",
        "| Done | Item |",
        "| --- | --- |",
    ]
    for _key, label in CLOSEOUT_ITEMS:
        lines.append(f"| [ ] | {label} |")
    lines.append("")
    lines.append("_Project Eden — open field tools. Not a substitute for the carrier spec._")
    lines.append("")
    return "\n".join(lines)
