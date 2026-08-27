# Termux setup (Phase 1)

Target: a work phone you already own. 8 GB RAM is enough for 7B–8B
Q4_K_M if you are honest about context length.

## 1. Install Termux from F-Droid

Play Store builds lag and break. Use F-Droid.

## 2. Bootstrap

```bash
pkg update && pkg upgrade -y
pkg install -y git python clang make cmake
curl -fsSL https://raw.githubusercontent.com/xxtj1xx/eden-field/main/scripts/termux-bootstrap.sh | bash
```

Or clone and run locally:

```bash
git clone https://github.com/xxtj1xx/eden-field.git
cd eden-field
bash scripts/termux-bootstrap.sh
```

## 3. Weights

See `docs/models.md`. Put GGUF files in `~/models`. Never commit them.

## 4. Sanity check

```bash
python -m pip install -e ".[dev]"
eden stack --preset phone-8gb
eden colors --fiber 24
```

## Thermal reality

A phone in July on a pole is not a lab bench. If tokens/sec fall off a
cliff after two minutes, drop quant or context before you buy a new
phone.
