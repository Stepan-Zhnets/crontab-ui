import flet as ft
# from cron_tools import create_job
from components_gui.components_new_job.value_data import (
    data_text_field,
    minute, hour, day, month, week,
)

time_button = [
    ft.TextButton("Startup", on_click=None),
    ft.TextButton("Hourly", on_click=None),
    ft.TextButton("Daily", on_click=None),
    ft.TextButton("Weekly", on_click=None),
    ft.TextButton("Monthly", on_click=None),
    ft.TextButton("Yearly", on_click=None),
]

name_job = ft.TextField(label="Name")
command_job = ft.TextField(label="Command")

def header_menu(page: ft.Page):
    frame = ft.Row(spacing=10)

    def handle_close(e):
        page.close(create_new_job)

    def create(e):
        data_job = f"{minute.value}, {hour.value}, {day.value}, {month.value}, {week.value}"
        # create_job(name=None, date=None, command=None)
        print(f'{name_job.value}, {command_job.value}, {data_job}')
        page.close(create_new_job)

    # Всплывающее окно
    create_new_job = ft.AlertDialog(
            modal=True,
            title=ft.Text("Create new job"),
            actions=[
                ft.AutofillGroup(
                    ft.Column(
                        controls=[
                            # Имя задачи
                            name_job,
                            # Команда задачи
                            command_job,
                            ft.Text("Quick Schedule"),
                            ft.Row(
                                    controls=time_button
                                ),

                            ft.Text("Time"),
                            ft.Row(
                                    controls=data_text_field
                                ),
                            ft.TextField(
                                label="Job"
                            ),
                        ]
                    )
                ),
                ft.Checkbox(label="Enable error logging"),
                ft.Row(
                    controls =[
                        ft.TextButton("Cancel", on_click=handle_close),
                        ft.TextButton("Save", on_click=create),
                    ],
                ),
            ]
        )

    btn_new_job = ft.ElevatedButton(
        text="new job",
        on_click=lambda e: page.open(create_new_job)
    )

    frame.controls.append(btn_new_job)
    page.add(frame)
