# SUPPLEMENTS.md

Companion to [`CURRICULUM.md`](./CURRICULUM.md). Supplemental learning resources correlated **arc-by-arc** to the curriculum, aimed at the **AI Product Engineer → Applied AI/ML Engineer** trajectory.

> **Philosophy:** Project-first. Current tooling. Free-or-cheap by default. Paid only when the mental model is genuinely better. Supplements run at roughly 20–30% of learning time per phase — Claudia's arcs and the flagship builds are the main course; these are seasoning.
>
> **The video rule:** Video earns a slot only when the medium wins — (a) watching someone *drive* something (terminals, dashboards, deploys), (b) inherently visual subjects, (c) algorithm pattern intuition. Otherwise text/docs/interactive labs are faster, and video is a comfort trap.

**Role tags** *(when a supplement slots relative to a Claudia arc)*:
- 🌅 **Prelude** — before the arc; builds intuition so lessons land harder
- 🔧 **Intra-lesson** — alongside; reference or practice as topics surface
- 🌙 **Wrap-up** — after; consolidation, depth, or spaced reinforcement

**Sprint weeks** (W1–W12) reference the operating plan in `CURRICULUM.md`.

---

## ⚰️ Retired & Completed

*Kept for the record — knowing what was cut and why is part of the map.*

- ~~**The Odin Project — Full-Stack JS path**~~ — **CUT.** Made sense against a 15-lesson frontend arc; against a 12-week sprint with demo-grade React it cannibalizes build time (Flatiron-bootcamp logic). Its portfolio artifact is strictly dominated by the flagships.
- ~~**Real Python**~~ — **Cancel the subscription.** Phase 1 complete; the "3–4 months then cancel" clock has run. Resubscribe-if-needed reference only.
- ~~**SQLBolt / Mode SQL Tutorial**~~ — SQL arc ✅ 🎯. Retired.
- ~~**Obey the Testing Goat**~~ — Testing arc ✅ 🎯, and its Django/Selenium lane isn't mine. Retired with honors; THE BRIDGE lives on in the evals arc.
- ~~**DLAI: Building Systems with the ChatGPT API / LangChain for LLM App Dev / Functions, Tools & Agents with LangChain / Agentic RAG with LlamaIndex**~~ — Superseded by **Anthropic Academy** (Claude-centric, official, free, certificated) and by LangChain's demotion to a survey in the curriculum.

---

## 🌐 PHASE 2 — Remaining Arcs

### FastAPI + async + security thread · *W1–2*

