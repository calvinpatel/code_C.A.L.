import { useState, useEffect } from "react";
import { ApiError, listNotes, createNote, boom } from "./api.js";

export default function App() {
  const [notes, setNotes] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadNotes() {
      try {
        const data = await listNotes();
        setNotes(data.items);
      } catch (err) {
        setError(err);
      }
    }
    loadNotes();
  }, []);

  async function handleBadNote() {
    setError(null);
    try {
      await createNote({ title: "t" });
    } catch (err) {
      setError(err);
    }
  }

  async function handleBoom() {
    setError(null);
    try {
      await boom();
    } catch (err) {
      setError(err);
    }
  }

  return (
      <main>
        <h1>L02b — the contract</h1>
        <button onClick={handleBadNote}>Add bad note</button>
        <button onClick={handleBoom}>Boom</button>

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

        <ul>
          {notes.map((n)  => <li key={n.id}>{n.title}</li>)}
        </ul>
      </main>
  );
}