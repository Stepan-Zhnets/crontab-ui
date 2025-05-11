import flet as ft
from components_gui import update_table

# Главная страница
def main(page: ft.Page):
    page.title = "crontab ui"
    page.window.min_height=500
    page.window.min_width=800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # Инициализируем таблицу
    update_table(page)

if __name__ == "__main__":
    ft.app(target=main)
