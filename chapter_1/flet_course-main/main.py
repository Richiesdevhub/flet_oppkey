import flet as ft


def create_cory() -> ft.Image:
    return ft.Image("cory_front.png", width=58, height=79)


def create_image(seed: int) -> ft.Image:
    return ft.Image(f"https://picsum.photos/seed/{seed}/120/120")


def main(page: ft.Page) -> None:
    corys = [create_cory() for _ in range(5)]
    spacing: ft.Container = ft.Container(width=100, height=200)
    corys.insert(0, spacing)
    page.add(ft.Row(corys))
    images = [create_image(seed * 5) for seed in range(5)]
    images2 = [create_image((seed + 3) * 45) for seed in range(5)]

    page.add(ft.Row(images))
    page.add(ft.Row(images2))


ft.run(main, assets_dir="assets")
