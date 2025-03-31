import flet as ft

def button_update_page(page: ft.Page):
    frame = ft.Row(spacing=10)

    def update_page(e):
        page.update()

    btn_update_page = ft.Button(text="update page", on_click=update_page)

    frame.controls.append(btn_update_page)
    page.add(frame)
