import { useState } from "react";
import { ApiError } from "./api";

export default function LoginForm({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState(null);

    async function handleSubmit(e) {
        e.preventDefault();
        setMessage(null);
        try {
            await onLogin(username, password);
        } catch (err) {
            if (err instanceof ApiError) {
                setMessage(err.message);
            } else {
                setMessage("Can't reach the server.");
            }
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit">Login</button>
            {message && <p role="alert">{message}</p>}
        </form>
    );
}