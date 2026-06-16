import flet as ft


class Actor(ft.Image):
    strength: int
    health: int
    name: str

    def __init__(
        self, src: str, width: int, height: int, name: str, strength: int, health: int
    ):
        super().__init__(src, width=width, height=height)
        self.name = name
        self.strength = strength
        self.health = health


def create_actor(name: str, strength: int, health: int) -> Actor:
    return Actor(
        src="cory_front.png",
        width=58,
        height=79,
        name=name,
        strength=strength,
        health=health,
    )


def main(page: ft.Page) -> None:
    cory = create_actor("Cory", 10, 100)
    page.add(cory)
    print(f"Character Name: {cory.name}")
    print(f"Strength: {cory.strength}")
    print(f"Health: {cory.health}")
    print(cory.health)
    page.add(ft.Text(f"Character Name: {cory.name}"))
    page.add(ft.Text(f"Strength: {cory.strength}"))
    page.add(ft.Text(f"Health: {cory.health}"))


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
