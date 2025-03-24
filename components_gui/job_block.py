from tkinter import ttk
from cron_tools import delete_job

def job_block(frame_name,
                name_job, command_job, row_job,
                status, change, 
            ):
    '''Button job - job'''
    btn_job = ttk.Button(frame_name,
                        text=name_job,
                        command=command_job
                        )
    btn_job.grid(row=row_job, column=0,
                # ipadx=6, ipady=6,
                padx=1, pady=5)

    '''Date for job completion'''
    list_box_command = ttk.Label(frame_name,
                                text=command_job, font=("Arial", 10))
    list_box_command.grid(row=row_job, column=2,
                ipadx=0.1, ipady=0.1,
                padx=1, pady=5)

    '''Button job - status'''
    btn_job_status = ttk.Button(frame_name,
                        text=status,
                        command=change
                        )
    btn_job_status.grid(row=row_job, column=3,
                # ipadx=1, ipady=5,
                padx=1, pady=5)

    '''Button job - delete'''
    btn_job_delete = ttk.Button(frame_name,
                        text="delete",
                        command=delete_job(name=name_job)
                        )
    btn_job_delete.grid(row=row_job, column=4,
                # ipadx=1, ipady=5,
                padx=1, pady=5)

    '''Button job - logs'''
    btn_job_logs = ttk.Button(frame_name,
                        text="logs",
                        command=None
                        )
    btn_job_logs.grid(row=row_job, column=5,
                # ipadx=1, ipady=5,
                padx=1, pady=5)