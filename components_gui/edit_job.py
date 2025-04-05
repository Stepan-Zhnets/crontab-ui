import flet as ft
from cron_tools import update_job, check_job
from components_gui.value_data import default_data_text_field

def button_edit_job(page: ft.Page, default_name, default_data, default_command):
    # Frame for the dialog content
    frame = ft.Column(spacing=10)

    name_job = ft.TextField(label="Name", value=default_name)
    command_job = ft.TextField(label="Command", value=default_command)

    # Parse default data into individual cron components
    d_min, d_h, d_d, d_mon, d_w = default_data.split()

    minute = ft.TextField(
        label="Minute",
        value=d_min,
        max_length=5,
    )

    hour = ft.TextField(
        label="Hour",
        value=d_h,
        max_length=5,
    )

    day = ft.TextField(
        label="Day",
        value=d_d,
        max_length=5,
    )

    month = ft.TextField(
        label="Month",
        value=d_mon,
        max_length=5,
    )

    week = ft.TextField(
        label="Week",
        value=d_w,
        max_length=5,
    )

    cron_fields = [
        ft.Container(
            width=80,
            content=minute
        ),
        ft.Container(
            width=80,
            content=hour
        ),
        ft.Container(
            width=80,
            content=day
        ),
        ft.Container(
            width=80,
            content=month
        ),
        ft.Container(
            width=80,
            content=week
        )
    ]

    # Function to handle closing the dialog
    def handle_close(e):
        page.dialog = None
        page.update()

    # Function to save changes and close the dialog
    def create(e):
        new_data = f"{minute.value} {hour.value} {day.value} {month.value} {week.value}"

        if check_job(name=name_job.value):
            update_job(name=default_name, new_name=name_job.value, new_command=command_job.value, new_date=new_data)
            print(f'Updated job: {name_job.value}, {command_job.value}, {new_data}')
        else:
            print("Job does not exist")

        handle_close(e)

    # Create the dialog
    create_new_job = ft.AlertDialog(
        modal=True,
        title=ft.Text("Edit a Job"),
        content=frame,
        actions=[
            name_job,
            command_job,
            ft.Row(cron_fields),
            ft.Row([
                ft.TextButton("Cancel", on_click=handle_close),
                ft.TextButton("Save", on_click=create)
            ])
        ]
    )

    # Show the dialog
    page.dialog = create_new_job
    create_new_job.open = True
    page.update()
