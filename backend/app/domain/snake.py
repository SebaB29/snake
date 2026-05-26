from __future__ import annotations

from app.domain.constants import KEYS


class Snake:
    def __init__(self) -> None:
        self._coordinates = [(0, 0), (1, 0), (2, 0)]
        self._colour = "#1A8500"

    @property
    def coordinates(self) -> list[tuple[int, int]]:
        return self._coordinates

    @property
    def head(self) -> tuple[int, int]:
        return self._coordinates[-1]

    @property
    def tail(self) -> tuple[int, int]:
        return self._coordinates[0]

    @property
    def colour(self) -> str:
        return self._colour

    def move(self, last_move: str) -> None:
        new_head = (
            self.head[0] + KEYS[last_move][0],
            self.head[1] + KEYS[last_move][1],
        )
        self._coordinates.append(new_head)
        self._coordinates.pop(0)

    def eat_fruit(self) -> None:
        self._coordinates.insert(0, self.tail)

    def you_crashed(self, obstacle_coordinates: list[tuple[int, int]]) -> bool:
        return self.head in self._coordinates[:-1] or self.head in obstacle_coordinates
