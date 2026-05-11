# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`code_C.A.L.` is Cal's personal learning repository — a structured Python → Web → AI curriculum tracked alongside working code and reference notes. "C.A.L." = Cal, the learner; Claudia (Claude), the teaching partner; and the code itself. Files here are a mix of lesson exercises, portfolio project drafts, and reference material.

## Environment

- **Python:** 3.14 (`.venv` using `uv`)
- **IDE:** PyCharm Pro (UMSOM license)
- **Virtual environment:** `.venv/` at project root

Activate the venv before running anything:
```bash
source .venv/bin/activate
```

Run a Python file:
```bash
python brain_project.py
python InsideOut_but_Cooler.py
```

There is no build system, test suite, or linter configured yet — these are introduced in the **Modules, Packages & Virtual Environments** and **Testing** arcs of the curriculum.

## Repository structure

- **`CURRICULUM.md`** — The canonical roadmap. Tracks which arcs are complete (`✅`), in progress (`🔄`), or upcoming (`⬜`). The single source of truth for learning progress.
- **`SUPPLEMENTS.md`** — External resources organized by phase (Real Python, Joy of React, DeepLearning.AI short courses, etc.). Not a task list — it's a curated shelf.
- **`notes/`** — Arc-specific cheat sheets and reference docs. Currently contains `file_io_streaming.md` (the streaming CSV pattern from the File I/O arc).
- **`brain_project.py`** — Phase 1 portfolio project: a neuroscience-themed interactive game. Targets the File I/O + OOP + Error Handling arcs.
- **`InsideOut_but_Cooler.py`** — Earlier interactive story exercise (Python basics / control flow era).

## Curriculum phase (as of May 2026)

Phase 1 (Python Core) is nearly complete. Completed arcs:
- CS50 Foundations, Python Basics, Control Flow, Data Structures, Functions & Scope, Randomness & Game Logic, OOP, Error Handling, File I/O & Data Persistence

**Next arc:** Modules, Packages & Virtual Environments (`import` mechanics, `__name__ == "__main__"`, `pip`, `venv`/`uv`, `requirements.txt`).

Phase 1 completion target: portfolio project — neuroscience game (Python-only, OOP + error handling + file I/O).

## Teaching style and conventions

- **Claudia's standing order:** nitpicks are gifts — flag style issues, subtle bugs, and non-obvious Python behavior without being asked.
- **Analogies over abstraction:** concepts stick via metaphor and myth (e.g., error handlers as Lucifer, `with` blocks as sugar over `__enter__`/`__exit__`).
- **Crash loudly during dev** — only catch exceptions you can meaningfully recover from. Don't swallow bugs with broad `except Exception`.
- **Exploratory testing > pondering** — REPL-first when behavior is uncertain.
- When adding new arcs or exercises, update `CURRICULUM.md` to reflect status.