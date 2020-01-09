import asyncio
from random import randint
from time import sleep

from loguru import logger

TIMES = 10


def random_sleep_time():
    return randint(1, 5) * .1


def function_sync(i: int):
    """
    :param i:
    :return:
    """
    logger.info('{} starting', i)
    t = random_sleep_time()
    sleep(t)
    logger.info('{} sync done in {}', i, t)


async def function_async(i: int):
    """
    :param i:
    :return:
    """
    logger.info('{} starting', i)
    t = random_sleep_time()
    await asyncio.sleep(t)
    logger.info('{} sync done in {}', i, t)


def start_sync():
    for i in range(TIMES):
        function_sync(i)


async def start_async():
    logger.info('Starting async')
    futures = [asyncio.ensure_future(function_async(i)) for i in range(TIMES)]
    logger.info('Ensured all futures')
    await asyncio.wait(futures)


def main():
    # start_sync()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_async())
    loop.close()

    logger.info('Finished')



if __name__ == '__main__':
    main()
