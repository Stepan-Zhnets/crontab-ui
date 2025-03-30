import flet as ft
from components_gui.header_menu import header_menu
from cron_tools import delete_job

# Данные из CronTab
list_jobs = [
    {
        "name": "Job 1",
        "command": "Command 1 Command 1 Command 1",
        "status":"stop"
    },
    {
        "name": "Job 2",
        "command": "Command 2",
        "status":"stop"
    },
    {
        "name": "Job 3",
        "command": "Command 3",
        "status":"stop"
    }
]

# list_jobs = get_jobs()

# Главная страница
def main(page: ft.Page):
    page.title = "crontab ui"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    header_menu(page)

    # Заголовки таблицы
    columns = [
        ft.DataColumn(ft.Text("Name")),
        ft.DataColumn(ft.Text("Command")),
        ft.DataColumn(ft.Text("Status")),
        ft.DataColumn(ft.Text("Actions"))
    ]

    rows = []
    for job in list_jobs:
        actions = ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.INFO, on_click=lambda e, job=job: print(f"Logs for {job['name']}")),
                ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, job=job: delete_job(name=job['name'])),
            ]
        )

        rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(job["name"])),
                ft.DataCell(ft.Text(job["command"])),
                ft.DataCell(ft.Text(job["status"])),
                ft.DataCell(actions)
            ]
        ))

    data_table = ft.DataTable(columns=columns, rows=rows)

    page.add(
        ft.Container(content=data_table, padding=ft.padding.only(left=10, right=10))
    )

ft.app(target=main)

