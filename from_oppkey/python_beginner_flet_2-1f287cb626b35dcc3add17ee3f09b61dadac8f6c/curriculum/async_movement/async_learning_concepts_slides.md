---
marp: true
theme: default
paginate: true
header: "Async Movement Concepts | UC and CSU Computer Science Prep"
footer: "CS Preparation before college"
style: |
  section {
    font-size: 28px;
  }
  h1 {
    color: #0066cc;
    font-size: 48px;
  }
  h2 {
    color: #0099ff;
    font-size: 36px;
  }
  code {
    background-color: #f4f4f4;
    padding: 4px 8px;
    border-radius: 4px;
  }
---

<!-- _class: lead -->

# Async Movement Concepts

## Learning Slides for Video Tutorial

Preparing for UC and CSU Computer Science

---

# Video 1: The Problem

## Understanding Synchronous vs Asynchronous

---

## Current Behavior: Synchronous

**Synchronous = One thing at a time**

- Click button → Character moves once
- Click again → Character moves again
- Each action must finish before the next starts

**Like a single-lane road:**

- One car at a time
- Must wait for the car ahead to finish

---

## What We Want: Asynchronous

**Asynchronous = Multiple things happening**

- Hold button → Character moves continuously
- UI stays responsive
- Background work happens while UI updates

**Like a multi-lane highway:**

- Multiple cars moving at once
- Different lanes for different tasks

---

## The Key Concept: Threads

**Thread = A separate worker**

- Main program handles UI
- Background thread handles game logic
- They work together simultaneously

**Analogy:**

- Main program = Restaurant manager (handles customers)
- Thread = Kitchen staff (prepares food in background)

---

## Why This Matters

**Problem with synchronous:**

- If we loop in button handler → UI freezes
- User can't interact while loop runs
- Bad user experience

**Solution with async:**

- Background thread does the work
- UI stays responsive
- Smooth, professional feel

---

# Video 2: State Management

## Setting Intentions vs Taking Actions

---

## The Old Way: Direct Action

**Buttons directly call functions:**

```python
on_click=move_left  # Does the action immediately
```

**Problem:**

- Action happens once
- Can't hold button for continuous movement
- Tightly coupled (button → action)

---

## The New Way: Set State

**Buttons set a direction:**

```python
on_click=lambda e: state.update({"direction": LEFT})
```

**Benefits:**

- Button sets "intention"
- Background loop reads intention
- Separation of concerns

**Analogy:**

- Old: Button = "Move now!"
- New: Button = "I want to go left" (loop handles it)

---

## Enums: Type Safety

**Enum = List of allowed values**

```python
class MovementDirection(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
    IDLE = "idle"
```

**Why use Enums?**

- Prevents typos ("leff" vs "left")
- IDE autocomplete helps
- Clear, readable code
- Professional coding practice

---

## State Dictionary Pattern

**State holds current values:**

```python
state = {
    "speed": 5,
    "direction": MovementDirection.IDLE
}
```

**Benefits:**

- Single source of truth
- Easy to read current values
- Easy to update values
- Common pattern in game development

---

## Key Takeaway: Separation

**Before:**

- Button → Action (tightly coupled)

**After:**

- Button → State (sets intention)
- Loop → Action (reads state, acts)

**This separation enables:**

- Continuous movement
- Multiple input methods
- Complex game logic
- Professional code structure

---

# Video 3: Threading

## Background Workers

---

## What is a Thread?

**Thread = Separate execution path**

- Main program runs in main thread
- Background thread runs independently
- Both can run at the same time

**Real-world analogy:**

- Main thread = You (handling phone calls)
- Background thread = Assistant (doing research)
- Both working simultaneously

---

## The Game Loop Pattern

**Game loop = Continuous checking**

```python
def game_loop():
    while True:
        handle_movement(state["direction"])
        time.sleep(0.1)
```

**What it does:**

- Runs forever (while True)
- Checks direction every 0.1 seconds
- Moves character if needed
- Sleep prevents it from running too fast

---

## Why Sleep is Important

**Without sleep:**

- Loop runs millions of times per second
- CPU usage goes to 100%
- Computer becomes unresponsive
- Character moves too fast to see

**With sleep(0.1):**

- Loop runs 10 times per second
- Smooth movement
- Low CPU usage
- Professional feel

---

## Daemon Threads

**Daemon = Background service**

```python
thread = threading.Thread(target=game_loop, daemon=True)
```

**What daemon=True means:**

- Thread stops when main program stops
- No "zombie" threads left running
- Clean program shutdown
- Important for good code

**Without daemon:**

- Thread keeps running after app closes
- Can cause problems
- Always use daemon=True for background work

---

## Thread Safety Concept

**Thread safety = Safe sharing**

- Main thread: Updates UI, handles buttons
- Background thread: Updates game state
- Both read/write shared state

**Why it matters:**

- Two threads accessing same data
- Need to be careful about conflicts
- Queue helps with this (next video)

