from tkinter import ttk

from components_gui.windows.create_job import menu_create_job


def header_menu():
    frame = ttk.Frame(borderwidth=1,
                        relief='solid',
                        padding=[2, 1]
                    )


    btn_new_job = ttk.Button(frame,
                            text="new job",
                            command=menu_create_job
                            )
    btn_new_job.grid(
        # ipadx=3, ipady=2,
        padx=1, pady=1
        )

    frame.grid(
        padx=1, pady=1
        )