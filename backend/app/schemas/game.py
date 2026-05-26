from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class Coordinate(BaseModel):
    x: int
    y: int


class BoardState(BaseModel):
    rows: int
    columns: int


class GameState(BaseModel):
    session_id: str
    level: int
    status: Literal["running", "won", "lost"]
    paused: bool
    board: BoardState
    snake: list[Coordinate]
    fruit: list[Coordinate]
    obstacles: list[Coordinate]
    remaining_fruits: int


class GameStartRequest(BaseModel):
    level: int = 1


class InputRequest(BaseModel):
    direction: Literal["UP", "DOWN", "LEFT", "RIGHT"]


class RestartRequest(BaseModel):
    level: int | None = None
