// src/api.js — the one file that speaks to the server

const BASE_URL = import.meta.env.VITE_API_URL;
if (!BASE_URL) throw new Error("VITE_API_URL is not set — create .env");

export class ApiError extends Error {
    constructor(status, envelope) {
        super(envelope.detail);                     // Error sets .message (+ .stack)
        this.name = "ApiError";                     // DevTools label
        this.status = status;                       // HTTP status — L03 reads this for 401
        this.errors = envelope.errors ?? [];        // 422 rider
        this.errorId = envelope.error_id ?? null;   // 500 rider
    }
}

export async function request(path, { method = "GET", body } = {}) {
    const options = { method };
    if (body !== undefined) {
        options.headers = { "Content-Type": "application/json" };
        options.body = JSON.stringify(body);
    }
    const response = await fetch(`${BASE_URL}${path}`, options);    // door 1: TypeError if no server
    if (!response.ok) {                                                             // door 2: server answered, said no
        const envelope = await response
            .json()
            .catch(() => ({ detail: `${response.status} ${response.statusText}` }));    // proxy HTML guard
        throw new ApiError(response.status, envelope);
    }
    return await response.json();
}

export const listNotes = () => request("/notes");
export const createNote = (payload) => request("/notes", { method: "POST", body: payload});
export const boom = () => request("/boom");