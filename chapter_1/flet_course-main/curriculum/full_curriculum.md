# Oppkey Python Course Checklist
_updated Jan 7, 2026_

## UC CS Prep (Concept-First)

### A. Python Environment & Tooling

- [x] uv – Python package manager
- [x] Add packages with specific versions (`uv add flet==...`)
- [x] Import external packages (`import flet as ft`)
- [x] Define `main()`
- [x] Optional type hints
- [x] App folder structure (`assets/`)
- [x] Virtual environments (`.venv`), activation vs `uv run ...` (PYTH 1.04)
- [x] Understand Python import path (explicitly) (implied by PYTH 8.01–8.03, covered more in PYTH 11.2)

### B. Programming Fundamentals (Intro 1 / CS1 Core)

- [x] Python variable assigned to custom object
- [x] List data structure
- [x] Python `for` loop with `range`
- [x] Iterating over list with loop counters
- [x] Append to list
- [x] Insert into list
- [x] List deconstruction
- [x] List Comprehension
- [x] Function definition
- [x] Function definition with parameter
- [x] Python f-strings
- [x] Comment code with `#`
- [x] Conditionals (`if`, `elif`, `else`)
- [x] Boolean expressions (`and`, `or`, `not`) (PYTH 4.02; PYTH 2.04)
- [x] While loops
- [ ] String slicing and string methods
- [ ] Tuple basics (creation, unpacking)

### C. File I/O

- [ ] Read text files
- [ ] Write text files
- [ ] CSV-style parsing
- [ ] Strip newline and whitespace

### D. Dictionaries & Nested Data (CS1 → CS2 Bridge)

- [x] Dictionary basics (create, update, iterate)
- [x] Access & update dict values
- [x] Iterate through dictionaries (PYTH 9.03–9.05)
- [x] Nested structures (list of dicts, dict of lists) (PYTH 10.4; PYTH 9.03–9.05)
- [x] JSON-like data handling (PYTH 10.8; PYTH 7.04–7.06)

### E. Modules & Program Organization (CS2 Habits)

- [x] Split code across multiple files (PYTH 8.01–8.03)
- [x] Import from local modules (PYTH 8.01–8.03)

### F. Exceptions & Defensive Programming (Practical)

- [x] `try` / `except` (not explicitly listed in the chapter descriptions)
- [x] Handling common error cases (PYTH 10.2; PYTH 10.6)
- [x] Defensive programming (PYTH 10.2; PYTH 10.6)

### G. APIs & JSON (Common CS2 Topic)

- [x] Make network requests (`requests` or `httpx`) (PYTH 7.05; PYTH 10.1; PYTH 10.6–10.7)
- [x] Parse JSON responses (PYTH 10.8; PYTH 7.04–7.06)
- [x] Use dicts to extract fields (PYTH 10.8; PYTH 7.05)
- [x] Display results in Flet (PYTH 7.05; PYTH 10.4–10.6)

### H. Classes (CS2 Core)

- [x] Define a class (PYTH 9.03)
- [x] `__init__` and attributes (PYTH 9.03)
- [x] Create and use objects (PYTH 9.03–9.04)
- [x] Dataclasses (PYTH 9.08)

### I. Concurrency & Asynchrony (CS3-Relevant)

- [x] Synchronous vs asynchronous mental model (PYTH 3.01)
- [x] Threading basics (daemon threads, `sleep`) (PYTH 3.03)
- [x] Queues for thread-safe communication (PYTH 3.04)
- [x] Async functions (`async def`, `await`, `asyncio.sleep`) (PYTH 3.04; PYTH 4.01; PYTH 10.6)
- [x] Streaming patterns + async iteration (PYTH 10.6–10.8)

### J. Testing & Debugging

- [ ] Use `assert` for lightweight testing
- [ ] Test pure functions
- [x] Test a backend endpoint independently with `curl` (PYTH 7.06)
- [x] Test API endpoint in editor browser tab (PYTH 11.2)

### K. Program Design

- [x] Separate logic from UI
- [x] Decompose into helper functions
- [x] Understand side effects vs return values (PYTH 1.05; PYTH 3.02; PYTH 7.02)

## Portfolio / Industry Skills (Project-First)

### 1. Flet UI (Controls, Layout, Interaction)

- [x] Flet Page
- [x] Flet Row
- [x] Flet color, size, image from file
- [x] Network image
- [x] Buttons + event handlers (`on_click`) (PYTH 2.01; PYTH 6.03)
- [x] Icons + `IconButton` (PYTH 2.01)
- [x] `Stack` + absolute positioning (PYTH 2.02)
- [x] Slider + UI-driven state (PYTH 2.03)
- [x] Bounds/constraint logic in UI (PYTH 2.04)
- [x] GridView (PYTH 9.01)
- [x] Dropdown menus + selection handlers (PYTH 9.02–9.04)
- [x] SnackBar notifications (PYTH 9.06–9.07)

### 2. Full-Stack Python (FastAPI + Flet)

- [x] FastAPI basics (routes, GET/POST) (PYTH 7.03–7.06)
- [x] Health check endpoint (`/health`) (PYTH 7.03)
- [x] Pydantic request schemas + validation (PYTH 7.04)
- [x] UI → API requests + UI updates from response (PYTH 7.05)
- [x] Separation of concerns (UI vs backend) (PYTH 7.02; PYTH 7.06)

### 3. Servers, Real-Time Architecture, and Deployment

- [x] ASGI + Uvicorn mental model / usage (PYTH 4.02; PYTH 5.02)
- [x] Docker basics (Dockerfile, images/containers mental model) (PYTH 4.04; PYTH 5.03)
- [x] Fly.io deployment workflow + config basics (PYTH 4.04)

### 4. Git / Project Sharing

- [x] Git/GitHub basics (repo setup, `.gitignore`, README, screenshots) (PYTH 4.03)

### 5. AI App Patterns (Ollama + Streaming + UI)

- [x] Local LLM via Ollama HTTP API (PYTH 10.1)
- [x] Performance/tuning + error handling patterns (PYTH 10.2)
- [x] Chat UI: message list, roles, scrolling output (PYTH 10.4)
- [x] Upgrade workflow with uv + lockfile regeneration (PYTH 10.5)
- [x] Streaming tokens/chunks + incremental rendering (PYTH 10.6–10.9)
- [x] Async streaming with `httpx.AsyncClient` (PYTH 10.6–10.7)
