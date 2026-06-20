import flet as ft


def main(page: ft.Page):
    page.title = "Flet Movement Buttons"

    status_text = ft.Text("Press a button to move!")

    def move_left(e):
        status_text.value = "Moving LEFT ◀️"
        page.update()

    def move_right(e):
        status_text.value = "Moving RIGHT ▶️"
        page.update()

    def move_up(e):
        status_text.value = "Moving UP 🔼"
        page.update()

    def move_down(e):
        status_text.value = "Moving DOWN 🔽"
        page.update()

    controls_row = ft.Row(
        [
            ft.IconButton(icon=ft.icons.ARROW_LEFT, on_click=move_left),
            ft.IconButton(icon=ft.icons.ARROW_UPWARD, on_click=move_up),
            ft.IconButton(icon=ft.icons.ARROW_DOWNWARD, on_click=move_down),
            ft.IconButton(icon=ft.icons.ARROW_RIGHT, on_click=move_right),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        ft.Text("Movement Control Pad", size=24, weight=ft.FontWeight.BOLD),
        controls_row,
        status_text,
    )


if __name__ == "__main__":
    ft.app(target=main)