**For now:**

- Simple state updates are usually safe
- We'll add queue for UI updates

---

# Video 4: Queues and Async

## Communication Between Threads

---

## The Problem: Thread Communication

**Challenge:**

- Background thread updates character position
- UI thread must update the screen
- UI updates must happen on main thread
- How do they communicate?

**Solution: Queue**

---

## Queue: The Mailbox Pattern

**Queue = Thread-safe mailbox**

```python
update_queue = queue.Queue()
```

**How it works:**

- Background thread: `queue.put("message")`
- Main thread: `queue.get()` or `queue.get_nowait()`
- Thread-safe: Multiple threads can use safely

**Analogy:**

- Like a mailbox
- One person puts mail in
- Another person checks for mail
- Safe, organized communication

---

## The Update Flow

**Step 1: Background thread**

```python
handle_movement(state["direction"])
update_queue.put("update")  # Signal: "I changed something"
```

**Step 2: Main thread checks**

```python
try:
    update_queue.get_nowait()  # Any updates?
    page.update()  # Yes! Update the UI
except queue.Empty:
    pass  # No updates, continue
```

**Result:**

- Smooth UI updates
- No freezing
- Professional feel

---

## Async Functions: Non-Blocking Waits

**Async = Can wait without blocking**

```python
async def check_updates():
    while True:
        # Check queue
        await asyncio.sleep(0.1)  # Wait, but don't block
```

**Key difference:**

- `time.sleep()` = Blocks everything
- `await asyncio.sleep()` = Waits, but UI stays responsive

**Why async:**

- UI can still respond to clicks
- Other code can run
- Smooth user experience

---

## get_nowait() vs get()

**get_nowait() = Try, don't wait**

```python
try:
    update_queue.get_nowait()  # Try to get
except queue.Empty:
    pass  # Queue empty, that's OK
```

**Why not just get()?**

- `get()` waits until item available
- Would block the async function
- `get_nowait()` tries and continues
- Non-blocking is key for UI

---

## The Complete Pattern

**Three components working together:**

1. **State** - Holds current direction
2. **Thread** - Checks state, moves character, signals queue
3. **Async function** - Checks queue, updates UI

**Flow:**

```
Button → State → Thread → Queue → Async → UI Update
```

**This is a common pattern in:**

- Game development
- Real-time applications
- Professional software

---

# Video 5: System Overview

## Understanding the Complete System

---

## The Complete Flow

**Step 1: User Input**

- User clicks/holds button
- Button updates state direction

**Step 2: Background Processing**

- Thread loop checks direction
- Moves character if needed
- Puts message in queue

---

**Step 3: UI Update**

- Async function checks queue
- Updates UI if message found
- Waits briefly, repeats

**Result: Smooth, continuous movement**

---

## Why This Architecture Works

**Separation of Concerns:**

- UI thread: Handles user interaction
- Game thread: Handles game logic
- Queue: Safe communication

---

**Benefits:**

- Responsive UI (never freezes)
- Smooth movement (continuous)
- Professional code structure
- Scalable pattern

---

**This pattern is used in:**

- Video games
- Real-time applications
- Professional software
- UC CS courses!

---

## Key Concepts Summary

**Threads:**

- Background workers
- Run independently
- Don't block main program

---

**Queues:**

- Thread-safe communication
- Like a mailbox
- Safe data sharing

---

**Async:**

- Non-blocking waits
- UI stays responsive
- Modern Python pattern

---

## Real-World Applications

**Where you'll see this pattern:**

- **Video Games:** Game loop, rendering, input handling
- **Web Servers:** Handling multiple requests
- **Mobile Apps:** Background tasks, UI updates
- **Data Processing:** Background analysis, UI feedback

---

**UC/CSU CS Courses:**

- CS 1: Introduction to Programming (foundations, basic concepts)
- CS 2: Programming with Libraries (using libraries, state management)
- CS 3: Intermediate Programming (introduces threading, async patterns)

**You're learning professional patterns.**

---

## What You've Learned

**Concepts (Light Touch):**

- Threads enable background work
- Queues enable safe communication
- Async enables responsive UIs
- These work together for professional apps

---

**Skills:**

- Reading and modifying state
- Creating background threads
- Using queues for communication
- Writing async functions

---

**Pattern:**

- State → Thread → Queue → Async → UI
- Common in professional development
- Foundation for advanced topics

---

## Next Steps

**You now understand:**

- How async movement works
- Basic threading concepts
- Queue communication patterns
- Professional code structure

---

**Future lessons will explore:**

- Deeper threading theory
- More async patterns
- Advanced queue usage
- Performance optimization

---

**For now:**

- You have a working system!
- You understand the basics
- You're ready for more advanced topics

**Great job!**

---

<!-- _class: lead -->

# Questions?

## Keep coding and exploring.

**Remember:**

- Practice makes perfect
- These concepts will become clearer with use
- You're building professional skills
- UC or CSU CS will build on these foundations
