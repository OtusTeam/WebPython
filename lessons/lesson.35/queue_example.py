from time import time
from queue import Queue
from math import factorial
from threading import Thread

from loguru import logger

THREADS_COUNT = 10

q = Queue()


def worker():
    while 1:
        item = q.get()
        res = factorial(item)
        # logger.info('Processed {}. Length is {}', item, len(str(res)))
        q.task_done()


if __name__ == '__main__':

    logger.info('Starting main')

    factorials_args = range(9300, 9900)

    for _ in range(THREADS_COUNT):
        thread = Thread(
            target=worker,
            daemon=True,
        )
        thread.start()

    logger.info('Fulfilling queue')
    for item in factorials_args:
        q.put(item)

    start = time()
    q.join()
    end = time()

    logger.info('Finished in {:.3f}', end - start)

    logger.info('Finished main')

