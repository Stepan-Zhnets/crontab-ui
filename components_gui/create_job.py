import flet as ft
from cron_tools import create_job, check_job
from components_gui.components_new_job.value_data import (
    data_text_field,
    minute, hour, day, month, week,
)

name_job = ft.TextField(label="Name")
command_job = ft.TextField(label="Command")

def button_create_new_job(page: ft.Page):
    frame = ft.Row(spacing=10)

    # Закрытие окна
    def handle_close(e):
        page.close(create_new_job)

    # Создание задачи и закрытие окна
    def create(e):
        data_job = f"{minute.value} {hour.value} {day.value} {month.value} {week.value}"
        # Check if job with the same name already exists
        if check_job(name=name_job.value):
            bs = ft.BottomSheet(
                # on_dismiss=handle_dismissal,
                content=ft.Container(
                    padding=50,
                    content=ft.Column(
                        tight=True,
                        controls=[
                            ft.Text("This is bottom sheet's content!"),
                            ft.ElevatedButton("Close bottom sheet", on_click=lambda _: page.close(bs)),
                        ],
                    ),
                ),
            )
            page.dialog = bs
            page.dialog.open = True
        else:
            create_job(name=name_job.value, date=data_job, command=command_job.value)
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
                ft.Row(
                    controls =[
                        ft.TextButton("Cancel", on_click=handle_close),
                        ft.TextButton("Save", on_click=create),
                    ],
                ),
            ]
        )

    # Кнопка, вызывающая всплывающееся окно
    btn_new_job = ft.ElevatedButton(
        text="new job",
        on_click=lambda e: page.open(create_new_job)
    )

    frame.controls.append(btn_new_job)
    page.add(frame)

