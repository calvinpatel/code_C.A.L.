import NoteCard from './NoteCard.jsx';
import Counter from './Counter.jsx';
import EffectLab from './NoteList.jsx';
import NoteList from './NoteList.jsx';
import NoteDetail from './NoteDetail.jsx';
import NoteForm from './NoteForm.jsx';
import {useState, useEffect } from "react";


function App() {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [saveError, setSaveError] = useState(null);

  useEffect(() => {
      async function load() {
          try {
              const response = await fetch("http://localhost:8000/notes");
              if (!response.ok) throw new Error (`HTTP ${response.status}`);
              const data = await response.json();
              setNotes(data);
          } catch (err) {
              setError(err);
          } finally {
              setLoading(false);
          }
      }
      load();
  }, []);

  async function addNote(author, title) {
      setSaveError(null);           // fresh attempt, stale verdict cleared
      try {
          const response = await fetch("http://localhost:8000/notes", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ author, title }),
          });

          if (!response.ok) throw new Error (`HTTP ${response.status}`);
          console.log("status:", response.status);
          const created = await response.json();
          console.log("server returned:", created);
          setNotes([...notes, created]);
      } catch (err) {
          setSaveError(err);
      }
  }

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

    return (
      <div>
          <ul>
            {notes.map((note) => (
                <NoteCard key={note.id} title={note.title} author={note.author} />
            ))}
          </ul>
            <NoteForm onAddNote={addNote} />
            {saveError && <p>Could not save: {saveError.message}</p>}
      </div>
    );
}

export default App;