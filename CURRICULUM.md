# Cal's Python → Web → AI Curriculum

> *The trio's official roadmap. Cal, Cortex, and Claudia — we push, we fight, we return not None.* ⚔️

**Format:** Topic-level with rough lesson estimates. Lessons emerge organically within each arc. Independent of Angela Yu's 100 Days of Code, with parallel coverage noted where relevant.

**Legend:**
- ✅ Completed
- 🔄 In progress
- ⬜ Not yet started
- 🎯 Final boss quiz passed

> 📚 Supplemental courses and external resources tracked in [`SUPPLEMENTS.md`](./SUPPLEMENTS.md).

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


### Current & Upcoming

- ⬜ **Type Hints & Static Analysis** — *~3-4 lessons*
  Type annotations, `typing` module, `Optional`, `Union`, `List[str]` vs `list[str]`, generic types, `mypy`, why types matter in large codebases. Prep for modern Python and FastAPI.

- ⬜ **Async Python** *(optional — can defer)* — *~4-5 lessons*
  `async`/`await`, event loops, `asyncio`, concurrent vs parallel, when async matters vs when it's over-engineering. Prereq for modern web frameworks and LLM streaming.

- ⬜ **Testing** *(optional but highly recommended)* — *~3-4 lessons*
  `pytest` basics, writing unit tests, fixtures, mocking, TDD mindset. Separates hobbyists from engineers.

**Phase 1 completion target:** Portfolio Project #1 — Neuroscience game (Python-only, leverages OOP + error handling + file I/O)

---

## 🌐 PHASE 2: WEB FOUNDATIONS

*Goal: Build full-stack applications. Understand how the web actually works — frontend, backend, database, deployment.*

### Backend

- ⬜ **HTTP & Web Fundamentals** — *~3-4 lessons*
  Client-server model, request/response cycle, REST principles, statelessness, cookies/sessions, CORS, HTTPS. The mental model everything else rests on.

- ⬜ **SQL & Databases** — *~6-8 lessons*
  Relational model, SELECT/INSERT/UPDATE/DELETE, JOINs, indexes, schema design, normalization, PostgreSQL basics. Working with data at scale.

- ⬜ **SQLAlchemy / ORMs** — *~4-5 lessons*
  Why ORMs exist, models, relationships, queries, migrations (Alembic), when to drop to raw SQL. Python's bridge to databases.

- ⬜ **FastAPI** — *~6-8 lessons*
  Route handlers, Pydantic models, dependency injection, authentication, background tasks, async endpoints, OpenAPI docs. Modern Python's favorite web framework and your bridge to AI integration.

### Frontend

- ⬜ **HTML & CSS Foundations** — *~3-4 lessons*
  Semantic HTML, Flexbox, Grid, responsive design. The minimum viable frontend.

- ⬜ **JavaScript for Python Developers** — *~4-5 lessons*
  Syntax differences, async JS, fetch API, DOM manipulation. Leveraging existing CS50 JS exposure.

- ⬜ **React Fundamentals** — *~8-10 lessons*
  Components, props, state, hooks (useState, useEffect), conditional rendering, lists and keys, forms, lifting state, basic routing. The frontend ecosystem Python pairs with most.

### Integration

- ⬜ **Full-Stack Application Architecture** — *~3-4 lessons*
  Connecting React ↔ FastAPI, state management, API design patterns, auth flows end-to-end, deployment basics (Render, Vercel, Railway).

**Phase 2 completion target:** Portfolio Project #2 — Health web app (full-stack, real DB, user-facing)

---

## 🤖 PHASE 3: AI / LLM INTEGRATION

*Goal: Build AI-powered products. Not training models — integrating, orchestrating, and productizing existing ones.*

- ⬜ **Prompt Engineering Fundamentals** — *~3-4 lessons*
  System prompts, few-shot examples, chain-of-thought, prompt templates, evaluation, common pitfalls. The foundation of everything AI-product-related.

- ⬜ **LLM APIs & SDKs** — *~4-5 lessons*
  Anthropic Claude API, OpenAI API, streaming responses, tool use / function calling, structured outputs (JSON mode), multi-turn conversations, token management, cost optimization.

- ⬜ **Embeddings & Vector Databases** — *~4-5 lessons*
  Text embeddings, semantic search, vector DBs (Pinecone, pgvector, Chroma), similarity search, when to use RAG vs fine-tuning vs long context.

- ⬜ **RAG (Retrieval-Augmented Generation)** — *~5-6 lessons*
  Document ingestion, chunking strategies, hybrid search, reranking, citation handling, evaluating retrieval quality. The bread and butter of AI product engineering.

- ⬜ **LangChain / LangGraph** — *~4-5 lessons*
  LCEL (LangChain Expression Language), chains, agents, memory, LangGraph for multi-step workflows. When to use it vs roll your own.

- ⬜ **Agentic AI** — *~5-6 lessons*
  Tool-using agents, planning patterns, ReAct, multi-agent systems, evaluation of agentic systems, where Anthropic and OpenAI are pushing this.

- ⬜ **Production AI Engineering** — *~4-5 lessons*
  Observability (LangSmith, Langfuse), evals, prompt versioning, A/B testing LLM outputs, cost/latency monitoring, guardrails, fallback patterns. What separates a demo from a product.

**Phase 3 completion target:** Portfolio Project #3 — AI-powered health tool with RAG. Potential alternate: Astrology app (Co-Star-inspired, personality-driven LLM readings).

---

## 🔮 PHASE 4: APPLIED ML *(far-future, will detail when we approach)*

*Intentionally left skeletal — this is the long-horizon evolution from AI Product Engineer → Applied AI/ML Engineer. Topics will include PyTorch, MLOps, clinical NLP, model fine-tuning, and domain-specific ML. We'll build this out properly closer to the time — the landscape will look different by then.*

---

## 📚 Supporting Materials & Tools

- **Primary environment:** PyCharm Pro (UMSOM license)
- **Lecture exposure:** Angela Yu's 100 Days of Code (side dish, not main course)
- **Deep mastery:** Sessions with Claudia (Claude)
- **Debugger:** Cortex (PyCharm's built-in)
- **YouTube supplements:** 3Blue1Brown (NN intuition), Fireship (modern web/dev culture), @b001 (Python optimization)
- **Version control:** Git + GitHub (`github.com/calvinpatel`)
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

---

*Last updated: April 2026*
*Maintained by: Cal + Claudia*
