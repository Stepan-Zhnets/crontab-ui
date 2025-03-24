import tkinter as tk
from tkinter import ttk

from cron_tools import create_job

def menu_create_job():
    window = tk.Tk()

    window.title('create job')
    window.geometry("400x300")
    window.minsize(400,300)
    window.maxsize(400,300)

    '''Entry name job'''

    '''Entry date job'''

    '''Entry command job'''

    '''Entry name job'''

    ''' Button create job '''
    button_create = ttk.Button(window,
        text="Create",
        command=create_job
        )
    button_create.grid(
        sticky="se",
        padx=1, pady=1
        )
    button_create.pack(anchor="se")
    window.mainloop()