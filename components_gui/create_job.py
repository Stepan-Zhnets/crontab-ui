import flet as ft
from cron_tools import create_job
from components_gui.components_new_job.value_data import (
    data_text_field,
    minute, hour, day, month, week,
)

# Mapping for special cron commands
special_commands_map = {
    "Startup": "@reboot",
    "Hourly": "@hourly",
    "Daily": "@daily",
    "Weekly": "@weekly",
    "Monthly": "@monthly",
    "Yearly": "@yearly"
}

def set_special_command(command, minute, hour, day, month, week):
    if command == "@reboot":
        # Handle @reboot separately since it is not supported directly by crontab for jobs
        raise ValueError("The '@reboot' command cannot be used directly with this function. Please set up the reboot job manually.")
    else:
        cron_expression = special_commands_map[command]
        minute.value, hour.value, day.value, month.value, week.value = cron_expression.split()

time_button = [
    ft.TextButton("Startup", on_click=lambda e: set_special_command("Startup", minute, hour, day, month, week)),
    ft.TextButton("Hourly", on_click=lambda e: set_special_command("Hourly", minute, hour, day, month, week)),
    ft.TextButton("Daily", on_click=lambda e: set_special_command("Daily", minute, hour, day, month, week)),
    ft.TextButton("Weekly", on_click=lambda e: set_special_command("Weekly", minute, hour, day, month, week)),
    ft.TextButton("Monthly", on_click=lambda e: set_special_command("Monthly", minute, hour, day, month, week)),
    ft.TextButton("Yearly", on_click=lambda e: set_special_command("Yearly", minute, hour, day, month, week)),
]

name_job = ft.TextField(label="Name")
command_job = ft.TextField(label="Command")

def header_menu(page: ft.Page):
    frame = ft.Row(spacing=10)

    def handle_close(e):
        page.close(create_new_job)
        page.update()

    def create(e):
        # Check if a special command is set
        data_job = f"{minute.value} {hour.value} {day.value} {month.value} {week.value}"
        try:
            if minute.value in special_commands_map.values():
                create_job(name=name_job.value, date=minute.value, command=command_job.value)
            else:
                create_job(name=name_job.value, date=data_job, command=command_job.value)
        except ValueError as ve:
            page.snack_bar = ft.SnackBar(content=ft.Text(str(ve)))
            page.snack_bar.open = True
            return

        print(f'{name_job.value}, {command_job.value}, {data_job}')
        page.update()
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
