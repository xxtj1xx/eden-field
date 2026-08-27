"""Project Eden command line."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from eden import __version__
from eden.fiber.closeout_checklist import checklist_markdown
from eden.fiber.color_code import TIA_598_COLORS, color_for_fiber, fiber_table, pair_from_fiber
from eden.fiber.loss_budget import LossBudgetInput, calculate_loss_budget
from eden.stack import PRESETS, recommend
from eden.tco import PROFILES, TCOInput, estimate


def _cmd_version(_args: argparse.Namespace) -> int:
    print(f"project-eden {__version__}")
    return 0


def _cmd_colors(args: argparse.Namespace) -> int:
    if args.fiber:
        tube, color = pair_from_fiber(args.fiber)
        print(f"Fiber {args.fiber}: tube {tube} / fiber {color}")
        return 0
    rows = fiber_table(args.count)
    print(f"{'#':>4}  {'TUBE':<10} {'FIBER':<10}")
    for row in rows:
        print(f"{row['fiber']:>4}  {row['tube']:<10} {row['color']:<10}")
    if args.legend:
        print("\nTIA-598 sequence: " + ", ".join(TIA_598_COLORS))
    return 0


def _cmd_loss(args: argparse.Namespace) -> int:
    result = calculate_loss_budget(
        LossBudgetInput(
            length_km=args.km,
            wavelength_nm=args.nm,
            connectors=args.connectors,
            splices=args.splices,
            safety_margin_db=args.margin,
        )
    )
    print(f"Wavelength     {args.nm} nm")
    print(f"Fiber          {result.fiber_loss_db:.3f} dB  ({result.atten_used_db_per_km} dB/km)")
    print(f"Connectors     {result.connector_loss_db:.3f} dB")
    print(f"Splices        {result.splice_loss_db:.3f} dB")
    print(f"Margin         {result.safety_margin_db:.3f} dB")
    print(f"Total budget   {result.total_db:.3f} dB")
    return 0


def _cmd_checklist(args: argparse.Namespace) -> int:
    text = checklist_markdown(job_id=args.job, site=args.site, tech=args.tech)
    if args.out:
        path = Path(args.out)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path}")
    else:
        sys.stdout.write(text)
    return 0


def _cmd_stack(args: argparse.Namespace) -> int:
    profile = PRESETS[args.preset]
    recs = recommend(profile)
    print(f"Profile: {profile.name}  ({profile.ram_gb} GB RAM, {profile.platform})")
    for rec in recs:
        print(f"\n== {rec.phase} ==")
        print(f"Engine : {rec.engine}")
        print(f"Quant  : {rec.quant}")
        print(f"Model  : {rec.model_class}")
        print("Notes:")
        for note in rec.notes:
            print(f"  - {note}")
        print("Rejected:")
        for item in rec.rejected:
            print(f"  - {item}")
    return 0


def _cmd_tco(args: argparse.Namespace) -> int:
    if args.profile:
        inp = PROFILES[args.profile]
    else:
        inp = TCOInput(
            hardware_usd=args.hardware,
            yearly_power_kwh=args.kwh,
            usd_per_kwh=args.rate,
            years=args.years,
            cloud_alternative_monthly_usd=args.cloud_month,
        )
    result = estimate(inp)
    payload = {
        "hardware_usd": result.hardware_usd,
        "power_usd": result.power_usd,
        "maintenance_usd": result.maintenance_usd,
        "local_total_usd": result.local_total_usd,
        "cloud_total_usd": result.cloud_total_usd,
        "delta_usd": result.delta_usd,
        "cheaper": result.cheaper,
        "years": inp.years,
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"{inp.years}-year TCO")
        print(f"  Hardware      ${result.hardware_usd:>8.2f}")
        print(f"  Power         ${result.power_usd:>8.2f}")
        print(f"  Maintenance   ${result.maintenance_usd:>8.2f}")
        print(f"  Local total   ${result.local_total_usd:>8.2f}")
        print(f"  Cloud alt     ${result.cloud_total_usd:>8.2f}")
        print(f"  Delta         ${result.delta_usd:>8.2f}  ({result.cheaper} wins)")
    return 0


def _cmd_models(_args: argparse.Namespace) -> int:
    print("Recommended starting weights (download yourself, do not commit):")
    print()
    print("Phone 8 GB")
    print("  - Llama 3.1 8B Instruct  Q4_K_M")
    print("  - Qwen2.5 7B Instruct    Q4_K_M")
    print()
    print("Phone 12 GB")
    print("  - Llama 3.1 8B Instruct  Q5_K_M")
    print("  - Qwen2.5 14B Instruct   Q4_K_M")
    print()
    print("Home server + GPU")
    print("  - Qwen2.5 32B Instruct   Q5_K_M")
    print("  - keep the 8B around for fast field lookups")
    print()
    print("See docs/models.md and scripts/download-model.sh")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="eden",
        description="Project Eden — local-first AI and field tools for tradespeople.",
    )
    parser.add_argument("--version", action="store_true", help="print version and exit")
    sub = parser.add_subparsers(dest="command")

    p_colors = sub.add_parser("colors", help="TIA-598 fiber color code")
    p_colors.add_argument("--fiber", type=int, help="look up a single 1-based fiber number")
    p_colors.add_argument("--count", type=int, default=24, help="how many fibers to print")
    p_colors.add_argument("--legend", action="store_true", help="print the 12-color sequence")
    p_colors.set_defaults(func=_cmd_colors)

    p_loss = sub.add_parser("loss", help="optical loss budget")
    p_loss.add_argument("--km", type=float, required=True, help="span length in kilometers")
    p_loss.add_argument("--nm", type=int, default=1550, help="wavelength (1310, 1550, 1625)")
    p_loss.add_argument("--connectors", type=int, default=2)
    p_loss.add_argument("--splices", type=int, default=0)
    p_loss.add_argument("--margin", type=float, default=2.0, help="safety margin in dB")
    p_loss.set_defaults(func=_cmd_loss)

    p_check = sub.add_parser("checklist", help="print a fiber closeout checklist")
    p_check.add_argument("--job", default="")
    p_check.add_argument("--site", default="")
    p_check.add_argument("--tech", default="")
    p_check.add_argument("--out", help="write markdown to a file")
    p_check.set_defaults(func=_cmd_checklist)

    p_stack = sub.add_parser("stack", help="recommend a local inference stack")
    p_stack.add_argument(
        "--preset",
        choices=sorted(PRESETS.keys()),
        default="phone-8gb",
    )
    p_stack.set_defaults(func=_cmd_stack)

    p_tco = sub.add_parser("tco", help="3-year local vs cloud cost sketch")
    p_tco.add_argument("--profile", choices=sorted(PROFILES.keys()))
    p_tco.add_argument("--hardware", type=float, default=0.0)
    p_tco.add_argument("--kwh", type=float, default=15.0)
    p_tco.add_argument("--rate", type=float, default=0.16)
    p_tco.add_argument("--years", type=int, default=3)
    p_tco.add_argument("--cloud-month", type=float, default=20.0)
    p_tco.add_argument("--json", action="store_true")
    p_tco.set_defaults(func=_cmd_tco)

    p_models = sub.add_parser("models", help="print recommended starting models")
    p_models.set_defaults(func=_cmd_models)

    p_ver = sub.add_parser("version", help="print version")
    p_ver.set_defaults(func=_cmd_version)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.version:
        return _cmd_version(args)
    if not getattr(args, "command", None):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
