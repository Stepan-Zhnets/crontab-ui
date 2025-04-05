import flet as ft
from cron_tools import update_job, check_job
from components_gui.value_data import (
    default_data_text_field,
    d_minute, d_hour, d_day, d_month, d_week,
)

def button_edit_job(page: ft.Page, default_name, default_data, default_command):
    frame = ft.Row(spacing=10)

    name_job = ft.TextField(label="Name", value=default_name)
    command_job = ft.TextField(label="Command", value=default_command)

    # Закрытие окна
    def handle_close(e):
        # page.close(edit_job)
        page.dialog = None
        page.update()

    # Создание задачи и закрытие окна
    def create(e):
        new_data  = f"{d_minute.value} {d_hour.value} {d_day.value} {d_month.value} {d_week.value}"
        if check_job(name=name_job.value):
            update_job(name=default_name, new_name=name_job.value, new_command=command_job.value, new_date=new_data)
            print(f'Updated job: {name_job.value}, {command_job.value}, {new_data}')
        else:
            print("Job does not exist")

        handle_close(e)

    # Всплывающее окно
    edit_job = ft.AlertDialog(
            modal=True,
            title=ft.Text("Edit a job"),
            actions=[
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

    frame.controls.append(edit_job)
    page.add(frame)
