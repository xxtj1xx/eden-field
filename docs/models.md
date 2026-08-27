# Models

Eden does not host weights. Download from the upstream project that
licenses them.

## Starting points

| Device | Class | Quant | Why |
| --- | --- | --- | --- |
| Android 8 GB | 7B–8B instruct | Q4_K_M | Fits, usable, less heat |
| Android 12 GB | 8B–14B instruct | Q4_K_M / Q5_K_M | Headroom for context |
| Home CPU box | 8B + 14B | Q5_K_M | Same family as the phone |
| Home + NVIDIA | 14B–32B | Q5_K_M / Q6_K | Quality jump that earns watts |

Concrete names change every quarter. As of this writing the short list
is Llama 3.1 8B Instruct and Qwen2.5 7B/14B/32B Instruct.

## Benchmark table (fill this in)

Submit a PR.

| Device | RAM | Engine | Model / quant | ctx | t/s | heat notes |
| --- | --- | --- | --- | --- | --- | --- |
| _your phone_ |  | llama.cpp |  |  |  |  |

## Rules

- Prefer one resident model on a phone.
- Do not chase leaderboard winners that need 32k context on 8 GB.
- Keep a small model even after you stand up a server. Fast lookups
  should not wait on a 32B.
