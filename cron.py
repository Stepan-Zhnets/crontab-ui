# import
from crontab import CronTab

user = "user"

with CronTab(user='user') as cron:
    job = cron.new(command='echo hello_world >> ~/test.txt')
    job.minute.every(1)
print('cron.write() was just executed')

def check_job():
	...

def create_job(name, date, command):
	...

def start_and_stop_job(name, status):
	...

def delete_job(name):
	...

