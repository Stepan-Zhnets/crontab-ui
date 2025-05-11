import flet as ft
from cron_tools import create_job, check_job
from components_gui import (
    data_text_field,
    minute, hour, day, month, week,
)

name_job = ft.TextField(label="Name")
command_job = ft.TextField(label="Command")

def open_create_new_job(page: ft.Page):
    def handle_close(e):
        page.close(create_new_job)

    def create(e):
        data_job = f"{minute.value} {hour.value} {day.value} {month.value} {week.value}"
        if check_job(name=name_job.value):
            ...
        else:
            create_job(name=name_job.value, date=data_job, command=command_job.value)
            print(f'{name_job.value}, {command_job.value}, {data_job}')
            page.close(create_new_job)

    create_new_job = ft.AlertDialog(
            modal=True,
            title=ft.Text("Create new job"),
            actions=[
                ft.AutofillGroup(
                    ft.Column(
                        controls=[
                            name_job,
                            command_job,
                            # ft.Text("Quick Schedule"),
                            # ft.Row(
                            #         controls=time_button
                            #     ),
                            ft.Text("Time"),
                            ft.Row(
                                    controls=data_text_field
                                ),
                            # ft.TextField(
                            #     label="Job"
                            # ),
                        ]
                    )
                ),
                # ft.Checkbox(label="Enable error logging"),
                ft.Divider(height=30, thickness=3),
                ft.Row(
                    controls =[
                        ft.TextButton("Cancel", on_click=handle_close),
                        ft.TextButton("Save", on_click=create),
                    ],
                ),
            ]
        )
    page.open(create_new_job)

