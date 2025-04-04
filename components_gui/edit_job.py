import flet as ft
from cron_tools import create_job, check_job
from components_gui.value_data import (
    default_data_text_field,
    # minute, hour, day, month, week,
)

def button_edit_job(page: ft.Page, default_name, default_data, default_command):
    frame = ft.Row(spacing=10)

    name_job = ft.TextField(label="Name", value=default_name)
    command_job = ft.TextField(label="Command", value=default_command)

    # Закрытие окна
    def handle_close(e):
        page.close(create_new_job)

    # Создание задачи и закрытие окна
    def create(e):
        # data_job = f"{minute.value} {hour.value} {day.value} {month.value} {week.value}"
        if check_job(name=name_job.value):
            ...
        else:
            create_job(name=name_job.value, date=default_data, command=command_job.value)
            print(f'{name_job.value}, {command_job.value}, {default_data}')
            page.close(create_new_job)

    # Всплывающее окно
    create_new_job = ft.AlertDialog(
            modal=True,
            title=ft.Text("Edit a job"),
            actions=[
                ft.AutofillGroup(
                    ft.Column(
                        controls=[
                            # Имя задачи
                            name_job,
                            # Команда задачи
                            command_job,
                            # ft.Text("Quick Schedule"),
                            # ft.Row(
                            #         controls=time_button
                            #     ),

                            ft.Text("Time"),
                            ft.Row(
                                    controls=default_data_text_field(default_data)
                                ),
                            # ft.TextField(
                            #     label="Job"
                            # ),
                        ]
                    )
                ),
                # ft.Checkbox(label="Enable error logging"),
                ft.Row(
                    controls =[
                        ft.TextButton("Cancel", on_click=handle_close),
                        ft.TextButton("Save", on_click=create),
                    ],
                ),
            ]
        )

    page.add(frame)
