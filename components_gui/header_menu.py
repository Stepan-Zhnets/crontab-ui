import flet as ft

def show_create_job_dialog():...

def header_menu(page: ft.Page):
    frame = ft.Row(spacing=10)

    btn_new_job = ft.ElevatedButton(
        text="new job",
        on_click=lambda e: show_create_job_dialog(e, page)
    )

    frame.controls.append(btn_new_job)
    page.add(frame)
