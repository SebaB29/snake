from __future__ import annotations

from app.core.settings import get_settings
from app.services.session_manager import SessionManager

settings = get_settings()
session_manager = SessionManager(settings)
