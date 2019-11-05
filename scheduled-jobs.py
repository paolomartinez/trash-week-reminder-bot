
from apscheduler.schedulers.blocking import BlockingScheduler
import app

sched = BlockingScheduler()

# REMINDERS
def rent_payment_reminder():
    msg = 'Reminder to pay Mike rent!'
    app.send_message(msg)

@sched.scheduled_job('cron', day=4, hour=20, minute=13)
def rent_reminder_job():
    rent_payment_reminder()

sched.start()