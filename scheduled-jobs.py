from apscheduler.schedulers.blocking import BlockingScheduler
import random
import app

sched = BlockingScheduler()

# CONSTANTS
TRASH_WEEK_BASE_MESSAGE = ', it is your week to take out the trash'
HOUSEMATE_LIST = ['PJ', 'Mike', 'Drex', 'George']

# REMINDERS
def rent_payment_reminder():
    msg = 'Reminder to pay Mike rent!'
    app.send_message(msg)

def trash_week_reminder_pj():
    msg = 'PJ' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

def trash_week_reminder_drex():
    msg = 'Drex' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

def trash_week_reminder_george():
    msg = 'George' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

def trash_week_reminder_mike():
    msg = 'Mike' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

# Choose a random housemate from the housemate list, then append to base trash reminder message
def trash_week_reminder_random():
    housemate = random.choice(HOUSEMATE_LIST)
    msg = housemate + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

# SCHEDULED JOBS
# Send rent reminder message on the 25th of every month at 7:30pm
@sched.scheduled_job('cron', day=25, hour=19, minute=30)
def rent_reminder_job():
    rent_payment_reminder()

@sched.scheduled_job('cron', day='1st mon', hour=16, minute=30)
def trash_job_pj():
    trash_week_reminder_pj()

@sched.scheduled_job('cron', day='2nd mon', hour=16, minute=30)
def trash_job_drex():
    trash_week_reminder_drex()

@sched.scheduled_job('cron', day='3rd mon', hour=16, minute=30)
def trash_job_george():
    trash_week_reminder_george()

@sched.scheduled_job('cron', day='4th mon', hour=16, minute=30)
def trash_job_mike():
    trash_week_reminder_mike()

@sched.scheduled_job('cron', day='5th mon', hour=16, minute=30)
def trash_job_random():
    trash_week_reminder_random()

sched.start()