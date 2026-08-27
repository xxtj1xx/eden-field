"""Inference stack recommendations for Project Eden.

Phase 1 is Android / Termux on a phone you already carry.
Phase 2 is a home server when the phone is no longer enough.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HardwareProfile:
    name: str
    ram_gb: int
    has_nvidia: bool = False
    has_amd: bool = False
    platform: str = "android"  # android | linux | windows


@dataclass(frozen=True)
class StackRecommendation:
    phase: str
    engine: str
    quant: str
    model_class: str
    notes: tuple[str, ...]
    rejected: tuple[str, ...]


def recommend(profile: HardwareProfile) -> list[StackRecommendation]:
    """Return Phase 1 (and Phase 2 if relevant) stack picks."""
    recs: list[StackRecommendation] = []

    if profile.platform == "android" or profile.ram_gb <= 12:
        quant = "Q4_K_M" if profile.ram_gb < 10 else "Q5_K_M"
        model = "7B–8B instruct" if profile.ram_gb < 10 else "8B–14B instruct"
        recs.append(
            StackRecommendation(
                phase="1 — phone / Termux",
                engine="llama.cpp (termux-packages / build from source)",
                quant=quant,
                model_class=model,
                notes=(
                    "Keep context modest (2k–4k) until you measure thermal throttle.",
                    "Prefer one resident model. Swapping weights on-device is pain.",
                    "Do not send job photos, GPS, or splice matrices to a cloud API.",
                    "Benchmark on the actual phone, not a laptop M-series number.",
                ),
                rejected=(
                    "Ollama on Termux — extra daemon, weaker ARM story.",
                    "Unquantized 70B — will not fit, will heat-soak the phone.",
                    "Cloud-only assistants — they fail in vaults and huts.",
                ),
            )
        )

    if profile.platform != "android" or profile.has_nvidia or profile.has_amd:
        engine = "llama.cpp + GPU offload"
        if profile.has_nvidia:
            engine = "llama.cpp (CUDA) or Ollama if you want a daemon"
        recs.append(
            StackRecommendation(
                phase="2 — home server",
                engine=engine,
                quant="Q5_K_M or Q6_K",
                model_class="14B–32B instruct, optional second 8B for speed",
                notes=(
                    "Same GGUF family as Phase 1 so prompts and templates port.",
                    "Phone becomes a thin client over tailnet when you have signal.",
                    "Size the PSU and idle watts; 24/7 is a power bill not a hobby.",
                ),
                rejected=(
                    "Jumping to a different engine just because it is trendy.",
                    "Hosting open weights on a public IP with no auth.",
                ),
            )
        )

    return recs


PRESETS = {
    "phone-8gb": HardwareProfile("typical Android 8GB", ram_gb=8, platform="android"),
    "phone-12gb": HardwareProfile("Android 12GB", ram_gb=12, platform="android"),
    "server-nvidia": HardwareProfile(
        "home box + NVIDIA", ram_gb=32, has_nvidia=True, platform="linux"
    ),
    "server-cpu": HardwareProfile("home box CPU-only", ram_gb=32, platform="linux"),
}
