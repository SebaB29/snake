from __future__ import annotations

from random import randint

from app.domain.constants import AMOUNT_FRUITS_TO_WIN


class Fruit:
    def __init__(self) -> None:
        self._coordinates: list[tuple[int, int]] = []
        self._colour = "#F00"
        self._quantity_fruits = AMOUNT_FRUITS_TO_WIN

    @property
    def coordinates(self) -> list[tuple[int, int]]:
        return self._coordinates

    @property
    def colour(self) -> str:
        return self._colour

    @property
    def quantity_fruits(self) -> int:
        return self._quantity_fruits

    def set_fruit(
        self,
        board_dimensions: tuple[int, int],
        snake_coordinates: list[tuple[int, int]],
        obstacle_coordinates: list[tuple[int, int]],
    ) -> None:
        self._coordinates = [
            self._generate_fruit(
                board_dimensions, snake_coordinates, obstacle_coordinates
            )
        ]

    def set_quantity_fruits(self) -> None:
        self._quantity_fruits -= 1

    def _generate_fruit(
        self,
        board_dimensions: tuple[int, int],
        snake_coordinates: list[tuple[int, int]],
        obstacle_coordinates: list[tuple[int, int]],
    ) -> tuple[int, int]:
        new_coordinates = None
        while (
            new_coordinates is None
            or new_coordinates in snake_coordinates
            or new_coordinates in obstacle_coordinates
        ):
            new_coordinates = (
                randint(0, board_dimensions[1] - 1),
                randint(0, board_dimensions[0] - 1),
            )

        return new_coordinates
