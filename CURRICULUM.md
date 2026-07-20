# Cal's Python → Web → AI Curriculum

**Format:** Topic-level with rough lesson estimates. Lessons emerge organically within each arc. Independent of Angela Yu's 100 Days of Code, with parallel coverage noted where relevant.

**Legend:**
- ✅ Completed
- 🔄 In progress
- ⬜ Not yet started
- 🎯 Final boss quiz passed
- ◆ Flagship build gate — nothing past this line until the build ships

> 📚 Supplemental courses and external resources tracked in [`SUPPLEMENTS.md`](./SUPPLEMENTS.md).
>
> 🏗️ Flagship specs: [`PROJECT_01_NOTEPILOT.md`](./PROJECT_01_NOTEPILOT.md) · [`PROJECT_02_TRIALMATCH.md`](./PROJECT_02_TRIALMATCH.md) · [`PROJECT_03_PRELUDE.md`](./PROJECT_03_PRELUDE.md)

---

## 🗡️ OPERATING PLAN: THE 12-WEEK SPRINT

*Applications open ~October 2026. Application day ≠ curriculum complete — it's **minimum credible arsenal** day: DS&A gate passable, one flagship shipped and demoable, a story nobody else in the pile can tell. Learning continues through the application season; the search itself takes 4–8 weeks and TrialMatch ships inside that window.*

| Weeks | Focus | Deliverable |
|-------|-------|-------------|
| **W1–2** | FastAPI + async + auth/security | The big backend arc |
| **W3–4** | Frontend, compressed | Demo-grade React, nothing more |
| **W5** | Shipping & Infrastructure | 🚩 **First live deploy** — something of mine on the public internet before the AI phase begins |
| **W6–7** | Prompt Engineering + LLM APIs → Evals arc | The moat, forged early |
| **W8–10** | ◆ **Build & deploy NotePilot** | Fix the two CRITICALs *first*. Live app + eval dashboard |
| **W11–12** | RAG core + portfolio polish | calvinpatel.dev live, **applications out** |

**Sprint laws:**
1. **The slip absorber is W11 RAG depth.** Never the DS&A ramp. Never the NotePilot deploy. Those are load-bearing walls.
2. **No scope additions mid-build.** New ideas go in `FUTURE.md` and become interview roadmap material ("here's what I'm doing next" — interviewers love a roadmap).
3. **The arsenal on application day:** NotePilot deployed with eval harness visible · DS&A mediums comfortable across core patterns · TrialMatch in-flight · Prelude = active real-world clinical engagement with a HIPAA compliance path. The story has a future tense on purpose.

---

## ⚡ PARALLEL TRACK: DS&A

*The LeetCode-medium gate stands between me and anyone ever seeing the moat. This track runs alongside everything — it never competes with a flagship for attention, and it never gets skipped.*

- 🔄 **Steady state (now → W8)** — 3–4 problems/week, patterns-first order: arrays & hashing → two pointers → sliding window → stack → binary search → trees → graphs → DP-lite. Small daily bricks, not a wall built in a weekend.
- ⬜ **The ramp (W9–12)** — daily grind + **timed** solves in the final two weeks. The clock is a separate skill from the solving.
- **Target:** comfortable with mediums across the core patterns. Not "500 solved."

---

## 🐍 PHASE 1: PYTHON CORE

*Goal: Become genuinely fluent in Python. Not "I can write code" fluent — "I can read, write, debug, and reason about real-world Python" fluent.*

### Completed Arcs

