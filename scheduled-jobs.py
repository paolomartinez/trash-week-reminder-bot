
from apscheduler.schedulers.blocking import BlockingScheduler
import app

sched = BlockingScheduler()

# REMINDERS
def rent_payment_reminder():
    msg = 'Reminder to pay Mike rent!'
    app.send_message(msg)

# Scheduled job to send rent reminder message on the 25th of every month at 7:30pm
#@sched.scheduled_job('cron', day=25, hour=19, minute=30)
@sched.scheduled_job('cron', day=4, hour=22, minute=26)
def rent_reminder_job():
    rent_payment_reminder()

sched.start()