from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


def _resolve_resources_dir() -> Path:
    env_value = os.getenv("RESOURCES_DIR")
    if env_value:
        return Path(env_value)

    base_dir = Path(__file__).resolve().parents[2]
    candidate = base_dir / "resources"
    if candidate.exists():
        return candidate

    return base_dir.parent / "resources"


@dataclass(frozen=True)
class Settings:
    resources_dir: Path
    obstacle_file: Path
    fps: int


def get_settings() -> Settings:
    resources_dir = _resolve_resources_dir()
    fps = int(os.getenv("GAME_FPS", "8"))

    return Settings(
        resources_dir=resources_dir,
        obstacle_file=resources_dir / "obstacles.txt",
        fps=fps,
    )
