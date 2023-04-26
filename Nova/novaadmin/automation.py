from apscheduler.schedulers.background import BackgroundScheduler
from .auto import automate


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(automate, 'interval', seconds=10)
    scheduler.start()
