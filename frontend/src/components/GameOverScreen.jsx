function getTitle(status) {
    if (status === "won") {
        return "You win";
    }

    return "Game over";
}

export default function GameOverScreen({ state, onRestart, onExit, error }) {
    return (
        <section className="panel gameover-screen">
            <div className="header">
                <p className="eyebrow">Session ended</p>
                <h1>{getTitle(state?.status)}</h1>
                <p className="sub">Ready for another run?</p>
            </div>

            <div className="stats">
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
                <button className="button primary" type="button" onClick={onRestart}>
                    Restart
                </button>
                <button className="button ghost" type="button" onClick={onExit}>
                    Back to menu
                </button>
            </div>

            {error ? <p className="error">{error}</p> : null}
        </section>
    );
}
