from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.api.websocket import ws_router


def _parse_cors_origins(value: str | None) -> list[str]:
    if not value:
        return ["http://localhost:5173"]

    return [origin.strip() for origin in value.split(",") if origin.strip()]


app = FastAPI(title="Snake API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=_parse_cors_origins(os.getenv("CORS_ORIGINS")),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
app.include_router(ws_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Snake API is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
