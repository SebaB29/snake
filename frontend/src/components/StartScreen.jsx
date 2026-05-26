const levels = Array.from({ length: 7 }, (_, index) => index + 1);

export default function StartScreen({
    level,
    onLevelChange,
    onStart,
    loading,
    error,
    apiUrl
}) {
    return (
        <section className="panel start-screen">
            <div className="header">
                <p className="eyebrow">Classic snake, modern stack</p>
                <h1>Snake Web</h1>
                <p className="sub">Choose a level and start a fresh session.</p>
            </div>

            <div className="menu-grid">
                <label className="field">
                    <span>Level</span>
                    <select
                        value={level}
                        onChange={(event) => onLevelChange(Number(event.target.value))}
                    >
                        {levels.map((value) => (
                            <option key={value} value={value}>
                                Level {value}
                            </option>
                        ))}
                    </select>
                </label>

                <div className="field">
                    <span>Mode</span>
                    <div className="chip">Classic</div>
                </div>
            </div>

            <div className="actions">
                <button
                    className="button primary"
                    type="button"
                    onClick={onStart}
                    disabled={loading}
                >
                    {loading ? "Starting..." : "Start Game"}
                </button>
            </div>

            {error ? <p className="error">{error}</p> : null}
            <p className="meta">API: {apiUrl}</p>
        </section>
    );
}
