from apscheduler.schedulers.blocking import BlockingScheduler
import random
import requests
import app

sched = BlockingScheduler()

# CONSTANTS
RANDOM_PREFIX_LIST = ['Good googly moogly! ', 'feelsbadman. ', 'heyyyyyy :) ur gonna hate me but ', 'poggers! ']
RANDOM_CHOICE_MESSAGE = 'You were randomly selected on this fifth Monday. '
TRASH_WEEK_BASE_MESSAGE = ', it is your week to take out the trash'
HOUSEMATE_LIST = ['PJ', 'Mike', 'Drex', 'Eugene']

# REMINDERS
def rent_payment_reminder():
    msg = 'Reminder to pay Mike rent via Zelle!'
    app.send_message(msg)

def trash_week_reminder_pj():
    msg = 'PJ' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

def trash_week_reminder_drex():
    msg = 'Drex' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

def trash_week_reminder_eugene():
    msg = 'Eugene' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

def trash_week_reminder_mike():
    msg = 'Mike' + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

# Choose a random housemate from the housemate list, then append to base trash reminder message
def trash_week_reminder_random():
    housemate = random.choice(HOUSEMATE_LIST)
    random_msg = random.choice(RANDOM_PREFIX_LIST) + RANDOM_CHOICE_MESSAGE
    msg = random_msg + housemate + TRASH_WEEK_BASE_MESSAGE
    app.send_message(msg)

# SCHEDULED JOBS
# Send rent reminder message on the 25th of every month at 7:30pm
@sched.scheduled_job('cron', day=20, hour=19, minute=30)
def rent_reminder_job():
    rent_payment_reminder()
    print('SUCCESS! Ran rent reminder job')

@sched.scheduled_job('cron', day='1st mon', hour=18, minute=30)
def trash_job_pj():
    trash_week_reminder_pj()
    print('SUCCESS! Ran trash week reminder job for PJ')

@sched.scheduled_job('cron', day='2nd mon', hour=18, minute=30)
def trash_job_drex():
    trash_week_reminder_drex()
    print('SUCCESS! Ran trash week reminder job for Drex')

@sched.scheduled_job('cron', day='3rd mon', hour=18, minute=30)
def trash_job_eugene():
    trash_week_reminder_eugene()
    print('SUCCESS! Ran trash week reminder job for Eugene')

@sched.scheduled_job('cron', day='4th mon', hour=18, minute=30)
def trash_job_mike():
    trash_week_reminder_mike()
    print('SUCCESS! Ran trash week reminder job for Mike')

@sched.scheduled_job('cron', day='5th mon', hour=18, minute=30)
def trash_job_random():
    trash_week_reminder_random()
    print('SUCCESS! Ran random trash week reminder job for the 5th Monday')

@sched.scheduled_job('interval', minutes=30)
def keep_dyno_alive():
    url     = 'https://trash-week-bot.herokuapp.com/'
    res = requests.get(url)

sched.start()