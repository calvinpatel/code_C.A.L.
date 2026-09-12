// src/api.js — the one file that speaks to the server

const BASE_URL = import.meta.env.VITE_API_URL;
if (!BASE_URL) throw new Error("VITE_API_URL is not set — create .env");

let token = null;

export function setToken(t) { token = t; }
export function clearToken() { token = null; }
export function isLoggedIn() { return token !== null; }

export function authHeader() {
    return token ? { Authorization: `Bearer ${token}` } : {};
}

export class ApiError extends Error {
    constructor(status, envelope) {
        super(envelope.detail);                     // Error sets .message (+ .stack)
        this.name = "ApiError";                     // DevTools label
        this.status = status;                       // HTTP status — L03 reads this for 401
        this.errors = envelope.errors ?? [];        // 422 rider
        this.errorId = envelope.error_id ?? null;   // 500 rider
    }
}

export async function request(path, { method = "GET", body, form } = {}) {
    const headers = authHeader();
    const options = { method, headers };
    if (body !== undefined) {                                       // dialect 1: JSON — we set the header
        headers["Content-Type"] = "application/json";
        options.body = JSON.stringify(body);
    } else if (form !== undefined) {                                // dialect 2: form-encoded — browser set the header
        options.body = new URLSearchParams(form);
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

export async function login(username, password) {
    const data = await request("/auth/login", { method: "POST", form: { username, password } });
    setToken(data.access_token);                    // the token goes into the cell and nowhere else
    return data;
}

export const listNotes = () => request("/notes");
export const createNote = (payload) => request("/notes", { method: "POST", body: payload});
export const boom = () => request("/boom");
export const getMe = () => request("/auth/me");