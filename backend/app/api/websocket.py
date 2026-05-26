from __future__ import annotations

import asyncio
import logging

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.api.deps import session_manager
from app.services.session_manager import SessionNotFound

ws_router = APIRouter()
logger = logging.getLogger("snake.websocket")
ALLOWED_DIRECTIONS = {"UP", "DOWN", "LEFT", "RIGHT"}


async def _receiver_loop(websocket: WebSocket, session) -> None:
    while True:
        try:
            data = await websocket.receive_json()
        except WebSocketDisconnect:
            break
        except Exception as exc:
            logger.warning("Invalid websocket payload: %s", exc)
            continue

        message_type = data.get("type")

        if message_type == "input":
            direction = data.get("direction")
            if direction in ALLOWED_DIRECTIONS:
                session.apply_input(direction)
        elif message_type == "pause":
            session.toggle_pause()
        elif message_type == "restart":
            level = data.get("level")
            if isinstance(level, int) and level > 0:
                session.reset(level=level)
            else:
                session.reset()


async def _sender_loop(websocket: WebSocket, session) -> None:
    interval = 1 / session.fps
    while True:
        await asyncio.sleep(interval)
        state = session.tick()
        await websocket.send_json(state.model_dump())


@ws_router.websocket("/ws/games/{session_id}")
async def game_socket(websocket: WebSocket, session_id: str) -> None:
    await websocket.accept()

    try:
        session = session_manager.get(session_id)
    except SessionNotFound:
        await websocket.close(code=1008)
        return

    await websocket.send_json(session.state().model_dump())

    receiver = asyncio.create_task(_receiver_loop(websocket, session))
    sender = asyncio.create_task(_sender_loop(websocket, session))

    done, pending = await asyncio.wait(
        {receiver, sender}, return_when=asyncio.FIRST_EXCEPTION
    )

    for task in pending:
        task.cancel()

    for task in done:
        exception = task.exception()
        if exception and not isinstance(exception, WebSocketDisconnect):
            raise exception
