# Snake Web (Fullstack)

Modernized Snake game with a FastAPI backend and a React frontend, designed for containerized local development and Render deployment. The backend preserves the original OOP game logic and still reads obstacle data from `resources/obstacles.txt`.

## Demo
<div style="display: flex; gap: 10px;">
    <img alt="Snake Gameplay" src="img/snake.png" width="350px">
    <img alt="Game Over Screen" src="img/gameover.png" width="350px">
</div>

## Project Structure
```text
Snake/
├── backend/             # FastAPI app (domain + API + services)
├── frontend/            # React SPA (Vite)
├── resources/           # Game resources (obstacles.txt)
├── docker-compose.yml   # Dev compose (hot reload)
├── docker-compose.prod.yml
├── graphics/            # Legacy rendering library (desktop version)
├── src/                 # Legacy OOP logic (desktop version)
└── main.py              # Legacy entry point
```

## Tech Stack
- **Backend:** FastAPI (Python 3.10+)
- **Frontend:** React (Vite)
- **Realtime:** WebSocket stream + REST endpoints
- **Infra:** Docker + Docker Compose

## Local Development (Docker)
```bash
docker compose up --build
```

Open `http://localhost:5173` and start a session.

### Controls
| Key         | Action         |
|-------------|----------------|
| Arrow Keys  | Move           |
| WASD        | Move           |
| P           | Pause / Resume |

## Backend API (summary)
- `POST /api/games` create a session
- `GET /api/games/{session_id}` fetch current state
- `POST /api/games/{session_id}/input` send direction (REST fallback)
- `POST /api/games/{session_id}/pause` toggle pause
- `POST /api/games/{session_id}/restart` restart session
- `DELETE /api/games/{session_id}` end session
- `WS /ws/games/{session_id}` realtime stream and inputs

## Tests
```bash
cd backend
pytest -q
```

## Production Docker (local)
```bash
docker compose -f docker-compose.prod.yml up --build
```

Frontend is served on `http://localhost:5173` (via nginx), backend on `http://localhost:8000`.

## Deploy to Render

### Backend (Web Service)
- **Build context:** repository root
- **Dockerfile:** `backend/Dockerfile.prod`
- **Env:**
  - `CORS_ORIGINS=https://YOUR-FRONTEND.onrender.com`
  - `GAME_FPS=8`

### Frontend (Static Site)
- **Build command:** `cd frontend && npm install && npm run build`
- **Publish directory:** `frontend/dist`
- **Env:**
  - `VITE_API_URL=https://YOUR-BACKEND.onrender.com`

## Legacy Desktop Version
The original desktop version (gamelib/tkinter) is still available and can be run with:
```bash
python main.py
```

## License
MIT License. See `LICENSE` for details.
