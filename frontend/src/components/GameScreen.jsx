import Board from "./Board.jsx";

function formatStatus(state) {
    if (!state) {
        return "loading";
    }

    if (state.paused) {
        return "paused";
    }

    return state.status;
}

export default function GameScreen({
    sessionId,
    state,
    connectionStatus,
    onPause,
    onRestart,
    onExit,
    error
}) {
    const overlayMessage = state?.paused
        ? "Paused"
        : connectionStatus !== "open"
            ? "Connecting..."
            : state
                ? null
                : "Waiting for game state...";

    return (
        <section className="panel game-screen">
            <div className="header-row">
                <div>
                    <p className="eyebrow">Live session</p>
                    <h1>Snake Web</h1>
                    <p className="sub">
                        Use WASD or arrow keys to move. Press P to pause.
                    </p>
                </div>
                <div className="status-stack">
                    <span className={`connection ${connectionStatus}`}>
                        {connectionStatus}
                    </span>
                    <span className="chip">
                        Session {sessionId ? sessionId.slice(0, 8) : "-"}
                    </span>
                </div>
            </div>

            <div className="content-grid">
                <div className="board">
                    <Board
                        board={state?.board}
                        snake={state?.snake}
                        fruit={state?.fruit}
                        obstacles={state?.obstacles}
                    />
                    {overlayMessage ? (
                        <div className="board-overlay">{overlayMessage}</div>
                    ) : null}
                </div>

                <div className="side-panel">
                    <div className="stats">
                        <div className="stat">
                            <span className="label">Status</span>
                            <span className="value">{formatStatus(state)}</span>
                        </div>
                        <div className="stat">
                            <span className="label">Level</span>
                            <span className="value">{state?.level ?? "-"}</span>
                        </div>
                        <div className="stat">
                            <span className="label">Fruits left</span>
                            <span className="value">{state?.remaining_fruits ?? "-"}</span>
                        </div>
                        <div className="stat">
                            <span className="label">Paused</span>
                            <span className="value">{state?.paused ? "Yes" : "No"}</span>
                        </div>
                    </div>

                    <div className="controls">
                        <button className="button" type="button" onClick={onPause}>
                            Pause
                        </button>
                        <button className="button" type="button" onClick={onRestart}>
                            Restart
                        </button>
                        <button className="button ghost" type="button" onClick={onExit}>
                            Back to menu
                        </button>
                    </div>

                    {error ? <p className="error">{error}</p> : null}
                    <p className="hint">Arrow keys and WASD are supported.</p>
                </div>
            </div>
        </section>
    );
}
