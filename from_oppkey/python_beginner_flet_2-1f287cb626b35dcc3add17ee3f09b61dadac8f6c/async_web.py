import flet as ft
from enum import Enum
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

    state: dict[str, object] = {
        "speed": speed,
        "direction": MovementDirection.IDLE,
    }

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

    def on_speed_change(e: ft.ControlEvent):
        state["speed"] = int(e.control.value)
        speed_label.value = f"Speed: {state['speed']}"
        # In Flet 1.0 alpha, auto-update helps, but explicit update is fine:
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
        speed_value = int(state["speed"])
        if cory.left - speed_value >= 0 + 30:
            cory.left -= speed_value
            movement_status.value = "moving left"
        else:
            movement_status.value = "hit left boundary"

    def move_right():
        speed_value = int(state["speed"])
        # background.width is set above from page.width
        if cory.left + speed_value <= background.width - cory_width - 60:
            cory.left += speed_value
            movement_status.value = "moving right"
        else:
            movement_status.value = "hit right boundary"

    def move_up():
        speed_value = int(state["speed"])
        if cory.top - speed_value >= 0:
            movement_status.value = "moving up"
            cory.top -= speed_value
        else:
            movement_status.value = "hit top boundary"

    def move_down():
        speed_value = int(state["speed"])
        if cory.top + speed_value <= game_area.height - cory_height:
            movement_status.value = "moving down"
            cory.top += speed_value
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

    async def game_loop():
        while True:
            handle_movement(state["direction"])
            # Explicit update after each movement tick
            page.update()
            # Non-blocking sleep works in Pyodide / async UI model
            await asyncio.sleep(0.1)

    # Start background async loop
    page.run_task(game_loop)

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
    # For local testing; assets_dir matches your existing structure.
    ft.run(main, assets_dir="assets")
