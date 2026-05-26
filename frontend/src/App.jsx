import { useEffect, useRef, useState } from "react";
import { API_BASE, createGame, deleteGame, getWsUrl, restartGame } from "./api/client.js";
import GameOverScreen from "./components/GameOverScreen.jsx";
import GameScreen from "./components/GameScreen.jsx";
import StartScreen from "./components/StartScreen.jsx";

const SCREENS = {
    START: "start",
    PLAYING: "playing",
    GAME_OVER: "gameover"
};

export default function App() {
    const [screen, setScreen] = useState(SCREENS.START);
    const [level, setLevel] = useState(1);
    const [sessionId, setSessionId] = useState(null);
    const [gameState, setGameState] = useState(null);
    const [starting, setStarting] = useState(false);
    const [error, setError] = useState("");
    const [connectionStatus, setConnectionStatus] = useState("idle");
    const socketRef = useRef(null);

    useEffect(() => {
        if (!sessionId) {
            return undefined;
        }

        setConnectionStatus("connecting");
        const socket = new WebSocket(getWsUrl(sessionId));
        socketRef.current = socket;

        socket.onopen = () => setConnectionStatus("open");
        socket.onmessage = (event) => {
            try {
                const nextState = JSON.parse(event.data);
                setGameState(nextState);
                if (nextState.status === "won" || nextState.status === "lost") {
                    setScreen(SCREENS.GAME_OVER);
                }
            } catch (parseError) {
                // ignore malformed payloads
            }
        };
        socket.onerror = () => setConnectionStatus("error");
        socket.onclose = () => setConnectionStatus("closed");

        return () => {
            socket.close();
            socketRef.current = null;
        };
    }, [sessionId]);

    const sendSocketMessage = (payload) => {
        const socket = socketRef.current;
        if (!socket || socket.readyState !== WebSocket.OPEN) {
            return false;
        }

        socket.send(JSON.stringify(payload));
        return true;
    };

    const handleStart = async () => {
        setError("");
        setStarting(true);
        try {
            const state = await createGame(level);
            setSessionId(state.session_id);
            setGameState(state);
            setScreen(SCREENS.PLAYING);
        } catch (startError) {
            setError(startError instanceof Error ? startError.message : "Failed to start session.");
        } finally {
            setStarting(false);
        }
    };

    const handleRestart = async () => {
        if (!sessionId) {
            return;
        }

        setError("");
        setScreen(SCREENS.PLAYING);
        const sent = sendSocketMessage({ type: "restart", level });
        if (!sent) {
            try {
                const state = await restartGame(sessionId, level);
                setGameState(state);
            } catch (restartError) {
                setError(
                    restartError instanceof Error
                        ? restartError.message
                        : "Failed to restart session."
                );
            }
        }
    };

    const handlePause = () => {
        sendSocketMessage({ type: "pause" });
    };

    const handleExit = async () => {
        if (sessionId) {
            try {
                await deleteGame(sessionId);
            } catch (deleteError) {
                // ignore delete failures
            }
        }

        if (socketRef.current) {
            socketRef.current.close();
        }

        setSessionId(null);
        setGameState(null);
        setScreen(SCREENS.START);
        setConnectionStatus("idle");
    };

    return (
        <main className="app">
            {screen === SCREENS.START ? (
                <StartScreen
                    level={level}
                    onLevelChange={setLevel}
                    onStart={handleStart}
                    loading={starting}
                    error={error}
                    apiUrl={API_BASE}
                />
            ) : null}

            {screen === SCREENS.PLAYING ? (
                <GameScreen
                    sessionId={sessionId}
                    state={gameState}
                    connectionStatus={connectionStatus}
                    onPause={handlePause}
                    onRestart={handleRestart}
                    onExit={handleExit}
                    error={error}
                />
            ) : null}

            {screen === SCREENS.GAME_OVER ? (
                <GameOverScreen
                    state={gameState}
                    onRestart={handleRestart}
                    onExit={handleExit}
                    error={error}
                />
            ) : null}
        </main>
    );
}
