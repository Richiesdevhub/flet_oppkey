#En este capitulo solo explica punto por punto como se hicieron los loops.
import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800

    def create_cory():
        return ft.Image("cory_front.png", width=58, height=79)

    def create_image(seed)->ft.Image:
        return ft.Image(src=f'https://picsum.photos/seed/{seed}/80/80')

    def icon_test():
        return ft.IconButton(
            icon=ft.Icons.ACCESS_ALARM,
            icon_size=100,
            bgcolor="green",
            icon_color="white"
        )

    corys = [create_cory() for _ in range(5)]
    spacing:ft.Container =ft.Container(width=100, height=200)
    corys.insert(0, spacing)

    images = [create_image(seed*5) for seed in range(5)]
    images2 = [create_image((seed+6)*8) for seed in range(5)]

    cory = ft.Container(
        content=ft.Image(src="cory_front.png", width=58, height=79),
        left=0,
        top=50)

    game_area = ft.Stack(
        controls=[*corys],
        width=ft.Window.width,
        height=300
    )

    # page.add(ft.Row(corys))
    page.add(ft.Row(corys))
    page.add(ft.Row(images))
    page.add(ft.Row(images2))


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
