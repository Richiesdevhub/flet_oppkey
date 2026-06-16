import flet as ft


def create_cory() -> ft.Image:
    return ft.Image("cory_front.png", width=58, height=79)


def main(page: ft.Page) -> None:
    corys = [create_cory() for _ in range(5)]
    # remove bgcolor to remove blue background
    corys.insert(0, ft.Container(width=100, height=200, bgcolor="blue"))
    # for i in range(5):
    #     corys.append(create_cory())
    page.add(ft.Row(corys))


ft.run(main, assets_dir="assets")
