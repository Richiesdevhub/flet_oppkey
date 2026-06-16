# Video Tutorial Outline: OOP Concepts Using Flet Actor Class

## 1. Introduction & Demo (0:00–1:30)

- Show final running app:
  - Character image displayed on screen.
  - Printed attributes (name, strength, health).
- Explain purpose:
  - Build a simple Flet program.
  - Use Object-Oriented Programming to model a game character.
- Learning goals:
  - Understand **Abstraction**, **Encapsulation**, **Inheritance**, **Polymorphism** using this code example.

---

## 2. Mental Model of OOP (1:30–4:00)

- Real-world analogy: game characters.
  - Characters have **data** → name, strength, health.
  - Characters have **behavior** → attack, heal, take damage.
- Classes vs. Objects:
  - A **class** is a blueprint.
  - An **object** is an instance built from the blueprint.
- Connect to code:
  - `Actor` is the class.
  - `cory` is the object.

---

## 3. Encapsulation with the Actor Class (4:00–8:00)

### 3.1 Reading the class definition

```python
class Actor(ft.Image):
    strength: int
    health: int
    name: str
```
