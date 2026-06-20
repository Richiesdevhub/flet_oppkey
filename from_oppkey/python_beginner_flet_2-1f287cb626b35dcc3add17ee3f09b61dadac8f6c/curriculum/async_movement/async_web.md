# Tutorial: Refactoring Our Flet Game from Threads to `asyncio`

_Preparing students for CS coursework, interviews, and real-world engineering_

---

## 1. Introduction

In this lesson, we refactor our Flet game from using:

- `threading.Thread`
- `queue.Queue`
- `time.sleep`

to a clean **async/await** model using:

- `asyncio`
- `page.run_task()`

This refactor aligns our code with:

1. The **Flet 1.0+ architecture** (where asyncio is the recommended path).
2. **Browser/WebAssembly constraints** (Pyodide does not support threads).
3. **Industry-standard async programming patterns** used in FastAPI, Node, distributed systems, and cloud applications.

This is the exact type of conceptual transition students encounter in:

- University CS courses (ICS 32, ICS 45C/45J, systems programming, OS, networking)
- Internships (writing async services, non-blocking event loops)
- Interviews (understanding concurrency models)

---

## 2. Learning Objectives

By the end of the tutorial, students will:

- Understand the differences between **multithreading** and **async concurrency**.
- Learn why **threading does not work in browser environments** (Pyodide).
- Recognize the **limits of threads** and why modern systems prefer async for I/O-driven tasks.
- Refactor a working game to use idiomatic asyncio loops.
- Build intuition for how async code is used in **FastAPI**, cloud services, and scalable backend systems.

---

## 3. Why We Are Refactoring: CS & Internship Perspective

### 3.1 Threads Are Useful, but Not Always Practical

Threads teach:

- Producer/consumer patterns
- Race conditions
- Shared-state coordination
- Blocking vs non-blocking execution

These concepts absolutely help students in:

- Operating Systems classes
- Systems architecture
- Parallel programming
- Low-level debugging during internships

However…

### 3.2 Modern Software Uses Async More Than Threads

Most real-world scalable systems avoid spinning up arbitrary threads inside an application.

Examples:

- **FastAPI** uses an event loop and async/await for nearly all parts of the stack.
- **Databases and message queues** rely on async drivers.
- **Cloud services** (AWS Lambda, GCP Cloud Run) are built around async I/O models.
- **Browser runtime** cannot use Python threads at all.

Understanding async programming directly supports:

- Backend development (FastAPI, Django async, QUIC/HTTP3 systems)
- Microservices
- Realtime apps (websockets, streaming APIs)
- Interview questions such as "explain event loops" and "explain async vs threads."

### 3.3 Pyodide + Flet Web Requires Async

If we want our game to run in:

- Static web builds
- GitHub Pages
- Pyodide

Then **threads are impossible**. WebAssembly currently _cannot_ create Python threads.

Async is the correct concurrency model for the browser.

---

## 4. Original Architecture (Thread + Queue Model)

Before refactoring, our game logic used:

- A background Python thread running `while True: ...`
- `time.sleep(0.1)`
- A queue to notify the main UI loop to update
- An async task polling the queue

### Why it works on desktop:

- CPython supports threads.
- Flet desktop apps can call blocking functions without halting UI.

### Why it fails on the web:

- Pyodide forbids threads.
- `time.sleep()` blocks the entire WebAssembly runtime.
- Browsers allow only cooperative (async) concurrency.

---

## 5. Target Architecture (Pure Async Model)

We replace:

- The thread
- The queue
- The blocking sleep

with a single async loop:

```python
async def game_loop():
    while True:
        handle_movement(...)
        page.update()
        await asyncio.sleep(0.1)
```

And run it via:

```python
page.run_task(game_loop)
```

### Benefits:

- Works on desktop, server, and web.
- Uses non-blocking concurrency.
- Matches Flet 1.0’s recommended async architecture.
- Builds intuition for async services used in real-world production.

---

## 6. Step-by-Step Refactor Script

### Step 1 — Remove Threading Imports

Explain:

- “We no longer need `threading`, `queue`, or `time.sleep`.”

### Step 2 — Replace Background Thread With Async Function

Show old vs new patterns.

Old:

```python
thread = threading.Thread(target=game_loop, daemon=True)
thread.start()
```

New:

```python
page.run_task(game_loop)
```

### Step 3 — Replace `time.sleep()` With `await asyncio.sleep()`

Explain:

- `await asyncio.sleep()` yields control to the event loop.
- UI remains responsive.
- Works in Pyodide.

### Step 4 — Remove the Queue

Explain:

- In an async event loop, we do not need the queue to signal updates.
- We can update the page directly inside the loop.

### Step 5 — Explain Why This Model Scales

Discuss:

- Event loops.
- Cooperative multitasking.
- How frameworks like FastAPI mirror the same async design.

---

## 7. Walkthrough of the New Code

Guide the student line-by-line through:

- The async loop
- The movement handler
- The controller button event updates
- How the loop “ticks” at 10 FPS
- Why this pattern is stable across all platforms

---

## 8. Summary: What Students Should Understand

By the end of the refactor:

- Threads are useful but limited, especially in browser settings.
- Async is the dominant concurrency model for modern engineering.
- Flet + FastAPI share the same conceptual async foundation.
- Learning async early gives students an advantage in:
  - College CS courses
  - Internships
  - Technical interviews
  - Real-world engineering

Students now understand:

- Event loops
- Non-blocking waits
- State-driven UI updates
- How async replaces threads in cross-platform applications

---

## 9. Next Steps

Suggested directions:

- Add animation easing or acceleration using async.
- Add collision detection.
- Add keyboard controls.
- Later: integrate FastAPI backend calls asynchronously.
- Discuss async DB drivers (PostgreSQL, SQLite via aiosqlite, etc.)
- Introduce proper job queues (Redis/Celery/RQ) as a follow-up to the “threading/queue” concept.

---

## 10. Closing

Reinforce:

- This refactor is not just about Flet—it’s building the concurrency foundation used everywhere in modern software.
- The skills learned here map directly to advanced CS courses and practical backend engineering.
