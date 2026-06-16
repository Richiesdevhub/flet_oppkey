---
marp: true
theme: default
class: lead
---

# OOP Recap & Next Steps

## 🔄 OOP Recap (Applied to the Actor Code)

- **Encapsulation**  
  Actor stores `name`, `strength`, and `health` inside the object.  
  Data is grouped and accessed through the object (`cory.name`, etc.).

- **Inheritance**  
  `Actor(ft.Image)` reuses all image-loading and rendering behavior from Flet.  
  Actor _is an Image_, so it can be used anywhere an Image is expected.

- **Abstraction**  
  `create_actor()` hides implementation details (sprite file, size).  
  `Actor` hides how images load internally — you just pass values.

- **Polymorphism**  
  Since Actor is a subclass of Image, `page.add(actor)` works without modification.  
  Future subclasses (`Enemy`, `Healer`) could behave differently but use the same interface.

---

## 🚀 Next Steps

- Add methods like `take_damage(amount)`, `heal(amount)`, `attack(target)`  
  → Strengthen encapsulation and introduce behavior.

- Create subclasses:

  - `Enemy(Actor)`
  - `Hero(Actor)`  
    → Demonstrate polymorphism through overridden methods.

- Add a game loop where each actor runs `take_turn()`  
  → Shows polymorphism in action: each class can implement the method differently.

- Animate or move actors using Flet controls  
  → Connect OOP concepts to more dynamic UI/game behavior.
