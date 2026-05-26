const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
    return (
        <main className="app">
            <h1>Snake Web</h1>
            <p>Frontend skeleton is running.</p>
            <p>API URL: {apiUrl}</p>
        </main>
    );
}
