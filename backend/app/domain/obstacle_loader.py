from __future__ import annotations

from csv import reader
from pathlib import Path


class ObstacleLoader:
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def load_obstacles(self) -> dict[int, list[tuple[int, int]]]:
        obstacles: dict[int, list[tuple[int, int]]] = {}
        try:
            with self.file_path.open() as file:
                csv_reader = reader(file, delimiter=" ")
                for i, coordinate_group in enumerate(csv_reader):
                    if not coordinate_group:
                        continue
                    obstacles[i] = [
                        tuple(map(int, coords.split(",")))
                        for coords in coordinate_group[0].split(";")
                    ]
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"Obstacle file not found: {self.file_path}"
            ) from exc
        except Exception as exc:
            raise Exception(f"Failed to read obstacle file: {exc}") from exc

        return obstacles
