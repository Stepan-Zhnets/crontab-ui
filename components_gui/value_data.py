import flet as ft

minute = ft.TextField(
    label="Minute",
    # hint_text=" * ",
    value="*",
    max_length=5,
)

hour = ft.TextField(
    label="Hour",
    # hint_text=" * ",
    value="*",
    max_length=5,
)

day = ft.TextField(
    label="Day",
    # hint_text=" * ",
    value="*",
    max_length=5,
)

month = ft.TextField(
    label="Month",
    # hint_text=" * ",
    value="*",
    max_length=5,
)

week = ft.TextField(
    label="Week",
    # hint_text=" * ",
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
    # ft.TextButton("Set", on_click=None)
]

def default_data_text_field(default_data:str) -> str:
    d_min, d_h, d_d, d_mon, d_w = default_data.split()

    d_minute = ft.TextField(
        label="Minute",
        value=d_min,
        max_length=5,
    )

    d_hour = ft.TextField(
        label="Hour",
        value=d_h,
        max_length=5,
    )

    d_day = ft.TextField(
        label="Day",
        value=d_d,
        max_length=5,
    )

    d_month = ft.TextField(
        label="Month",
        value=d_mon,
        max_length=5,
    )

    d_week = ft.TextField(
        label="Week",
        value=d_w,
        max_length=5,
    )

    ddtf = [
        ft.Container(
            width=80,
            content=d_minute
        ),
        ft.Container(
            width=80,
            content=d_hour
        ),
        ft.Container(
            width=80,
            content=d_day
        ),
        ft.Container(
            width=80,
            content=d_month
        ),
        ft.Container(
            width=80,
            content=d_week
        ),
        # ft.TextButton("Set", on_click=None)
    ]
    return ddtf
