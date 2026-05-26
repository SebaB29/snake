from __future__ import annotations

from fastapi import APIRouter, Body, HTTPException, status

from app.api.deps import session_manager
from app.schemas.game import GameStartRequest, GameState, InputRequest, RestartRequest
from app.services.session_manager import SessionNotFound

router = APIRouter(prefix="/api")


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/games", response_model=GameState, status_code=status.HTTP_201_CREATED)
def create_game(
    request: GameStartRequest = Body(default=GameStartRequest()),
) -> GameState:
    session = session_manager.create(request.level)
    return session.state()


@router.get("/games/{session_id}", response_model=GameState)
def get_game(session_id: str) -> GameState:
    try:
        session = session_manager.get(session_id)
    except SessionNotFound as exc:
        raise HTTPException(status_code=404, detail="Game session not found") from exc

    return session.state()


@router.post("/games/{session_id}/input", response_model=GameState)
def send_input(session_id: str, request: InputRequest) -> GameState:
    try:
        session = session_manager.get(session_id)
    except SessionNotFound as exc:
        raise HTTPException(status_code=404, detail="Game session not found") from exc

    session.apply_input(request.direction)
    return session.state()


@router.post("/games/{session_id}/tick", response_model=GameState)
def tick(session_id: str) -> GameState:
    try:
        session = session_manager.get(session_id)
    except SessionNotFound as exc:
        raise HTTPException(status_code=404, detail="Game session not found") from exc

    return session.tick()


@router.post("/games/{session_id}/pause", response_model=GameState)
def toggle_pause(session_id: str) -> GameState:
    try:
        session = session_manager.get(session_id)
    except SessionNotFound as exc:
        raise HTTPException(status_code=404, detail="Game session not found") from exc

    session.toggle_pause()
    return session.state()


@router.post("/games/{session_id}/restart", response_model=GameState)
def restart(session_id: str, request: RestartRequest) -> GameState:
    try:
        session = session_manager.get(session_id)
    except SessionNotFound as exc:
        raise HTTPException(status_code=404, detail="Game session not found") from exc

    return session.reset(level=request.level)


@router.delete("/games/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_game(session_id: str) -> None:
    session_manager.delete(session_id)
