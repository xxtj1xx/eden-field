# Project Eden

**Local-first AI for people who actually do the work.**

Phone first. Home server later. Your job data stays on devices you own.

Built by a Tier 1 CFOT splicer who got tired of tools that assume you have
signal, a laptop, and a willingness to upload every enclosure photo to
somebody else's cloud.

```
eden colors --fiber 37
eden loss --km 12.4 --nm 1550 --connectors 2 --splices 8
eden checklist --job WO-4419 --site "Hut 12 / Case A"
eden stack --preset phone-8gb
eden tco --profile phone-only
```

## Why this exists

Trades run on bad signal, dirty hands, and closeout packets that have to
be right the first time. Most AI stacks assume the opposite: always-on
broadband, a desktop GPU, and data that is fine to leave the site.

Project Eden is the opposite bet:

1. **The phone you already carry is the first computer.** Termux + llama.cpp.
2. **A home box is phase two**, not a prerequisite.
3. **Field utilities ship with the stack.** Color codes, loss budgets, and
   a closeout checklist you can print in a vault.
4. **Privacy is a constraint, not a slogan.** Job photos, GPS, and splice
   matrices do not go to a SaaS by default.

This repo is **not** SpliceFlow. [SpliceFlow](https://spliceflow.app) is the
productized job / photo / closeout workflow for splicing crews. Eden is the
open local-AI and field-math layer sitting next to it.

## Quick start

Python 3.9+

```bash
git clone https://github.com/xxtj1xx/eden-field.git
cd eden-field
python -m pip install -e ".[dev]"
eden --help
pytest -q
```

On Android with Termux, see [`docs/termux-setup.md`](docs/termux-setup.md)
and [`scripts/termux-bootstrap.sh`](scripts/termux-bootstrap.sh).

## What ships in 0.1

| Command | What it does |
| --- | --- |
| `eden colors` | TIA-598 fiber / tube color lookup |
| `eden loss` | Conservative optical loss budget |
| `eden checklist` | Printable closeout checklist (markdown) |
| `eden stack` | Phase 1 / Phase 2 inference recommendation |
| `eden models` | Starting GGUF classes, not hosted weights |
| `eden tco` | 3-year local vs cloud cost sketch |

No model weights are in this repository. You download them.

## Design rules

- Offline-first. A hut with no LTE is a valid production environment.
- Quantized models by default (`Q4_K_M`, `Q5_K_M`). Quality arguments for
  going heavier have to beat heat, battery, and RAM.
- Same engine family from phone to server so prompts port.
- Measure on the device you will use. Laptop tokens/sec are fan fiction.
- Refuse to become a graveyard of half-ported frameworks.

Full architecture notes: [`docs/architecture.md`](docs/architecture.md).

## Roadmap

- [x] Public repo, MIT license, CLI + tests
- [x] Fiber color / loss / closeout helpers
- [x] Stack + TCO decision helpers
- [ ] Termux one-shot installer that actually survives Samsung updates
- [ ] Prompt pack for splice notes and as-built summaries (local only)
- [ ] Optional tailnet bridge from phone to home box
- [ ] Real device benchmark table (submit a PR with your phone + t/s)

## Contributing

PRs from people who have pulled slack, dressed a tray, or actually run
llama.cpp on a phone are first in line. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. Use it, fork it, take it to work.

## Credits

TJay ([@xx1tjx](https://x.com/xx1tjx) / [xxtj1xx](https://github.com/xxtj1xx)).
Field work by day, local models at night.
