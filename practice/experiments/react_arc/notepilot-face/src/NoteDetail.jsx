import { useEffect, useState } from 'react';

export default function NoteDetail({ noteId }) {
    const [note, setNote] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const controller = new AbortController();
        console.log("setup for noteId", noteId);

        async function load() {
            try {
                const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${noteId}`, {signal: controller.signal});
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                const data = await response.json();
                setNote(data);
            } catch (err) {
                if (err.name === 'AbortError') {
                    console.log('fetch aborted for note:', noteId);
                    return;
                } else {
                    setError(err);
                }
            }
        }

        load();

        return () => {
            console.log("cleanup for noteId:", noteId);
            controller.abort();
        };
    }, [noteId]);

    if (error) return <p>Error: {error.message}</p>;
    if (!note) return <p>Loading…</p>;
    return <h2>{note.title}</h2>;
}