import datetime

import asyncio

async def run_periodically(wait_time, func, *args):

    """
    Helper for schedule_task_periodically.
    Wraps a function in a coroutine that will run the
    given function indefinitely
    :param wait_time: seconds to wait between iterations of func
    :param func: the function that will be run
    :param args: any args that need to be provided to func
    """
    while True:
        passed = func(*args)
        if passed:
            break
        await asyncio.sleep(wait_time)

def schedule_task_periodically(wait_time, func, *args):
    """
    Schedule a function to run periodically as an asyncio.Task
    :param wait_time: interval (in seconds)
    :param func: the function that will be run
    :param args: any args needed to be provided to func
    :return: an asyncio Task that has been scheduled to run
    """
    return asyncio.create_task(run_periodically(wait_time, func, *args))

async def cancel_scheduled_task(task):
    """
    Gracefully cancels a task
    :type task: asyncio.Task
    """
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

def count_seconds_since(then):
    """
    Prints the number of seconds that have passed since then
    :type then: datetime.datetime
    :param then: Time to count seconds from
    """
    now = datetime.datetime.now()
    passed = f"{(now - then).seconds} seconds have passed."
    open(passed, 'a').close()

    return (now - then).seconds > 10

async def main():

    print('bla bla bla')

    counter_task = schedule_task_periodically(3, count_seconds_since, datetime.datetime.now())

    # print("Doing something..")
    # await asyncio.sleep(1)
    # print("Doing something else..")
    # await asyncio.sleep(5)
    # print("Shutting down now...")

    # await cancel_scheduled_task(counter_task)
    print("Done")

if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(main())
