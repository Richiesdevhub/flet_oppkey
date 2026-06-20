import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800

    def create_cory():
        return ft.Image("cory_front.png", width=58, height=79)

    def icon_test():
        return ft.IconButton(
            icon=ft.Icons.ACCESS_ALARM,
            icon_size=100,
            bgcolor="green",
            icon_color="white"
        )

    corys = [icon_test() for _ in range(5)]

    cory = ft.Container(
        content=ft.Image(src="cory_front.png", width=58, height=79),
        left=0,
        top=50
    )

    game_area = ft.Stack(
        controls=[cory],
        width=ft.Window.width,
        height=300
    )

    # page.add(ft.Row(corys))
    page.add(game_area)


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
