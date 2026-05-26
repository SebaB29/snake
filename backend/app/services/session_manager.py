from __future__ import annotations

from threading import Lock

from app.core.settings import Settings
from app.services.game_session import GameSession


class SessionNotFound(Exception):
    pass


class SessionManager:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._sessions: dict[str, GameSession] = {}
        self._lock = Lock()

    def create(self, level: int) -> GameSession:
        session = GameSession(
            level=level,
            obstacle_file=self._settings.obstacle_file,
            fps=self._settings.fps,
        )
        with self._lock:
            self._sessions[session.session_id] = session
        return session

    def get(self, session_id: str) -> GameSession:
        with self._lock:
            session = self._sessions.get(session_id)

        if session is None:
            raise SessionNotFound(session_id)

        return session

    def delete(self, session_id: str) -> None:
        with self._lock:
            self._sessions.pop(session_id, None)
