import flet as ft
from enum import Enum
import threading as th
import time


class MovementDirection(str, Enum):
    """game character possible movement directions"""
    LEFT = "left"
    RIGHT = "right"
    UP="up"
    DOWN="down"
    IDLE="idle"


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    game_icon_size = 50
    # Starting speed
    speed = 5
    speed_label = ft.Text(f"Speed: {speed}", color="white")

    movement_status = ft.Text("Stay in bounds", color="white")

    background = ft.Container(
        content=ft.Image(src="background.gif",
                         width=page.width,
                         height=500),
        width=ft.Window.width,
        height=ft.Window.height)

    cory_width=40
    cory_height=60

    cory = ft.Container(
        content=ft.Image(src="cory_front.png",
                        width=cory_width, height=cory_height),
                        left=20,
                        top=100
    )

    game_area = ft.Stack(
        controls=[background, cory],
        expand=True,
        height=400
    )

    state:dict[str,any]={"speed":speed, "direction": MovementDirection.IDLE}
    #El instructor menciona pydantic para manejar el estado, revisar cuando
    #sea posible

    def on_speed_change(e):
        state["speed"] = int(e.control.value)
        speed_label.value=f"Speed: {state['speed']}"
        page.update()

    speed_slider = ft.Slider(min=2, max=12, divisions=10, value=speed,
                             label="{value}", on_change=on_speed_change)

    def handle_movement(direction: MovementDirection):
        match direction:
            case MovementDirection.LEFT:
                move_left()
            case MovementDirection.RIGHT:
                move_right()
            case MovementDirection.UP:
                move_up()
            case MovementDirection.DOWN:
                move_down()
            case MovementDirection.IDLE:
                pass

    def move_left():
        if cory.left - state["speed"] >= 0:
            cory.left -= state["speed"]
            movement_status.value="moving left"
        else:
            movement_status.value="hit left boundry"

    def move_right():
        if cory.left + state["speed"] <= page.width-cory_width:
            cory.left += state["speed"]
            movement_status.value = "moving right"
        else:
            movement_status.value = "hit right boundry"

    def move_up():
        if cory.top - state["speed"] >= 0:
            cory.top -= state["speed"]
            movement_status.value = "moving up"
        else:
            movement_status.value = "hit upper boundry"


    def move_down():
        if cory.top + state["speed"] <= 300-cory_height:
            cory.top += state["speed"]
            movement_status.value = "moving down"
        else:
            movement_status.value = "hit bottom boundry"

    left_button = ft.IconButton(
        icon=ft.Icons.ARROW_LEFT,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction":MovementDirection.LEFT}),
        bgcolor="green",
        icon_color="white"
    )

    right_button = ft.IconButton(
        icon=ft.Icons.ARROW_RIGHT,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction":MovementDirection.RIGHT}),
        bgcolor="green",
        icon_color="white"
    )

    up_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_UP,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction":MovementDirection.UP}),
        bgcolor="green",
        icon_color="white"
    )

    down_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_DOWN,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction":MovementDirection.DOWN}),
        bgcolor="green",
        icon_color="white"
    )


    game_controller = ft.Row(
        controls=[left_button, right_button, up_button, down_button],
        alignment=ft.MainAxisAlignment.START
    )

    def game_loop():
        while True:
            handle_movement(state["direction"])
            time.sleep(0.1)

    thread = th.Thread(target=game_loop, daemon=True)
    thread.start()

    page.add(game_controller,
             ft.Row([speed_label, speed_slider, movement_status]),
             game_area)


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
