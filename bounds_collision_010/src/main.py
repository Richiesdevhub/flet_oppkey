import flet as ft
from rich import color_triplet


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    game_icon_size = 50
    # Starting speed
    speed = 5
    speed_label = ft.Text(f"Speed: {speed}", color="white")
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

    state={"speed":speed, }

    def on_speed_change(e):
        state["speed"] = int(e.control.value)
        speed_label.value=f"Speed: {state['speed']}"
        page.update()

    speed_slider = ft.Slider(min=2, max=12, divisions=10, value=speed,
                             label="{value}", on_change=on_speed_change)

    def move_left():
        print("Moving left")
        cory.left -= state["speed"]

    def move_right():
        print("Moving right")
        cory.left += state["speed"]

    def move_up():
        print("Moving up")
        cory.top -= state["speed"]

    def move_down():
        print("Moving down")
        cory.top += state["speed"]

    left_button = ft.IconButton(
        icon=ft.Icons.ARROW_LEFT,
        icon_size=game_icon_size,
        on_click=move_left,
        bgcolor="green",
        icon_color="white"
    )

    right_button = ft.IconButton(
        icon=ft.Icons.ARROW_RIGHT,
        icon_size=game_icon_size,
        on_click=move_right,
        bgcolor="green",
        icon_color="white"
    )

    up_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_UP,
        icon_size=game_icon_size,
        on_click=move_up,
        bgcolor="green",
        icon_color="white"
    )

    down_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_DOWN,
        icon_size=game_icon_size,
        on_click=move_down,
        bgcolor="green",
        icon_color="white"
    )

    game_controller = ft.Row(
        controls=[left_button, right_button, up_button, down_button],
        alignment=ft.MainAxisAlignment.START
    )

    page.add(game_controller,
             ft.Row([speed_label, speed_slider]),
             game_area)


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
