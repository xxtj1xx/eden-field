# Architecture

## Layers

1. **Constraints** — phone RAM, heat, vaults with no signal, job data
   that should not leave the site.
2. **Criteria** — quality, latency, privacy, 3-year TCO.
3. **Phase 1** — Android / Termux + llama.cpp + one quantized instruct
   model + this CLI.
4. **Phase 2** — home server, same weight family, GPU if it earns the
   power bill, phone becomes a client when you have signal.

## Why llama.cpp first

- ARM64 is a first-class story, not an afterthought.
- GGUF quants are how 8 GB phones participate.
- The same files move to a home box without a format conversion circus.

Ollama is acceptable on Phase 2 if you want a daemon. It is not the
Termux default.

## What this repo is allowed to be

A decision framework, a small Python CLI, field math, and scripts that
get a splicer to a working local model.

## What this repo is not allowed to become

- A wrapper around five inference engines
- A hosted chat product
- A clone of SpliceFlow's job/photo/packet workflow
- A place to store weights

## Data rules

Eden processes local inputs. If a future module summarizes splice notes,
the notes stay on device unless the user exports them. No anonymous
usage pings.
