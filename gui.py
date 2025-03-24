import tkinter as tk
from tkinter import ttk

from components_gui.header_menu import header_menu
from components_gui.job_block import job_block
from cron_tools import get_jobs #, create_job, delete_job

from widgets import print_info

# list_jobs = [
#     {
#         "name_jobs": "Job 1",
#         "command_jobs": "Command 1 Command 1 Command 1",
#         "status":"stop"
#     },
#     {
#         "name_jobs": "Job 2",
#         "command_jobs": "Command 2",
#         "status":"stop"
#     },
#     {
#         "name_jobs": "Job 3",
#         "command_jobs": "Command 3",
#         "status":"stop"
#     }
# ]

list_jobs = get_jobs()

root = tk.Tk()

root.title('crontab ui')
root.geometry("400x300")
root.minsize(400,300)
root.maxsize(500,400)


header_menu()

frame_list_jobs = ttk.Frame(borderwidth=1,
                            relief='solid',
                            padding=[8, 10]
                            )
for index, job in enumerate(list_jobs):

    job_block(frame_name=frame_list_jobs,
                name_job=job['name'],
                command_job=job['command'],
                row_job=index,
                status=job['status'],
                change=None)
frame_list_jobs.grid(
        padx=5, pady=5
        )

    # btn = ttk.Button(
    #     text=job['name_jobs'],
    #     command=lambda j=job['command_jobs']: print(j)
    #     )
    # btn.pack(anchor="nw",
    #     padx=20, pady=10#(10 if index else 30)
    #     )

    # btn_s = ttk.Button(
    #     text=job['status']
    # )
    # btn_s.pack(anchor="nw",
    #     padx=0, pady=0)

# widgets-info
root.update()
print_info(root)

# Start
root.mainloop()


