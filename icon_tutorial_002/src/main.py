import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800

    background = ft.Container(
        content=ft.Image(src="background.gif",
                         width=ft.Window.width,
                         height=ft.Window.height),
        width=ft.Window.width,
        height=ft.Window.height)

    cory = ft.Container(
        content=ft.Image(src="cory_front.png", width=58, height=79),
        left=0,
        top=50
    )

    game_area = ft.Stack(
        controls=[background, cory],
        width=ft.Window.width,
        height=300
    )

    def move_left():
        print("Moving left")
        cory.left -= 10

    def move_right():
        print("Moving right")
        cory.left += 10

    def move_up():
        print("Moving up")
        cory.top -= 10

    def move_down():
        print("Moving down")
        cory.top += 10

    left_button = ft.IconButton(
        icon=ft.Icons.ARROW_LEFT,
        icon_size=100,
        on_click=move_left,
        bgcolor="green",
        icon_color="white"
    )

    right_button = ft.IconButton(
        icon=ft.Icons.ARROW_RIGHT,
        icon_size=100,
        on_click=move_right,
        bgcolor="green",
        icon_color="white"
    )

    up_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_UP,
        icon_size=100,
        on_click=move_up,
        bgcolor="green",
        icon_color="white"
    )

    down_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_DOWN,
        icon_size=100,
        on_click=move_down,
        bgcolor="green",
        icon_color="white"
    )

    game_controller = ft.Row(
        controls=[left_button, right_button, up_button, down_button],
        alignment=ft.MainAxisAlignment.START
    )

    page.add(game_controller, game_area)


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
