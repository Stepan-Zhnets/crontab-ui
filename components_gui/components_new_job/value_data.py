import flet as ft

minute = ft.TextField(
    label="Minute",
    hint_text=" * ",
    value="*",
    max_length=5,
)

hour = ft.TextField(
    label="Hour",
    hint_text=" * ",
    value="*",
    max_length=5,
)

day = ft.TextField(
    label="Day",
    hint_text=" * ",
    value="*",
    max_length=5,
)

month = ft.TextField(
    label="Month",
    hint_text=" * ",
    value="*",
    max_length=5,
)

week = ft.TextField(
    label="Week",
    hint_text=" * ",
    value="*",
    max_length=5,
)

data_text_field = [
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
    ),
    ft.TextButton("Set", on_click=None)
]
