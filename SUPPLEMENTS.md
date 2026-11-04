# Supplements

Courses, documentation, and references that support [`ROADMAP.md`](./ROADMAP.md), organized by phase. Progress lives in the roadmap; this file is the resource list.

**How I choose resources**

- **Project-first.** Resources support structured study and the projects; they're never the main path.
- **Official and current first.** Maintainer-written docs and courses before third-party summaries.
- **Free by default.** Paid only when the mental model is clearly better.
- **Video only when the medium wins:** watching someone drive a tool (terminals, deploys, CI dashboards), inherently visual subjects, or building pattern intuition. Otherwise, text, docs, and interactive labs are faster.

---

## Phase 1 — Python Core

- **[CS50x](https://cs50.harvard.edu/x/)** and **[CS50P](https://cs50.harvard.edu/python/)** (Harvard) — Free. Computer science fundamentals, then Python. Exercises in `practice/cs50p/`.
- **100 Days of Code: The Complete Python Pro Bootcamp** (Angela Yu, Udemy) — Paid. Project-a-day practice. Exercises in `practice/angela_yu/`.
- **[Real Python](https://realpython.com)** — Paid. Tutorial reference throughout Phase 1.

## Phase 2 — Web Foundations

### HTTP, SQL & ORMs

- **[SQLBolt](https://sqlbolt.com)** and **Mode's SQL Tutorial** — Free. Interactive SQL practice.
- **techTFQ** and **Database Star** (YouTube) — Free. Query patterns and schema design.
- **[SQLAlchemy documentation](https://docs.sqlalchemy.org)** — Free. The ORM reference of record.

### FastAPI & security

- **Sanjeev Thiyagarajan — FastAPI course** (freeCodeCamp, YouTube, ~19 hrs) — Free. A full API build end to end: Postgres, auth, testing, deployment.
- **[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)** — Free. The official reference; its Security section covers OAuth2 and JWT.
- **[PortSwigger Web Security Academy](https://portswigger.net/web-security)** — Free. Interactive labs on authentication, JWT attacks, SQL injection, and access control.
- **[OWASP Top 10](https://owasp.org/www-project-top-ten/)** — Free. The shared vocabulary for web application risk.
- **ArjanCodes** (YouTube) — Free. Architecture and refactoring critiques of Python and FastAPI design.

### Frontend

- **[Josh Comeau's interactive guides](https://www.joshwcomeau.com)** — Free. Flexbox and Grid, taught through interactive widgets.
- **Kevin Powell** (YouTube) — Free. CSS layout and responsive patterns.
- **[MDN Web Docs](https://developer.mozilla.org)** — Free. The JavaScript and web platform reference.
- **[react.dev — Learn React](https://react.dev/learn)** — Free. The official path: components, props, state, hooks, forms.
- **[The Joy of React](https://www.joyofreact.com)** (Josh Comeau) — Paid. Deeper React mental models, including rendering, state management, and routing patterns.

### Shipping & infrastructure

- **[The Twelve-Factor App](https://12factor.net)** — Free. Why configuration lives in the environment and logs are event streams.
- **TechWorld with Nana** (YouTube) — Free. Docker and GitHub Actions walkthroughs.
- **[Docker: Get Started](https://docs.docker.com/get-started/)** and **[GitHub Actions quickstart](https://docs.github.com/actions/quickstart)** — Free. References for building the actual pipeline.

### Git for teams

- **[Learn Git Branching](https://learngitbranching.js.org)** — Free. Branching, rebasing, and merging as interactive visual puzzles.
- **[Oh Shit, Git!?!](https://ohshitgit.com)** — Free. Recovery recipes for common mistakes.
- **[Conventional Commits](https://www.conventionalcommits.org)** — Free. The commit message convention used in this repo.

## Scientific Python

- **[Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)** (Jake VanderPlas) — Free online. The NumPy and Matplotlib chapters.
- **[Scientific Python Lectures](https://lectures.scientific-python.org)** — Free. NumPy, SciPy, plotting, and image processing with scikit-image, edited by core developers of the stack.
- **[From Python to Numpy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)** (Nicolas Rougier) — Free. Vectorization: replacing Python loops with array operations.
- **[numpy-100](https://github.com/rougier/numpy-100)** — Free. One hundred graded NumPy exercises.
- **3Blue1Brown — Essence of Linear Algebra** (YouTube) — Free. Vectors, dot products, and transformations; groundwork for embeddings.

## Phase 3 — AI / LLM Integration

- **Andrej Karpathy — "Intro to Large Language Models" and "Deep Dive into LLMs"** (YouTube) — Free. What sits under the API: tokens, training, RLHF, and why models hallucinate.

### Prompt engineering + LLM APIs

- **[Anthropic Academy](https://anthropic.skilljar.com) — Building with the Claude API** — Free, certificate. Auth, streaming, tool use, prompt caching, extended thinking, and production patterns: error handling, retries, rate limiting, batching.
- **[Anthropic Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)** and **[Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)** — Free. Hands-on notebooks and a recipe reference.

### Evals & LLM testing

- **Hamel Husain — "Your AI Product Needs Evals"** — Free essay.
- **Anthropic's evaluation guides and Cookbook eval notebooks** — Free. Working patterns for building test sets and graders.
- **Eugene Yan — "Patterns for Building LLM-based Systems & Products"** — Free. The evals and guardrails sections.
- **Chip Huyen — *AI Engineering*** (O'Reilly) — The evaluation chapters.

### Embeddings, vector databases & RAG

- **[DeepLearning.AI — Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/)** — Free. Chunking, hybrid search, reranking, and retrieval evaluation.
- **pgvector documentation** and **Anthropic Cookbook RAG and citations recipes** — Free. Postgres-native vector search and grounded answers.

### Agents + MCP

- **Anthropic — "Building Effective Agents"** — Free essay. Workflows vs. agents, and when not to build an agent.
- **Anthropic Academy — Introduction to MCP → MCP: Advanced Topics** — Free, certificates. Building MCP servers and clients in Python, transports, and production patterns.
- **[Hugging Face Agents Course](https://huggingface.co/learn/agents-course)** — Free, certificate. How the wider ecosystem frames agents.
- **LangChain and LangGraph documentation** — Free. Survey depth: enough to read and discuss code that uses them.

### Production AI engineering

- **Langfuse documentation** — Free, open source. Tracing, cost, and latency monitoring for LLM applications.
- **Chip Huyen — *AI Engineering*** (production chapters) and **Eugene Yan and Hamel Husain's production writing** — Synthesis reading.

## Phase 4 — Applied ML

*A starting shortlist, finalized when the phase begins.*

- **[PyTorch tutorials](https://pytorch.org/tutorials/)** — Free. Tensors, autograd, and training loops.
- **3Blue1Brown — Neural Networks** (YouTube) — Free. Gradient descent and backpropagation, visually.
- **[Generative AI with LLMs](https://www.coursera.org/learn/generative-ai-with-llms)** (DeepLearning.AI / AWS, Coursera) — Free to audit. Pretraining, fine-tuning, and RLHF.
- **4A · Imaging & scientific ML:** **[Neuromatch Academy](https://neuromatch.io)** — Free, open course materials in computational neuroscience and deep learning — plus the scikit-image chapter of the Scientific Python Lectures.
- **4B · Clinical NLP:** **[Hugging Face NLP Course](https://huggingface.co/learn/nlp-course)** — Free, certificate. Transformers, tokenizers, and fine-tuning.

## Ongoing

- **Anthropic Academy — Claude Code 101 → Claude Code in Action → Introduction to Agent Skills → Introduction to Subagents** — Free, certificates. Hooks, subagent delegation, and Skills vs. `CLAUDE.md`.
- **[MIT — The Missing Semester](https://missing.csail.mit.edu)** — Free. Shell tools, debugging and profiling, and git's data model.
- **ArjanCodes** and **Fireship** (YouTube) — Free. Python design critiques, and fast overviews of new tools.

---

*Last updated: November 2026*
