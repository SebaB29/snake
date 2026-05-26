const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";
const WS_BASE = API_BASE.replace(/^http/, "ws");

async function request(path, options = {}) {
    const response = await fetch(`${API_BASE}${path}`, {
        headers: {
            "Content-Type": "application/json",
            ...(options.headers || {})
        },
        ...options
    });

    if (!response.ok) {
        let message = `Request failed (${response.status})`;
        try {
            const data = await response.json();
            if (data && data.detail) {
                message = data.detail;
            }
        } catch (error) {
            // ignore invalid json
        }
        throw new Error(message);
    }

    if (response.status === 204) {
        return null;
    }

    return response.json();
}

export function createGame(level) {
    return request("/api/games", {
        method: "POST",
        body: JSON.stringify({ level })
    });
}

export function restartGame(sessionId, level) {
    return request(`/api/games/${sessionId}/restart`, {
        method: "POST",
        body: JSON.stringify({ level })
    });
}

export function deleteGame(sessionId) {
    return request(`/api/games/${sessionId}`, {
        method: "DELETE"
    });
}

export function getWsUrl(sessionId) {
    return `${WS_BASE}/ws/games/${sessionId}`;
}

export { API_BASE };
