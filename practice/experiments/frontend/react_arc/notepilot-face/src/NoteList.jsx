import { useState, useEffect } from 'react';

// export default function EffectLab() {
//   const [n, setN] = useState(0);
//   console.log(`render — n is ${n}`);
//
//   useEffect(() => {
//     console.log(`effect (no deps) — n is ${n}`);
//   });
//
//   useEffect(() => {
//     console.log(`effect [] — n is ${n}`);
//   }, []);
//
//   useEffect(() => {
//     console.log(`effect [n] — n is ${n}`);
//   }, [n]);
//
//   useEffect(() => {
//   console.log("syncing title");
//   document.title = `n = ${n}`;   // touching something outside React: a side effect
//   }, [n]);
//
//   return <button onClick={() => setN(c => c + 1)}>n = {n}</button>;
// }

export default function NoteList() {
  const [notes, setNotes] = useState([]);       // the data — starts empty, renderable
  const [loading, setLoading] = useState(true); // "in flight" flag
  const [error, setError] = useState(null);     // null = no error yet
  console.log("render — loading:", loading, "notes:", notes.length);

  useEffect(() => {
    async function load() {                     // Trap 1: inner async fn, not the effect itself
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts?_limit=4");
        if (!response.ok) throw new Error(`HTTP ${response.status}`);   // your L03 guard
        const data = await response.json();
        setNotes(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);                      // either way, we're no longer in flight
      }
    }
    load();                                     // fire it — the returned promise is deliberately dropped
  }, []);                                       // mount only: reads no reactive values

  if (loading) return <p>Loading…</p>;
  if (error)   return <p>Error: {error}</p>;
  return (
    <ul>
      {notes.map(note => <li key={note.id}>{note.title}</li>)}
    </ul>
  );
}