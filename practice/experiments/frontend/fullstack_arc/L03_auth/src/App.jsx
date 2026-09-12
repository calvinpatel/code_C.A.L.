import { useState, useEffect } from "react";
import { ApiError, listNotes, createNote, boom, login, getMe, clearToken } from "./api.js";
import LoginForm from "./LoginForm";

export default function App() {
  const [notes, setNotes] = useState([]);
  const [error, setError] = useState(null);
  const [user, setUser] = useState(null);

  function logout() {
    clearToken();
    setUser(null);
    setNotes([]);
  }

  function handleApiFailure(err) {
    if (err instanceof ApiError && err.status === 401) {
      logout();
      setError(new Error("Session expired - Please sign in again."));
      return;
    }
    setError(err);
  }

  async function handleLogin(username, password) {
    await login(username, password);
    setUser(await getMe());
  }

  useEffect(() => {
    if (!user) return;
    async function loadNotes() {
      setError(null);
      try {
        const data = await listNotes();
        setNotes(data.items);
      } catch (err) {
        handleApiFailure(err);
      }
    }
    loadNotes();
  }, [user]);

  async function handleBadNote() {
    setError(null);
    try {
      await createNote({ title: "t" });
    } catch (err) {
      handleApiFailure(err);
    }
  }

  async function handleBoom() {
    setError(null);
    try {
      await boom();
    } catch (err) {
      handleApiFailure(err);
    }
  }

  if (!user) {
    return (
        <>
          <h1>L03b — auth</h1>
          <LoginForm onLogin={handleLogin} />
          {error && <p role="alert">{error.message}</p>}
        </>
    );
  }

  return (
      <main>
        <h1>L03b — auth</h1>
        <p>
          Signed in as {user.username}{" "}
          <button onClick={logout}>Sign out</button>
        </p>

        <button onClick={handleBadNote}>Add bad note</button>
        <button onClick={handleBoom}>Boom</button>

        <ul>
          {notes.map((n) => (
              <li key={n.id}>{n.title}</li>
          ))}
        </ul>

        {error && (
            <section role="alert">
              {error instanceof ApiError ? (
                  <>
                    <p>{error.status} — {error.message}</p>
                    <ul>
                      {error.errors.map((e) => (
                          <li key={e.field}>{e.field}: {e.msg}</li>
                      ))}
                    </ul>
                    {error.errorId && <p>incident {error.errorId}</p>}
                  </>
              ) : (
                  <p>Can't reach the server.</p>
              )}
            </section>
        )}
      </main>
  );
}