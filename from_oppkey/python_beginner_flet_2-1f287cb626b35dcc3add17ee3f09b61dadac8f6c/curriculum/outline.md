# Oppkey Python Beginner Course Flet Module 2: 5 Sections

| Lesson | Topic / Goal                                   | Flet Components Introduced                                     | Python Concepts Reinforced / Introduced                           | Student Outcome                                                                         |
| ------ | ---------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **1**  | Buttons with icons for movement                | `IconButton`, `Row`, `Column`, material icons                  | Event handlers (`on_click`), functions                            | Students build a directional control pad (up, down, left, right).                       |
| **2**  | Move a character image by 10px per press       | `Container` for positioning, `Image`, `Stack`, `page.update()` | State variables (`x`, `y`), updating control properties           | Character moves on screen with button presses.                                          |
| **3**  | Slider to adjust movement speed (2–10px)       | `Slider`, `Text`                                               | Reading widget values, event handling (`on_change`), shared state | Students adjust movement speed like a game settings menu.                               |
| **4**  | Boundaries and collision using `if` statements | `Container` (for walls/boundaries), optional `Stack`           | `if / elif / else`, boolean logic                                 | Character stops when reaching the edges of the play area.                               |
| **5**  | Auto-movement using a `while` loop             | Optional `Switch`, optional `ProgressBar`                      | `while` loops, break conditions, basic timing (`time.sleep`)      | Character auto-moves until hitting a boundary, demonstrating simple game loop behavior. |

# Optional Enhancing Widgets

| Widget               | Why It Helps                               |
| -------------------- | ------------------------------------------ |
| **SnackBar**         | Show fun feedback like “You hit the wall!” |
| **AlertDialog**      | Pop-ups for warnings or events             |
| **Dropdown**         | Choose skins or character sizes            |
| **Tabs**             | Create a simple in-app menu system         |
| **AnimatedSwitcher** | Smooth transitions between elements        |
