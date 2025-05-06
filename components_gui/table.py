import flet as ft
from components_gui.create_job import open_create_new_job
from components_gui.edit_job import button_edit_job
from components_gui.read_pdf import open_manual_list
from cron_tools import delete_job, start_and_stop_job#, get_jobs

# Условные данные
list_jobs = []

def update_table(page):
    # Данные из CronTab
    # list_jobs = get_jobs()

    def status_switch_button(e, name):
        e.control.selected = not e.control.selected
        new_status = "enabled" if e.control.selected else "disabled"
        start_and_stop_job(name, new_status)

        # Update the job's status in list_jobs
        for job in list_jobs:
            if job['name'] == name:
                job['status'] = new_status
                break

        print(f"Job {name} was set to {new_status}")
        e.control.update()
        update_table(page)

    # Заголовки таблицы
    columns = [
        ft.DataColumn(ft.Text("#")),
        ft.DataColumn(ft.Text("Name")),
        ft.DataColumn(ft.Text("Command")),
        ft.DataColumn(ft.Text("Time")),
        ft.DataColumn(ft.Text("Status")),
        ft.DataColumn(ft.Text("Actions"))
    ]

    def delete(value):
        delete_job(value)
        # Обновление страницы
        update_table(page)

    num=0
    rows = []
    for job in list_jobs:
        num+=1
        selected_status = job['status'].lower() == 'enabled'
        actions = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.PLAY_CIRCLE,
                    selected_icon=ft.Icons.STOP_CIRCLE,
                    on_click=lambda e, name=job['name']: status_switch_button(e, name),
                    selected=not selected_status,
                    style=ft.ButtonStyle(color={
                        "selected": ft.Colors.ORANGE_300,
                        "": ft.Colors.GREEN_300
                    }),
                ),
                ft.IconButton(
                    icon=ft.Icons.EDIT,
                    on_click=lambda e, job=job: button_edit_job(
                        page,
                        default_name=job["name"],
                        default_command=job["command"],
                        default_cron=job["cron"]
                    ),
                    style=ft.ButtonStyle(color={"": ft.Colors.BLUE_300}),
                ),

                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    on_click=lambda e, job=job: delete(value=job['name']),
                    style=ft.ButtonStyle(color={"": ft.Colors.RED_300}),
                ),
            ]
        )

        rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(num)),
                ft.DataCell(ft.Text(job["name"])),
                ft.DataCell(ft.Text(job["command"])),
                ft.DataCell(ft.Text(job["cron"])),
                ft.DataCell(ft.Text("enabled" if selected_status else "disabled")),
                ft.DataCell(actions)
            ]
        ))
    data_table = ft.DataTable(columns=columns, rows=rows)

    # Очищаем предыдущую таблицу и добавляем новую
    page.clean()
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextButton(
                    text="new job",
                    on_click=lambda e: open_create_new_job(page)
                ),
                ft.TextButton(
                    text="manual",
                    on_click=lambda e: open_manual_list(page)
                ),
                ft.TextButton(
                    text="update page",
                    on_click=lambda e: update_table(page)
                ),
            ]
        ),
        ft.Container(
            content=data_table,
            padding=ft.padding.only(left=10, right=10)
        ),
    )
