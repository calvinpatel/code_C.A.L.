async function summarizeNote(note) {
    const response = await fetch("http://127.0.0.1:8000/summarize", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(note)
    });

    if (!response.ok) {
        const errBody = await response.json();
        throw new Error(`HTTP error! status: ${response.status}: ${JSON.stringify(errBody.detail)}`);
    }
    return await response.json();
}

async function main() {
    try {
        const result = await summarizeNote({
            patient_id: "pt-042",
            note_text: "Patient reports intermittent chest pain radiating to left arm since Tuesday",
        });
        console.log(result);
    } catch (err) {
        console.error("summarize failed:", err.message);
    }
}

main();