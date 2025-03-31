import flet as ft
from components_gui.create_job import button_create_new_job
from cron_tools import delete_job, get_jobs

# Данные из CronTab
list_jobs = get_jobs()

def create_data_table(list_jobs):
    # Заголовки таблицы
    columns = [
        ft.DataColumn(ft.Text("#")),
        ft.DataColumn(ft.Text("Name")),
        ft.DataColumn(ft.Text("Command")),
        ft.DataColumn(ft.Text("Status")),
        ft.DataColumn(ft.Text("Actions"))
    ]

    def delete(page, value):
        delete_job(name=value)
        # Перезагружаем таблицу с актуальными данными
        list_jobs = get_jobs()
        data_table = create_data_table(list_jobs)
        page.clean()  # Очищаем страницу
        main(page)    # Перерисовываем главную страницу

    num = 0
    rows = []
    for job in list_jobs:
        num += 1
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
                    # bgcolor=ft.Colors.RED_500,
                    on_click=lambda e, job=job, value=job['name']: delete(job, value)
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

    return ft.DataTable(columns=columns, rows=rows)

def main(page: ft.Page):
    page.title = "crontab ui"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    button_create_new_job(page)

    # Создаем таблицу на основе текущих данных
    data_table = create_data_table(list_jobs)

    page.add(
        ft.Container(content=data_table, padding=ft.padding.only(left=10, right=10))
    )

ft.app(target=main)
