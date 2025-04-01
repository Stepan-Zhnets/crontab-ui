import flet as ft
from components_gui.create_job import button_create_new_job
from cron_tools import delete_job#, get_jobs

# Условные данные
list_jobs = [
    {
        "name": "Job 1",
        "command": "Command 1",
        "status":"stopped"
    },
    {
        "name": "Job 2",
        "command": "Command 2",
        "status":"started"
    },
    {
        "name": "Job 3",
        "command": "Command 3",
        "status":"stop"
    }
]

# Данные из CronTab
# list_jobs = get_jobs()

def delete_and_refresh(page, job_name):
    delete_job(name=job_name)
    page.update()

# Главная страница
def main(page: ft.Page):
    page.title = "crontab ui"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    button_create_new_job(page)

    # Заголовки таблицы
    columns = [
        ft.DataColumn(ft.Text("#")),
        ft.DataColumn(ft.Text("Name")),
        ft.DataColumn(ft.Text("Command")),
        ft.DataColumn(ft.Text("Status")),
        ft.DataColumn(ft.Text("Actions"))
    ]

    def delete(value):
        delete_job(name=value)
        # Обновление страницы
        page.controls.append(data_table)
        page.update()

    num=0
    rows = []
    for job in list_jobs:
        num+=1
        actions = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    on_click=lambda e, job=job: print(f"Logs for {job['name']}")
                ),
                ft.IconButton(
                    icon=ft.icons.INFO,
                    on_click=lambda e, job=job: print(f"Logs for {job['name']}")
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    on_click=lambda e, job=job: delete(value=job['name'])
                ),
            ]
        )

        rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(num)),
                ft.DataCell(ft.Text(job["name"])),
                ft.DataCell(ft.Text(job["command"])),
                ft.DataCell(ft.TextButton(job["status"])),
                ft.DataCell(actions)
            ]
        ))
    data_table = ft.DataTable(columns=columns, rows=rows)

    page.add(
        ft.Container(content=data_table, padding=ft.padding.only(left=10, right=10))
    )

ft.app(target=main)
