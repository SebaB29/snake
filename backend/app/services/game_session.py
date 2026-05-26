from __future__ import annotations

from pathlib import Path
from threading import Lock
from uuid import uuid4

from app.domain.fruit import Fruit
from app.domain.game import Game
from app.domain.obstacle import Obstacle
from app.domain.obstacle_loader import ObstacleLoader
from app.domain.snake import Snake
from app.schemas.game import BoardState, Coordinate, GameState


def _to_coordinates(values: list[tuple[int, int]]) -> list[Coordinate]:
    return [Coordinate(x=coord[0], y=coord[1]) for coord in values]


class GameSession:
    def __init__(self, level: int, obstacle_file: Path, fps: int) -> None:
        self.session_id = str(uuid4())
        self.level = level
        self.status = "running"
        self.paused = False
        self.fps = fps
        self._lock = Lock()

        self._loader = ObstacleLoader(obstacle_file)
        self._reset_state()

    def _reset_state(self) -> None:
        self.game = Game()
        self.snake = Snake()
        self.fruit = Fruit()
        self.obstacle = Obstacle(self._loader)

        self.obstacle.set_obstacle(self.level)
        self.fruit.set_fruit(
            self.game.get_board_dimensions(),
            self.snake.coordinates,
            self.obstacle.coordinates,
        )
        self.status = "running"
        self.paused = False

    def reset(self, level: int | None = None) -> GameState:
        with self._lock:
            if level is not None:
                self.level = level
            self._reset_state()
            return self.state()

    def apply_input(self, direction: str | None) -> None:
        if direction:
            self.game.set_move(direction)

    def toggle_pause(self) -> bool:
        self.paused = not self.paused
        return self.paused

    def tick(self) -> GameState:
        with self._lock:
            if self.status != "running" or self.paused:
                return self.state()

            self.snake.move(self.game.get_last_move())
            self._check_fruit_collision()
            self.status = self.game.get_status(
                self.snake, self.fruit.quantity_fruits, self.obstacle.coordinates
            )
            return self.state()

    def _check_fruit_collision(self) -> None:
        if self.snake.head in self.fruit.coordinates:
            self.snake.eat_fruit()
            self.fruit.set_quantity_fruits()
            self.fruit.set_fruit(
                self.game.get_board_dimensions(),
                self.snake.coordinates,
                self.obstacle.coordinates,
            )

    def state(self) -> GameState:
        board_rows, board_columns = self.game.get_board_dimensions()
        return GameState(
            session_id=self.session_id,
            level=self.level,
            status=self.status,
            paused=self.paused,
            board=BoardState(rows=board_rows, columns=board_columns),
            snake=_to_coordinates(self.snake.coordinates),
            fruit=_to_coordinates(self.fruit.coordinates),
            obstacles=_to_coordinates(self.obstacle.coordinates),
            remaining_fruits=self.fruit.quantity_fruits,
        )
