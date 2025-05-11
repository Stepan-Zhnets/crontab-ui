import flet as ft
from cron_tools import update_job, check_job
from components_gui import (
    data_text_field,
    minute, hour, day, month, week,
)

def button_edit_job(page: ft.Page, default_name=None, default_command=None, default_cron=None):
    def handle_close(e):
        page.close(edit_new_job)

    def update(e):
        data_job = f"{minute.value} {hour.value} {day.value} {month.value} {week.value}"
        if check_job(name=default_name):
            update_job(name=default_name, new_command=command_job.value, new_date=data_job)
            print(f'{default_name}, {command_job.value}, {data_job}')
            page.close(edit_new_job)

    if default_cron:
        cron_parts = default_cron.split()
        minute.value = cron_parts[0]
        hour.value = cron_parts[1]
        day.value = cron_parts[2]
        month.value = cron_parts[3]
        week.value = cron_parts[4]

    edit_new_job = ft.AlertDialog(
            modal=True,
            title=ft.Text("Edit job"),
            actions=[
                ft.AutofillGroup(
                    ft.Column(
                        controls=[
                            ft.TextField(label="Name", value=default_name+" *", read_only=True),
                            command_job := ft.TextField(label="Command", value=default_command or ""),
                            ft.Text("Time"),
                            ft.Row(
                                controls=data_text_field
                            ),
                        ]
                    )
                ),
                ft.TextField(
                    label=f"{None}"
                ),
                ft.Divider(height=30, thickness=3),
                ft.Row(
                    controls =[
                        ft.TextButton("Cancel", on_click=handle_close),
                        ft.TextButton("Save", on_click=update),
                    ],
                ),
            ]
        )

    page.open(edit_new_job)
