from __future__ import annotations

from app.domain.constants import BOARD_COLUMNS, BOARD_ROWS, KEYS
from app.domain.snake import Snake


class Game:
    def __init__(self) -> None:
        self._last_move = "RIGHT"

    def get_board_dimensions(self) -> tuple[int, int]:
        return (BOARD_ROWS, BOARD_COLUMNS)

    def get_last_move(self) -> str:
        return self._last_move

    def set_move(self, key: str) -> None:
        if key in KEYS:
            self._last_move = key

    def _you_lost(self, snake_head: tuple[int, int], you_crashed: bool) -> bool:
        return (
            not (0 <= snake_head[0] < BOARD_ROWS and 0 <= snake_head[1] < BOARD_COLUMNS)
            or you_crashed
        )

    def _you_won(self, quantity_fruits: int) -> bool:
        return not quantity_fruits

    def get_status(
        self,
        snake: Snake,
        quantity_fruits: int,
        obstacle_coordinates: list[tuple[int, int]],
    ) -> str:
        if self._you_won(quantity_fruits):
            return "won"

        if self._you_lost(snake.head, snake.you_crashed(obstacle_coordinates)):
            return "lost"

        return "running"

    def finish_game(
        self,
        snake: Snake,
        quantity_fruits: int,
        obstacle_coordinates: list[tuple[int, int]],
    ) -> bool:
        return self._you_won(quantity_fruits) or self._you_lost(
            snake.head, snake.you_crashed(obstacle_coordinates)
        )
