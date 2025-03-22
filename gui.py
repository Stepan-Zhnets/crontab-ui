import tkinter as tk
from tkinter import ttk
# from cron import check_job, create_job, delete_job

from widgets import print_info

list_jobs = [
    {
        "name_jobs": "Job 1",
        "command_jobs": "Command 1",
        "status":"stop"
    },
    {
        "name_jobs": "Job 2",
        "command_jobs": "Command 2",
        "status":"stop"
    },
    {
        "name_jobs": "Job 3",
        "command_jobs": "Command 3",
        "status":"stop"
    }
]
 
root = tk.Tk()

root.title('crontab ui')
root.geometry("1000x400")

# Component

# Button
# btn = ttk.Button()
# btn.pack(anchor="nw",
#         padx=20, pady=30
#     )
# btn.config(text="create job")

for index, job in enumerate(list_jobs):
    btn = ttk.Button(
        text=job['name_jobs'],
        command=lambda j=job['command_jobs']: print(j)
        )
    btn.pack(anchor="nw",
        padx=20, pady=10#(10 if index else 30)
        )

    btn_s = ttk.Button(
        text=job['status']
    )
    btn_s.pack(anchor="nw",
        padx=0, pady=0)

# widgets-info
root.update()
print_info(root)

# Start
root.mainloop()


