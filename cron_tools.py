from crontab import CronTab

user = "user"

def check_job(name):
    with CronTab(user=user) as cron:
        for job in cron:
            if job.comment == name:
                return True
    return False

def create_job(name, date, command):
    with CronTab(user=user) as cron:
        job = cron.new(command=command, comment=name)
        
        # Разбираем дату на компоненты и устанавливаем соответствующие значения для задачи
        minute, hour, day_of_month, month, day_of_week = date.split()
        job.minute.on(int(minute))
        job.hour.on(int(hour))
        job.dom.on(int(day_of_month))
        job.month.on(int(month))
        job.dow.on(int(day_of_week))

        cron.write()

def start_and_stop_job(name, status):
    with CronTab(user=user) as cron:
        for job in cron:
            if job.comment == name:
                if status.lower() == 'start':
                    # Убираем комментарий, если задача должна быть активной
                    job.enable()
                elif status.lower() == 'stop':
                    # Комментируем задачу, если она должна быть неактивной
                    job.disable()
        cron.write()

def delete_job(name):
    with CronTab(user=user) as cron:
        for job in cron:
            if job.comment == name:
                cron.remove(job)
        cron.write()

def get_jobs():
    jobs = []
    with CronTab(user=user) as cron:
        for job in cron:
            status = "enabled" if job.is_enabled() else "disabled"
            jobs.append({
                "name": job.comment,
                "command": job.command,
                "status": status
            })
    print(jobs)
    return jobs