- 🌅🔧 **Sanjeev Thiyagarajan — FastAPI full course (freeCodeCamp, ~19 hrs)** — Free, YouTube. *The* one long-form video commitment; video wins here (watching someone drive a real API build end-to-end, incl. Postgres, auth, deployment). Stay in PyCharm; adapt, don't switch. Consume in slices synced to lessons, not as a binge.
- 🔧 **[FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/)** — Tiangolo's docs. Free. The reference of record; the Security section is the intra-lesson companion for the OAuth2/JWT lessons specifically.
- 🔧 **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** — Free, interactive labs. **Security-thread anchor.** Cherry-pick: authentication vulnerabilities, JWT attacks, SQL injection (arc callback), access control. Interactive labs beat both video and reading here — you *break* things.
- 🌙 **[OWASP Top 10](https://owasp.org/www-project-top-ten/)** — Free, one-afternoon read after the security lessons. The shared vocabulary every health-tech interview expects.
- 🌙 **ArjanCodes (YouTube)** — Free. Architecture/refactoring critiques of FastAPI + Python design. Wrap-up viewing: sharpens taste after the mechanics land.

### Frontend, compressed · *W3–4*

- 🔧 **[Josh Comeau's free interactive guides](https://www.joshwcomeau.com)** — Flexbox and Grid interactive articles. Free. The Joy of React author's blog; the interactive widgets ARE the mental model.
- 🔧 **Kevin Powell (YouTube)** — Free. CSS is a visual subject; video wins. Targeted hits only (flexbox, grid, responsive patterns) — not a playlist binge.
- 🔧 **[MDN Web Docs](https://developer.mozilla.org)** — Free. The JS reference of record for the JS-for-Python-devs arc.
- 🔧 **[react.dev — Learn React](https://react.dev/learn)** — Free, official. The demo-grade React path: exactly the compressed scope (components, props, state, hooks, forms). This IS the arc's textbook.
- ⏸️ **[The Joy of React](https://www.joyofreact.com)** — Josh Comeau, ~$300 (wait for ~$200 sale). **Still the one paid course worth defending — but deferred to application season** with the React deep dive. Buying it in W3 would tempt scope creep past demo-grade.

### Shipping & Infrastructure · *W5*

- 🌅 **[The Twelve-Factor App](https://12factor.net)** — Free, ~30-min read. The prelude: *why* config lives in the environment, why logs are streams. Makes every Docker lesson land as "oh, that's factor III" instead of arbitrary ritual.
- 🌅🔧 **TechWorld with Nana — Docker crash course + GitHub Actions tutorial (YouTube)** — Free. Video wins decisively for ops: watching someone drive terminals, Dockerfiles, and CI dashboards is the medium. ~3 hrs Docker + ~1 hr Actions.
- 🔧 **[Docker — Get Started docs](https://docs.docker.com/get-started/)** + **[GitHub Actions quickstart](https://docs.github.com/actions/quickstart)** — Free. Reference of record while building the actual pipeline (pytest-on-push is the arc capstone).
- 🌙 **[MIT — The Missing Semester](https://missing.csail.mit.edu)** — Free. Demoted from "full ~10 lectures" to **cherry-picked**: shell tools, debugging/profiling, and the git lecture (see next arc). High ROI for the self-taught; the rest is optional dessert.

### Git as a Team Sport · *threads through W1–5*

- 🔧 **[Learn Git Branching](https://learngitbranching.js.org)** — Free, interactive. Branching/rebase/merge as a visual puzzle game — interactive beats everything for this topic.
- 🌅 **Missing Semester — Git lecture** — Free video. Git's *data model* (the content-addressed DAG underneath), which makes rebase-vs-merge obvious instead of memorized.
- 🔧 **[Oh Shit, Git!?!](https://ohshitgit.com)** — Free. The panic-recovery reference. Bookmark, don't study.
- 🌙 **[Conventional Commits spec](https://www.conventionalcommits.org)** — Free, 10-min read. Already half-adopted in code_C.A.L.; this formalizes it.

---

## ⚡ DS&A PARALLEL TRACK · *now → W12*

- 🔧 **NeetCode 150 / Blind 75 (neetcode.io + YouTube)** — Free. Already canon. The explanation videos are the supplement: pattern intuition is the third case where video wins. Rule: 25 minutes honest attempt → watch → redo pile.
- 🌙 **NeetCode pattern-intro videos per new pattern** — 🌅 before entering each new pattern family (sliding window, graphs, DP-lite), one overview video; then problems.
- ❌ **Skipped deliberately:** Grokking the Coding Interview (paid, redundant with NeetCode), AlgoMonster, LeetCode Premium (revisit only if a target company's question bank matters in W11–12).

---

## 🤖 PHASE 3 — AI/LLM Integration

*The highest-leverage phase for supplements — and the phase where the supplement landscape changed most. **Anthropic Academy** (launched March 2026, `anthropic.skilljar.com`) is now the spine: official, free, self-paced, certificate per course. Education + recon + the one cert genre that reads as real signal, because it comes from the model provider itself.*

### Prompt Engineering + LLM APIs · *W6*

- 🌅 **Andrej Karpathy — "Intro to Large Language Models" (1 hr) → "Deep Dive into LLMs" (3.5 hr, optional)** — Free, YouTube. The Phase 3 prelude: the best free grounding in what's actually under the API (tokens, training, RLHF, why models hallucinate). This is the depth that separates candidates in AI-company interviews. Conceptual-video exception, fully earned.
- 🔧 **Anthropic Academy — "Building with the Claude API"** — Free, official, certificate. 8+ hrs / 84 lectures: auth, streaming, tool use, prompt caching, extended thinking, and production patterns (error handling, retry logic, rate limiting, batching) in Python + TS. **The W6 anchor supplement** — and direct recon on how Anthropic engineers think.
- 🔧 **[Anthropic Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)** + **[Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)** — Free. Notebooks = learn by doing; Cookbook doubles as the reference shelf for the NotePilot build.

### Evals & LLM Testing — THE MOAT ARC · *W7*

- 🌅 **Hamel Husain — "Your AI Product Needs Evals"** — Free essay. The closest thing the field has to a canonical text on the moat. Read before Lesson 1.
- 🔧 **Anthropic docs — empirical evaluation guides + Cookbook eval notebooks** — Free. Working examples to steal patterns from while building the NotePilot trap corpus.
- 🌙 **Eugene Yan — "Patterns for Building LLM-based Systems & Products"** — Free. The evals + guardrails sections; wrap-up synthesis.
- 🌙 **Chip Huyen — *AI Engineering*, evaluation chapters** — Already owned (see `cals_ai_reading_list.md`). The deep-work-canon cross-reference for this arc; read the eval chapters the weekend after the arc closes.

### ◆ NotePilot build · *W8–10*
> **No new supplements during builds.** The spec, the constitution, and the Cookbook reference shelf are the whole diet. Supplement consumption during a build gate is procrastination wearing a productivity costume.

### Embeddings, Vector DBs & RAG · *W11 core; regrounding = v2*

- 🔧 **[DeepLearning.AI — "Building and Evaluating Advanced RAG"](https://www.deeplearning.ai/short-courses/)** — Free, ~1–2 hrs. The one DLAI short course that survived the audit: chunking, hybrid search, reranking, *and* retrieval evals (moat callback). Check the current catalog for a newer equivalent when W11 arrives — this shelf turns over fast.
- 🔧 **pgvector docs + Anthropic Cookbook RAG/citations recipes** — Free. Postgres-native vectors keep the NotePilot stack coherent (no new database vendor for v2).

### Agentic AI + MCP · *application season*

- 🌅 **Anthropic — "Building Effective Agents"** — Free essay. The canonical taxonomy (workflows vs agents, when NOT to build an agent). TrialMatch's bounded-loop design is already this essay's philosophy; read it to name what you built.
- 🔧 **Anthropic Academy — "Introduction to MCP" → "MCP: Advanced Topics"** — Free, official, certificates. Build MCP servers/clients in Python; the advanced course covers transports and production patterns. Consistently rated the most valuable courses in the catalog — and "built an MCP server" is a legible portfolio line.
- 🌙 **[Hugging Face Agents Course](https://huggingface.co/learn/agents-course)** — Free, certificate. Breadth pass after TrialMatch ships: see how the non-Anthropic half of the ecosystem frames agents.
- 🔧 **LangChain/LangGraph official docs, survey-depth only** — Free. Enough LCEL/LangGraph to converse and read others' code. Matches the curriculum demotion; no course needed.

### Production AI Engineering · *application season*

- 🔧 **Langfuse docs + self-host quickstart** — Free/OSS. Instrument NotePilot for real: traces, cost, latency. The observability lesson becomes a portfolio screenshot.
- 🌙 **Chip Huyen — *AI Engineering*, production chapters** + **Eugene Yan / Hamel Husain production posts** — Free/owned. The synthesis shelf.

---

## 🛠️ TOOLING TRACK *(ongoing, low-dose)*

- 🔧 **Anthropic Academy — "Claude Code 101" → "Claude Code in Action" → "Introduction to Agent Skills" → "Introduction to Subagents"** — Free, ~2–3 hrs combined, certificates. Already a daily Claude Code driver in Split/Ship mode — these fill gaps you don't know you have (hooks, subagent delegation, Skills vs CLAUDE.md). Slot into low-energy evenings; they compound the force multiplier.

---

## 🎤 APPLICATION SEASON

- 🔧 **The Joy of React** — Now it earns its ~$200–300: the React deep dive slot exists in Phase 3.5 and the mental-model teaching is the point. The one paid course, still defended.
- 🌙 **[Hugging Face NLP Course](https://huggingface.co/learn/nlp-course)** — Free, certificate. Phase 4 on-ramp; the real artifact is a fine-tuned model on HF Hub.
- 🌙 **[Generative AI with LLMs (DeepLearning.AI / AWS, Coursera)](https://www.coursera.org/learn/generative-ai-with-llms)** — Free to audit. Re-slotted from Phase 3 core to here: what's *under* the API (pretraining, fine-tuning, RLHF) — pairs with Karpathy's deep dive and bridges toward Phase 4.

---

## 📜 Cert Posture *(revised)*

Hiring for the target list is portfolio + interview signal; certs are tiebreakers — **with one new exception**:

- **Anthropic Academy certificates** — the exception that proves the rule. Free, issued directly by the model provider, LinkedIn-legible, and earned as a byproduct of courses worth taking anyway. Collect them incidentally; never chase them.
- **Defer to Phase 4:** AWS Certified Machine Learning Engineer – Associate. Genuinely useful for applied ML roles, but only meaningful once skills are in place.
- **Skip:** TensorFlow Developer Cert (discontinued 2024), Azure AI-102 (wrong cloud for the target list), generic Udemy/Coursera "AI Engineer" certs.

---

*Last updated: July 2026 — correlated to the CURRICULUM.md sprint revision*
*Maintained by: Cal · audit performed with Claudia* ◡̈
