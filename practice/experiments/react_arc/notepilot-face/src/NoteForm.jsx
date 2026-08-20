import { useState } from "react";

export default function NoteForm({onAddNote}) {
    const [author, setAuthor] = useState("");
    const [title, setTitle] = useState("");

    function handleSubmit(e) {
        e.preventDefault();                               // disarm the navigation default
        onAddNote(author, title);                         // send the data up to the parent
        setAuthor("");                              // clear the field: one setter call, because state owns the text
        setTitle("");
    }

    return (
        <form onSubmit={handleSubmit}
              style={{
                  display: "flex",
                  flexDirection: "column",
                  gap: "0.5rem",
                  width: "75%",
                  margin: "0 auto",
              }}
        >
            <input
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Title"
            />
            <input
                value={author}
                onChange={(e) => setAuthor(e.target.value)}
                placeholder="Author"
            />
            <button>Save Note</button>
        </form>
    );
}