- ✅ 🎯 **CS50 Foundations** (Feb–Mar 2026) — C, JavaScript, computer science fundamentals
- ✅ 🎯 **Python Basics** — variables, data types, operators, f-strings, `return` vs `print`, booleans
- ✅ 🎯 **Control Flow** — `if`/`elif`/`else`, `while True`/`break` patterns, flag variables, De Morgan's Laws
- ✅ 🎯 **Data Structures: Lists, Dicts, Sets, Tuples** — indexing, slicing, mutation, nested structures, `.join()`, comprehensions
- ✅ 🎯 **Functions & Scope** — parameters, arguments, return values, default args, *args/**kwargs, list comprehension scoping (correctly caught my own Python 3 nuance 🏆)
- ✅ 🎯 **Randomness & Game Logic** — `random` module, sentinel values, loop architecture (Blackjack, Hangman, Higher Lower, Caesar cipher, calculator, password generator)
- ✅ 🎯 **Object-Oriented Programming** (April 2026) — classes, `__init__`, `self`, instance vs class attributes, inheritance, `super()`, polymorphism, MRO, dunder methods, OOP in the wild (Flask, LangChain, PyTorch)
- ✅ 🎯 **Error Handling & Exceptions** (April 2026) — `try`/`except`/`else`/`finally`, exception hierarchy, `raise`/`as`, custom exception classes, LBYL vs EAFP, defensive programming philosophy
- ✅ 🎯 **File I/O & Data Persistence** (April 2026) — file mental model (bytes/ledger entries/file descriptors), modes (r/w/a) with semantic contracts, `with` blocks as sugar over `__enter__`/`__exit__` protocol, reading patterns (`.read`/`.readlines`/iteration), `pathlib` with `/` as `__truediv__` overload, UTF-8 encoding deep dive (variable-width, combining characters), defensive per-row parsing, `csv.DictReader`/`DictWriter`, `json` module + 6-type constraint, streaming pattern for large files
- ✅ 🎯 **Modules, Packages & Virtual Environments** (May 2026) — `import` mechanics, `__name__ == "__main__"`, creating your own modules, `__init__.py`, packages, `pip`, `venv`/`uv`, `requirements.txt`, PyPI ecosystem. The "adulting" of Python.
- ✅ 🎯 **Decorators & Higher-Order Functions** (May 2026) — Functions as first-class citizens, closures, `*args`/`**kwargs` deep dive, writing decorators, `@property`, `functools.wraps`, real-world decorator patterns (logging, timing, auth). Bridge to FastAPI, LangChain, Flask.
- ✅ 🎯 **Working with APIs & HTTP** (June 2026) — `requests` library, HTTP methods (GET/POST/PUT/DELETE), status codes, headers, auth patterns, JSON payloads, rate limiting, error handling for network calls (callback to Error Handling arc). First real "talking to the internet" experience.
- ✅ 🎯 **Iterators, Generators & Comprehensions** (June 2026) — Iterator protocol, `yield` keyword, generator expressions vs list comprehensions, lazy evaluation, `itertools` module, memory efficiency at scale.
- ✅ 🎯 **Type Hints & Static Analysis** (June 2026) — Type annotations, `typing` module, `Optional`, `Union`, `List[str]` vs `list[str]`, generic types, `mypy`, why types matter in large codebases. Prep for modern Python and FastAPI.
- ✅ 🎯 **Testing** (June 2026) — `pytest` basics, unit tests, fixtures, mocking (patch where the name is *looked up*), TDD mindset, THE BRIDGE: an eval IS a test. Separates hobbyists from engineers — and forged the embryo of NotePilot's eval harness.
- ✅ 🎯 **Async Python** (July 2026, re-slotted into the FastAPI arc, pre-L6) — `async`/`await`, event loops, `asyncio`, concurrent vs parallel, when async matters vs when it's over-engineering. Prereq for modern web frameworks and LLM streaming.

---

## 🌐 PHASE 2: WEB FOUNDATIONS

*Goal: Build full-stack applications. Understand how the web actually works — frontend, backend, database, deployment. And then actually **ship** — an app that only runs on localhost is a diary entry, not a product.*

### Completed Arcs

### Backend

- ✅ 🎯 **HTTP & Web Fundamentals** (June 2026) — Client-server model, request/response cycle, REST principles, statelessness, cookies/sessions, CORS, HTTPS. The mental model everything else rests on.
- ✅ 🎯 **SQL & Databases** (June 2026) — Relational model, SELECT/INSERT/UPDATE/DELETE, JOINs, indexes, schema design, normalization, transactions/ACID, SQL injection + parameterized queries, PostgreSQL basics. Working with data at scale.
- ✅ 🎯 **SQLAlchemy / ORMs** (July 2026) — Why ORMs exist, models, relationships, queries, migrations (Alembic), when to drop to raw SQL. Python's bridge to databases. "The ORM rewards SQL knowledge, it doesn't replace it."
- ✅ 🎯 **FastAPI** (July 2026) — Route handlers, Pydantic models, dependency injection (fixtures foreshadowed this), background tasks, async endpoints (Async Python arc lands here, pre-L6), OpenAPI docs. Modern Python's favorite web framework and my bridge to AI integration.
  
- **Security thread (explicit, not a footnote):** OAuth2/JWT flows, secrets hygiene, PHI-adjacent data handling, threat-modeling lite. Health-AI targets make this non-negotiable — the SQL injection instinct, promoted to a standing thread.

### Frontend *(compressed — demo-grade, not mastery)*

- ⬜ **HTML & CSS Foundations** — *~3 lessons* · **W3**
  Semantic HTML, Flexbox, Grid, responsive design. The minimum viable frontend.

- ⬜ **JavaScript for Python Developers** — *~3–4 lessons* · **W3–4**
  Syntax differences, async JS, fetch API, DOM manipulation. Leveraging existing CS50 JS exposure.

- ⬜ **React, Demo-Grade** — *~5 lessons* · **W4**
  Components, props, state, hooks (useState, useEffect), lists and keys, forms, calling my own FastAPI backend. Enough to give NotePilot a face. **Deep dive (Joy of React back half, routing, state management) deferred to application season** — flagships need a UI, not frontend mastery.

### Shipping *(new — "deployment basics" was one sub-bullet; for my targets it's table stakes)*

- ⬜ **Shipping & Infrastructure** — *~4–5 lessons* · **W5**
  Docker + docker-compose, GitHub Actions CI (run the pytest suite on every push — callback to the Testing arc), deployment platforms (Render, Railway, Vercel), secrets management, structured logging. Environment isolation, secrets, and audit logging aren't DevOps trivia — they're **compliance primitives**. Prelude's HIPAA path is impossible without infrastructure thinking. Ends with 🚩 first live deploy.

- ⬜ **Git as a Team Sport** — *~2–3 lessons* · threads through W1–5
  Branching strategies, PRs and code review, rebase vs merge, conventional commits. Solo committing ≠ collaborative workflow — every target job works this way, and the bidirectional Ship Mode gate is already a code-review ritual; this formalizes the Git mechanics around it.

### Integration

- ⬜ **Full-Stack Application Architecture** — *~2–3 lessons* · folded into W4–5 and the NotePilot build
  Connecting React ↔ FastAPI, API design patterns, auth flows end-to-end. (Deployment content moved to Shipping & Infrastructure.)

---

## 🤖 PHASE 3: AI / LLM INTEGRATION

*Goal: Build AI-powered products. Not training models — integrating, orchestrating, and productizing existing ones. The rhythm of this phase: learn → **build** → learn → **build**. Nothing sits unapplied for long; every arc has a visible destination.*

- ⬜ **Prompt Engineering + LLM APIs & SDKs** — *~5–6 lessons* · **W6**
  Merged into one arc — I've already made raw authenticated calls to the Anthropic API. System prompts, few-shot, chain-of-thought, prompt templates; streaming responses, tool use / function calling, structured outputs, multi-turn conversations, token management, cost optimization.

- ⬜ **Evals & LLM Testing** — *~3–4 lessons* · **W7** · ⚔️ **THE MOAT ARC**
  Pulled forward from the end of the phase — the moat should not be the final boss, it should be the second weapon forged. Eval design, trap corpora, LLM-as-judge and its failure modes, severity triage, regression evals. Direct continuation of THE BRIDGE from the Testing arc: fuzzy asserts over a parametrize table.

### ◆ GATE: BUILD NOTEPILOT — *W8–10*
> Spec locked (`PROJECT_01_NOTEPILOT.md`), constitution written, adversarial review done. Three weeks of **pure execution** — the deciding was already bled for.
> **Step zero:** fix the two CRITICALs from adversarial review — (1) corpus scorer verdict inversion on detection-style trap cases, (2) retry loop must send a `tool_result` block with `is_error=True` referencing the original `tool_use_id`, not a plain-text user message.
> **Ships:** live deployed app + visible eval dashboard (the screen-share artifact). New ideas → `FUTURE.md`.

- ⬜ **Embeddings & Vector Databases** — *~3–4 lessons* · **W11 core, depth flexes**
  Text embeddings, semantic search, vector DBs (pgvector, Chroma, Pinecone), similarity search, RAG vs fine-tuning vs long context.

- ⬜ **RAG (Retrieval-Augmented Generation)** — *~5–6 lessons* · **W11–12 core; regrounding NotePilot = v2, application season**
  Document ingestion, chunking strategies, hybrid search, reranking, citation handling, evaluating retrieval quality (evals arc callback). The bread and butter of AI product engineering. **This arc is the designated slip absorber.**

- ⬜ **Agentic AI + MCP** — *~5–6 lessons* · application season
  Tool-using agents, planning patterns, ReAct, multi-agent systems, evaluating agentic systems. **MCP servers** — the 2026 standard for tool integration, and "built an MCP server" is a very legible portfolio line.
  **LangChain/LangGraph survey folded in** — *2–3 lessons, demoted from its own arc.* Understand LCEL and LangGraph well enough to converse in interviews and read others' code; flagships stay hand-rolled. "I understand the abstraction well enough to not need it" is a feature, not a gap.

### ◆ GATE: BUILD TRIALMATCH — *application season*
> Spec locked (`PROJECT_02_TRIALMATCH.md`). Bounded agentic retrieval loop → fixed eval-and-rank with three-valued Verdict (MET/FAILED/UNKNOWN), asymmetric aggregate, ranked by actionability. The **agentic** pattern flagship — deliberately a different GenAI architecture from NotePilot's pipeline. Ships mid-interview-season: the story grows while I'm in the room.

- ⬜ **Production AI Engineering** — *~4–5 lessons* · application season
  Observability (LangSmith, Langfuse), prompt versioning, A/B testing LLM outputs, cost/latency monitoring, guardrails, fallback patterns. (Evals removed — they got their own arc, where they belong.) What separates a demo from a product.

### ◆ GATE: SHIP PRELUDE — *post-Production arc*
> Spec locked (`PROJECT_03_PRELUDE.md`), CLAUDE.md at v1.1 with the bidirectional Ship Mode gate. A **real clinical engagement**: free-text complaint → tailored questionnaire from the physician-validated bank → structured HPI summary. Red-flag escalation is an operational safety **launch blocker**. Laddered data posture holds: synthetic → paper-parallel pilot → live, compliance stack first.

---

## 🎤 PHASE 3.5: APPLICATION SEASON

*Runs in parallel with the tail of Phase 3. Applying is when the campaign begins, not when the forging ends.*

- ⬜ **Interview readiness** — whiteboard-talking the flagship designs (the flagships + shipping arc *are* my system design education: a pipeline, an agent loop, and a compliance-constrained clinical system, designed from scratch), behavioral story bank, DS&A timed mocks
- ⬜ **Portfolio polish** — READMEs with demo GIFs, live deploy links, calvinpatel.dev as the front door
- ⬜ **React deep dive** — Joy of React back half, routing, state management
- 🔄 **TrialMatch build → Prelude advance** — the future tense of the interview story, kept true

---

## 🔮 PHASE 4: APPLIED ML *(far-future, will detail when we approach)*

*Intentionally left skeletal — this is the long-horizon evolution from AI Product Engineer → Applied AI/ML Engineer. Topics will include PyTorch, MLOps, clinical NLP, model fine-tuning, and domain-specific ML. We'll build this out properly closer to the time — the landscape will look different by then.*

---

## 📚 Supporting Materials & Tools

- **Primary environment:** PyCharm Pro (JetBrains Educational Pack — non-commercial; commercial seat via sponsorship when projects go live). DataGrip-engine DB tool window + built-in HTTP client, native.
- **Lecture exposure:** Angela Yu's 100 Days of Code (side dish, not main course)
- **Deep mastery:** Sessions with Claudia (Claude) · **Force multiplier:** Claude Code (Split/Ship mode per project constitutions)
- **Debugger:** Cortex (PyCharm's built-in)
- **Video supplements (mapped by arc):** Sanjeev Thiyagarajan's 19hr FastAPI course (the one long-form commitment — lands exactly in W1–2), techTFQ + Database Star (SQL), ArjanCodes (Python architecture), Fireship (patches), Joy of React (application season), 3Blue1Brown (NN intuition, Phase 4 horizon)
- **Version control:** Git + GitHub (`github.com/calvinpatel/code_C.A.L.`)
- **Personal domain:** `calvinpatel.dev`
- **LinkedIn positioning:** `Software Engineer | Python, AI, Data Analysis | Neuroscience BS (UCLA) · MHS (UMSOM) | Health × Tech`

---

## 🎯 Learning Principles (Cal's Operating System)

1. **Exploratory testing > pondering** — just poke at it in the REPL
2. **Sufficient depth > exhaustive depth** — go deeper when you hit a wall, not preemptively
3. **Errors are communication, not punishment** — a built-in professor giving real feedback
4. **Let code crash loudly during dev** — only catch what you can meaningfully recover from
5. **Concepts should become yours** — analogies, metaphors, and myths are how knowledge sticks (V12 in a Volkswagen, error handlers as Lucifer)
6. **Nitpicks are gifts** — standing order, continue with prejudice 💅🏾
7. **Synergy mode activated** — ADHD tamed, curiosity weaponized
8. **The projects are the deliverable, not the learning** — every arc has a build it feeds; nothing sits unapplied
9. **Application day = arsenal day, not graduation** — ship one thing fully; keep the story's future tense alive

---

*Last updated: July 2026 — sprint revision*
*Maintained by: Cal · surgery performed with Claudia* ◡̈
