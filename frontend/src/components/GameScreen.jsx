function formatStatus(status) {
    if (!status) {
        return "loading";
    }

    return status;
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
    return (
        <section className="panel game-screen">
            <div className="header-row">
                <div>
                    <p className="eyebrow">Live session</p>
                    <h1>Snake Web</h1>
                    <p className="sub">
                        Rendering lands in Hito 4. State already streams live.
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
                    <div className="board-grid"></div>
                    <div className="board-message">Board render in Hito 4.</div>
                </div>

                <div className="side-panel">
                    <div className="stats">
                        <div className="stat">
                            <span className="label">Status</span>
                            <span className="value">{formatStatus(state?.status)}</span>
                        </div>
                        <div className="stat">
                            <span className="label">Level</span>
                            <span className="value">{state?.level ?? "-"}</span>
                        </div>
                        <div className="stat">
                            <span className="label">Fruits left</span>
                            <span className="value">{state?.remaining_fruits ?? "-"}</span>
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
                    <p className="hint">Input mapping arrives in Hito 4.</p>
                </div>
            </div>
        </section>
    );
}
