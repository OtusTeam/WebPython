import asyncio
from time import sleep
from random import randint

from loguru import logger


TIMES = 10


def random_sleep_time() -> float:
    return randint(0, 5) * .001


def function_sync(i: int):
    logger.info("{} sync starting", i)
    t = random_sleep_time()
    sleep(t)
    logger.info("{} sync done in {}", i, t)


async def function_async(i: int):
    logger.info("{} async starting", i)
    t = random_sleep_time()
    await asyncio.sleep(t)
    # logger.info("{} finished sleeping {}", i, t)
    # for _ in range(10000):
    #     if _ % 1000 == 0:
    #         logger.info("{} sleeping, {}", i, _)
    #         await asyncio.sleep(0)
    logger.info("{} async done in {}", i, t)


def start_sync():
    for i in range(TIMES):
        function_sync(i)


async def start_async():
    logger.info("Starting async")
    futures = [asyncio.ensure_future(function_async(i)) for i in range(TIMES)]
    logger.info("Ensured all futures")
    await asyncio.wait(futures)


def main():
    # start_sync()
    loop = asyncio.get_event_loop()
    fut = start_async()
    loop.run_until_complete(fut)
    loop.close()


if __name__ == '__main__':
    main()
