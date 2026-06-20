import flet as ft
from enum import Enum
import threading
import time
import queue
import asyncio


class MovementDirection(str, Enum):
    """game character possible movement directions"""

    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
    IDLE = "idle"


def main(page: ft.Page):
    game_icon_size = 40
    # starting speed
    speed = 5
    speed_label = ft.Text(f"Speed: {speed}")
    cory_width = 58
    cory_height = 79
    cory = ft.Container(
        content=ft.Image(src="cory_front.png", width=cory_width, height=cory_height),
        left=200,
        top=170,
    )

    background = ft.Container(
        content=ft.Image(src="background.gif", width=page.width, height=500),
        width=page.width,
        height=400,
    )
    game_area = ft.Stack(
        controls=[background, cory],
        expand=True,
        height=400,
    )

    state: dict[str, any] = {"speed": speed, "direction": MovementDirection.IDLE}

    def handle_movement(direction: MovementDirection) -> None:
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

    def on_speed_change(e):
        state["speed"] = int(e.control.value)
        speed_label.value = f"Speed: {state['speed']}"
        page.update()

    speed_slider = ft.Slider(
        min=2,
        max=20,
        divisions=18,
        value=speed,
        label="{value}",
        on_change=on_speed_change,
    )

    movement_status = ft.Text("Stay in bounds")

    def move_left():
        if cory.left - state["speed"] >= 0 + 30:
            cory.left -= state["speed"]
            movement_status.value = "moving left"
        else:
            movement_status.value = "hit left boundary"

    def move_right():
        if cory.left + state["speed"] <= background.width - cory_width - 60:
            cory.left += state["speed"]
            movement_status.value = "moving right"
        else:
            movement_status.value = "hit right boundary"

    def move_up():
        if cory.top - state["speed"] >= 0:
            movement_status.value = "moving up"
            cory.top -= state["speed"]
        else:
            movement_status.value = "hit top boundary"

    def move_down():
        if cory.top + state["speed"] <= game_area.height - cory_height:
            movement_status.value = "moving down"
            cory.top += state["speed"]
        else:
            movement_status.value = "hit bottom boundary"

    left_button = ft.IconButton(
        icon=ft.Icons.ARROW_LEFT,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction": MovementDirection.LEFT}),
        bgcolor="green",
    )
    right_button = ft.IconButton(
        icon=ft.Icons.ARROW_RIGHT,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction": MovementDirection.RIGHT}),
        bgcolor="green",
    )
    up_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_UP,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction": MovementDirection.UP}),
        bgcolor="green",
    )
    down_button = ft.IconButton(
        icon=ft.Icons.ARROW_DROP_DOWN,
        icon_size=game_icon_size,
        on_click=lambda e: state.update({"direction": MovementDirection.DOWN}),
        bgcolor="green",
    )
    game_controller = ft.Row(
        [left_button, right_button, up_button, down_button],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    update_queue = queue.Queue()

    def game_loop():
        while True:
            handle_movement(state["direction"])
            update_queue.put("update")
            time.sleep(0.1)

    thread = threading.Thread(target=game_loop, daemon=True)
    thread.start()

    async def check_update():
        while True:
            try:
                update_queue.get_nowait()
                page.update()
            except queue.Empty:
                pass

            await asyncio.sleep(0.1)

    page.run_task(check_update)

    page.add(
        game_controller,
        ft.Row(
            [
                speed_label,
                speed_slider,
                movement_status,
            ]
        ),
        game_area,
    )


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
