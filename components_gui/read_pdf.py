import flet as ft
import os

files = {
    "Main list": "./manual/📍_Main_list.pdf",
    "Create-Edit job": "./manual/📝_Create-Edit_job.pdf",
    "Main panel": "./manual/📰_Main_panel.pdf"
}

def open_file(path):
    if os.name == 'nt':
        # Windows
        os.system(f"start {path}")
    else:
        # POSIX (Linux, macOS)
        os.system(f"open {path}")

def open_manual_list(page: ft.Page):
    # Закрытие окна
    def handle_close(e):
        page.close(manual_page)

    buttons = [
        ft.TextButton(text=name, on_click=lambda e, p=path: open_file(p))
        for name, path in files.items()
    ]

    manual_page = ft.AlertDialog(
        title=ft.Text("Manuals"),
        # content=ft.Column(buttons),
        actions=[
            ft.Column(buttons),
            ft.Divider(height=9, thickness=3),
            ft.TextButton("Cancel", on_click=handle_close),
        ]
    )

    page.open(manual_page)
