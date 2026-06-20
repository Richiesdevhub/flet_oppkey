import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800

    def create_cory():
        return ft.Image("cory_front.png", width=58, height=79)

    corys = [create_cory() for _ in range(5)]

    page.add(ft.Row(corys))

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
