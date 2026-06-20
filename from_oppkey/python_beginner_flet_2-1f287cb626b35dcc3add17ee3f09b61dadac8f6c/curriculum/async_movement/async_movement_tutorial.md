# Flet Movement Tutorial - Async Movement

## Overview

This tutorial teaches how to convert synchronous button-based movement into smooth, continuous async movement. Students will learn basic async concepts through hands-on coding without needing deep theoretical understanding.

**Starting Point:** `main.py` - Buttons that move character one step per click

**Learning Goal:** Understand how to make characters move continuously while a button is "active"

---

## Video 1: The Problem with Click-to-Move (5-7 minutes)

### Introduction

- Quick recap: We have a game with movement buttons
- Show current behavior: click button → character moves once
- Demonstrate the limitation: Can't hold button for continuous movement

### The Goal

- Show what we want: Hold button → character moves smoothly
- Explain that this requires "background processing"
- Preview: We'll use Python's `threading` and `asyncio` (don't worry about details yet)

### Key Concepts (Light Touch)

- **Synchronous:** One thing at a time (current code)
- **Asynchronous:** Multiple things happening (what we want)
- **Thread:** A separate "worker" that runs in the background

### What Students Will Type

- Just review `main.py` structure
- Point out the button `on_click` handlers
- No code changes yet

---

## Video 2: Setting Up Direction State (6-8 minutes)

### The Plan

- Instead of calling movement functions directly, buttons will set a "direction"
- A background loop will check the direction and move accordingly

### Step 1: Import Enum

```python
from enum import Enum
```

### Step 2: Create MovementDirection Enum

- Explain: Enum is like a list of allowed values
- Type in the Enum class with LEFT, RIGHT, UP, DOWN, IDLE
- Show how it prevents typos

### Step 3: Update State Dictionary

- Add `"direction": MovementDirection.IDLE` to state
- Explain: IDLE means "not moving"

### Step 4: Change Button Handlers

- Replace `on_click=move_left` with `on_click=lambda e: state.update({"direction": MovementDirection.LEFT})`
- Do this for all four buttons
- Explain: `lambda` is a tiny function, `state.update()` changes the direction
- Test: Show that buttons now just change direction (character doesn't move yet)

### Key Takeaway

- Buttons now "set intention" instead of "doing action"
- This separation is important for async code

---

## Video 3: Creating the Game Loop (7-9 minutes)

### The Idea

- We need something that runs continuously
- It checks the direction and moves the character
- This runs "in the background"

### Step 1: Create handle_movement Function

- Explain: This function takes a direction and calls the right movement function
- Use `match/case` (Python 3.10+) or `if/elif` for older Python
- Type in the function that routes to move_left, move_right, etc.

### Step 2: Create game_loop Function

- Explain: This runs forever, checking direction and moving
- Type: `def game_loop():` with `while True:`
- Inside: Call `handle_movement(state["direction"])`
- Add `time.sleep(0.1)` - explain this pauses for 0.1 seconds
- Import `time` at top

### Step 3: Start the Thread

- Import `threading` at top
- Explain: Thread = separate worker that doesn't block the UI
- Type: `thread = threading.Thread(target=game_loop, daemon=True)`
- Explain `daemon=True`: stops when main program stops
- Type: `thread.start()`
- Test: Character should now move continuously!

### Key Concepts (Light Touch)

- **Thread:** Background worker
- **Daemon:** Stops automatically when app closes
- **Sleep:** Pauses execution (prevents moving too fast)

### Common Issues

- Character moves too fast → adjust sleep time
- Character doesn't stop → need to handle IDLE (next video)

---

## Video 4: Adding the Update Queue (8-10 minutes)

### The Problem

- Thread is updating character position
- But Flet UI needs to be updated from the main thread
- We need a way to "signal" the UI to update

### The Solution: Queue

- Explain: Queue is like a mailbox
- Thread puts messages in queue
- UI checks queue and updates

### Step 1: Import queue

```python
import queue
```

### Step 2: Create Update Queue

- Type: `update_queue = queue.Queue()`
- Explain: This is our "mailbox"

### Step 3: Update game_loop

- After `handle_movement()`, add: `update_queue.put("update")`
- Explain: We're putting a message in the mailbox
- The message content doesn't matter, just that there's a message

### Step 4: Create check_updates Async Function

- Import `asyncio` at top
- Explain: `async` function can wait without blocking
- Type: `async def check_updates():`
- Inside: `while True:` loop
- Try to get from queue: `update_queue.get_nowait()`
- If successful: call `page.update()`
- If queue is empty: `except queue.Empty: pass`
- Always: `await asyncio.sleep(0.1)`

### Step 5: Start the Async Task

- Type: `page.run_task(check_updates)`
- Explain: This runs the async function in the background

### Test

- Character should move smoothly
- UI should update properly
- No freezing or lag

### Key Concepts (Light Touch)

- **Queue:** Thread-safe mailbox for messages
- **Async function:** Can wait without blocking other code
- **get_nowait():** Try to get item, don't wait if empty

---

## Video 5: Polishing and Understanding (5-7 minutes)

### Review What We Built

- Walk through the complete flow:
  1. Button click → updates state direction
  2. Thread loop → checks direction, moves character, puts message in queue
  3. Async loop → checks queue, updates UI

### Why This Pattern Works

- Thread handles game logic (doesn't freeze UI)
- Queue safely communicates between thread and UI
- Async function updates UI at right time

### Testing Different Scenarios

- Hold button: continuous movement
- Release button: set direction to IDLE (if implemented)
- Change speed: works with async movement
- Multiple buttons: only last direction matters

### Common Adjustments

- Movement speed: Change `time.sleep()` value
- Update frequency: Change `asyncio.sleep()` value
- Smoothness: Balance between the two sleep values

### What You Learned (Without Deep Theory)

- Threads let code run in background
- Queues let threads talk to main program
- Async functions can wait without blocking
- This pattern is common in game development

### Next Steps

- These concepts will be explored more in future lessons
- For now, you have a working async movement system!

---

## Summary Checklist

By the end of this tutorial, students should have:

- [ ] Added Enum for movement directions
- [ ] Changed buttons to update state instead of calling functions directly
- [ ] Created a game loop function that runs continuously
- [ ] Started the game loop in a thread
- [ ] Created an update queue
- [ ] Created an async function to check the queue
- [ ] Started the async task with `page.run_task()`
- [ ] Tested smooth, continuous movement

---

## Teaching Notes

### Concepts to Emphasize (Light Touch)

- Thread = background worker
- Queue = safe communication between threads
- Async = can wait without blocking
- Don't need to understand deeply yet - just that they work together

### Concepts to Defer

- Deep threading theory
- Async/await internals
- Queue implementation details
- Race conditions (mention briefly if asked)

### Common Student Questions

- "Why not just use a loop in the button handler?" → Would freeze UI
- "What if I forget daemon=True?" → Thread keeps running after app closes
- "Can I use multiple threads?" → Yes, but one is enough for now
- "What's the difference between sleep and await sleep?" → Thread vs async (simplified answer)

### Debugging Tips

- If character doesn't move: Check thread started, check direction is being set
- If UI freezes: Check async function is running, check sleep values
- If movement is jerky: Adjust sleep timings
- If character moves too fast: Increase sleep in game_loop
