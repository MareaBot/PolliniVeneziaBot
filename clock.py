from apscheduler.schedulers.blocking import BlockingScheduler

from pollinivenezianibot.runner import run

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=5)
def timed_job():
    run()


sched.start()
