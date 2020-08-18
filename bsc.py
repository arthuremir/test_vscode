from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time

scheduler = BlockingScheduler()

with open('res.txt', 'a') as f:
    f.write('Started\n')

@scheduler.scheduled_job('interval', seconds=3)
def make_post():
        global i, scheduler

        with open('res.txt', 'a') as f:
            f.write(str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S")) + '\n')

        # open(, 'a').close()
        i += 1

        if i == 5:
            scheduler.remove_all_jobs()

i = 0
scheduler.start()
with open('res.txt', 'a') as f:
    f.write('After start\n')

    