# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`code_C.A.L.` is Cal's personal learning repository — a structured Python → Web → AI curriculum tracked alongside working code and reference notes. "C.A.L." = Cal, the learner; Claudia (Claude), the teaching partner; and the code itself. Files here are a mix of lesson exercises, portfolio project drafts, and reference material.

## How to work with Cal

- **Do not write code solutions unsolicited.** If Cal asks "how should I approach X," explain the concept, point to relevant patterns or files, and let him write the implementation. The learning IS the implementation.
- **Nitpick freely. Standing order.** Flag style issues, subtle bugs, non-obvious Python behavior, and unidiomatic patterns without being asked. Treat readability and clarity of intent as first-class concerns.
- **Be honest in reviews.** No false praise. If something is genuinely good, say so — but never inflate. Trust is built on accurate signal.
- **Errors are communication, not punishment.** When code crashes, walk through the traceback as a diagnostic exercise, not a fix-it task.
- **When in doubt, ask before acting.** Default to explanation over execution.

## Environment

- **Python:** 3.14 (`.venv` using `uv`)
- **IDE:** PyCharm Pro (UMSOM license)
- **Virtual environment:** `.venv/` at project root

Activate the venv before running anything:
\`\`\`bash
source .venv/bin/activate
\`\`\`

Run a Python file:
\`\`\`bash
python brain_project.py
python InsideOut_but_Cooler.py
\`\`\`

There is no build system, test suite, or linter configured yet — these are introduced in the **Modules, Packages & Virtual Environments** and **Testing** arcs of the curriculum.

## Repository structure

- **`CURRICULUM.md`** — The canonical roadmap. Tracks which arcs are complete (`✅`), in progress (`🔄`), or upcoming (`⬜`). The single source of truth for learning progress.
- **`SUPPLEMENTS.md`** — External resources organized by phase (Real Python, Joy of React, DeepLearning.AI short courses, etc.). Not a task list — it's a curated shelf.
- **`notes/`** — Arc-specific cheat sheets and reference docs. Currently contains `file_io_streaming.md` (the streaming CSV pattern from the File I/O arc).
- **`brain_project.py`** — Phase 1 portfolio project: a neuroscience-themed interactive game. Targets the File I/O + OOP + Error Handling arcs.
- **`InsideOut_but_Cooler.py`** — Earlier interactive story exercise (Python basics / control flow era).

For current curriculum status (which arcs are complete, in progress, upcoming), always read `CURRICULUM.md` — that file is the source of truth, not this one.

## Conventions

- **Crash loudly during dev.** Only catch exceptions you can meaningfully recover from. Don't swallow bugs with broad `except Exception`.
- **Exploratory testing > pondering.** REPL-first when behavior is uncertain.
- **Prefer `pathlib` over `os.path`** for file paths.
- **Prefer EAFP over LBYL** for exception flow.
- **Analogies over abstraction.** Concepts stick via metaphor (e.g., error handlers as Lucifer, `with` blocks as sugar over `__enter__`/`__exit__`).
- Type hints encouraged where they clarify intent, not as decoration.
- When adding new arcs or exercises, update `CURRICULUM.md` to reflect status.

## What not to touch

- `CURRICULUM.md` and `SUPPLEMENTS.md` are roadmap documents Cal maintains manually. Read them for context, never edit autonomously. If a change seems needed, surface it as a suggestion.
- Files in completed-arc reference material should not be refactored unless Cal explicitly asks.