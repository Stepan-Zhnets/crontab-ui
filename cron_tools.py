from crontab import CronTab
import croniter
import subprocess

try:
    user = subprocess.check_output('whoami', shell=True).decode().strip()
except Exception as e:
    print(f"Failed to get the current user: {e}")
    user = "liveuser"  # Fallback to default user if an error occurs

# Mapping for special cron commands
special_commands_map = {
    "@reboot": "Reboot",
    "@hourly": "0 * * * *",
    "@daily": "0 0 * * *",
    "@weekly": "0 0 * * 0",
    "@monthly": "0 0 1 * *",
    "@yearly": "0 0 1 1 *",
    "@annually": "0 0 1 1 *",
    "@midnight": "0 0 * * *"
}

def check_job(name):
    with CronTab(user=user) as cron:
        for job in cron:
            if job.comment == name:
                return True
    return False

def create_job(name, date, command):
    with CronTab(user=user) as cron:
        job = cron.new(command=command, comment=name)

        if date in special_commands_map:
            if date == "@reboot":
                raise ValueError("The '@reboot' command cannot be used directly with this function. Please set up the reboot job manually.")
            else:
                cron_command = special_commands_map[date]
        else:
            try:
                croniter.croniter(date, "2023-01-01")
                cron_command = date
            except ValueError as e:
                raise ValueError("Invalid cron expression: " + str(e))

        job.setall(cron_command)
        cron.write()

def start_and_stop_job(name, status):
    with CronTab(user=user) as cron:
        for job in cron:
            if job.comment == name:
                match status.lower():
                    case 'enabled':
                        job.enable(False)
                    case 'disabled':
                        job.enable()
        cron.write()
    return None

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
            cron_expression = f"{job.minute} {job.hour} {job.dom} {job.month} {job.dow}"
            jobs.append({
                "name": job.comment,
                "cron": cron_expression,
                "command": job.command,
                "status": status
            })
            # print(f'"name": {job.comment}, "cron": {cron_expression}, "command": {job.command}, "status": {status}')
    return jobs

def update_job(name, new_name=None, new_command=None, new_date=None):
    with CronTab(user=user) as cron:
        for job in cron:
            if job.comment == name:
                if new_name:
                    job.comment = new_name
                if new_command:
                    job.command = new_command
                if new_date:
                    minute, hour, day_of_month, month, day_of_week = new_date.split()
                    job.setall(f"{minute} {hour} {day_of_month} {month} {day_of_week}")
        cron.write()
