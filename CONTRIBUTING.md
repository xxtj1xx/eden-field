# Contributing to Project Eden

This project is for people who work in the field and people who run
models on hardware they own. Both are welcome. Drive-by framework
rewrites are not.

## Ground rules

1. Keep the phone path working. If your change only helps a 4090, say so
   and do not break Termux.
2. Do not commit model weights, customer data, job photos, or traces.
3. Prefer small, tested modules over a new abstraction layer.
4. Field numbers should be labeled as defaults, not gospel. Carriers and
   manufacturers win arguments about spec.

## Dev setup

```bash
python -m pip install -e ".[dev]"
pytest -q
eden colors --fiber 1
```

## Good first issues

- Device benchmark: phone model, RAM, engine, quant, tokens/sec, notes
  on heat. Open a PR against `docs/models.md`.
- Extra closeout items used by a specific carrier, filed as an *optional
  profile*, not a replacement of the generic list.
- Termux bootstrap fixes after a Samsung / Android update.

## PR checklist

- [ ] Tests pass (`pytest -q`)
- [ ] New CLI flags have help text
- [ ] No secrets, weights, or proprietary closeout templates
- [ ] README / docs updated if you changed user-facing behavior
