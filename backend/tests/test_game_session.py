from __future__ import annotations

from pathlib import Path

from app.services.game_session import GameSession


def _make_session(tmp_path: Path) -> GameSession:
    obstacles_path = tmp_path / "obstacles.txt"
    obstacles_path.write_text("10,10\n", encoding="utf-8")
    return GameSession(level=1, obstacle_file=obstacles_path, fps=8)


def test_tick_moves_snake(tmp_path: Path) -> None:
    session = _make_session(tmp_path)
    initial_head = session.snake.head

    state = session.tick()

    assert session.snake.head != initial_head
    assert state.status == "running"


def test_eat_fruit_reduces_remaining(tmp_path: Path) -> None:
    session = _make_session(tmp_path)
    session.fruit._coordinates = [(3, 0)]

    before = session.fruit.quantity_fruits
    state = session.tick()

    assert state.remaining_fruits == before - 1
    assert len(session.snake.coordinates) == 4
