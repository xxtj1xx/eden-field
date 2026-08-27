# Project Eden

**Local-first field app for people who actually do the work.**

Phone first. Home screen install. Works offline in a hut with no bars.

Built by a Tier 1 CFOT splicer who got tired of tools that assume you have
signal, a laptop, and a willingness to upload every enclosure photo to
somebody else's cloud.

## The app

Open the `app/` folder, or the live PWA on your phone:

- Fiber color lookup (TIA-598)
- Loss budget
- Closeout checklist (saved on the device only)
- Local AI stack + 3-year cost sketch

Samsung Internet / Chrome → menu → **Add to Home screen**. After that it
opens like a normal app. No account. No telemetry.

The Python CLI is still in the repo for scripting. The product you use in
the field is the app.

## Why this exists

Trades run on bad signal, dirty hands, and closeout packets that have to
be right the first time. Most AI stacks assume the opposite: always-on
broadband, a desktop GPU, and data that is fine to leave the site.

This repo is **not** SpliceFlow. [SpliceFlow](https://spliceflow.app) is the
productized job / photo / closeout workflow. Eden is the open field + local-AI layer.

## Quick start

```bash
git clone https://github.com/xxtj1xx/eden-field.git
cd eden-field/app
# open index.html on your phone, or deploy the app/ folder
```

CLI still works:

```bash
python -m pip install -e ".[dev]"
eden colors --fiber 37
```

## License

MIT. Use it, fork it, take it to work.

## Credits

TJay ([@xx1tjx](https://x.com/xx1tjx) / [xxtj1xx](https://github.com/xxtj1xx)).
