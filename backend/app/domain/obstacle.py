from __future__ import annotations

from app.domain.obstacle_loader import ObstacleLoader


class Obstacle:
    def __init__(self, loader: ObstacleLoader) -> None:
        self._coordinates: list[tuple[int, int]] = []
        self._colour = "#CEB200"
        self._loader = loader
        self._obstacles = self._load_obstacles()

    @property
    def coordinates(self) -> list[tuple[int, int]]:
        return self._coordinates

    @property
    def colour(self) -> str:
        return self._colour

    def set_obstacle(self, level: int) -> None:
        if not self._obstacles:
            return

        obstacle_index = (level - 1) % len(self._obstacles)
        self._coordinates = self._obstacles[obstacle_index]

    def _load_obstacles(self) -> dict[int, list[tuple[int, int]]]:
        return self._loader.load_obstacles()
