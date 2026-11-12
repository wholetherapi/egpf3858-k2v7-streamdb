"""Core implementation for streamdb."""

from dataclasses import dataclass


@dataclass
class Config:
    seed: int = 0
    window: int = 8


def run_experiment(config_path: str) -> dict:
    """Run the reference experiment and return a metrics dictionary."""
    metrics = {"config": config_path, "status": "ok"}
    return metrics
