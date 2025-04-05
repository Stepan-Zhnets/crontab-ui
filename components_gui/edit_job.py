import flet as ft
from cron_tools import update_job, check_job
from components_gui.value_data import (
    data_text_field,
    minute, hour, day, month, week,
)

def button_edit_job(page: ft.Page, default_name, default_command, default_cron):
    # frame = ft.Row(spacing=10)

    # Setting pre-filled values for the text fields
    name_job = ft.TextField(label="Name", value=default_name)
    command_job = ft.TextField(label="Command", value=default_command)

    minute.value, hour.value, day.value, month.value, week.value = default_cron.split()

    # Закрытие окна
    def handle_close(e):
        page.close(edit_new_job)

    # Обновление задачи и закрытие окна
    def update(e):
        data_job = f"{minute.value} {hour.value} {day.value} {month.value} {week.value}"
        # Check if job with the same name already exists (except for the current job)
        if check_job(name=name_job.value) and name_job.value != default_name:
            ...
        else:
            update_job(name=default_name, new_name=name_job.value, new_command=command_job.value, new_date=data_job)
            print(f'{name_job.value}, {command_job.value}, {data_job}')
            page.close(edit_new_job)

    # Всплывающее окно
    edit_new_job = ft.AlertDialog(
        modal=True,
        title=ft.Text("Edit Job"),
        actions=[
            ft.AutofillGroup(
                ft.Column(
                    controls=[
                        name_job,
                        command_job,

                        ft.Text("Time"),
                        ft.Row(
                            controls=data_text_field
                        ),
                    ]
                )
            ),
            ft.Row(
                controls=[
                    ft.TextButton("Cancel", on_click=handle_close),
                    ft.TextButton("Update", on_click=update),
                ],
            ),
        ]
    )

    # Кнопка, вызывающая всплывающееся окно
    # btn_edit_job = ft.ElevatedButton(
    #     text="Edit job",
    #     on_click=lambda e: page.open(edit_new_job)
    # )

    # frame.controls.append(btn_edit_job)
    # page.add(frame)

