import asyncio
from time import sleep

from loguru import logger


def foo_sync():
    logger.info('foo_sync starting')
    sleep(.1)
    logger.info('foo_sync finishing')


def bar_sync():
    logger.info('bar_sync starting')
    sleep(.1)
    logger.info('bar_sync finishing')


def run_sync():
    logger.info('run_sync')
    logger.info(foo_sync())
    logger.info(bar_sync())


async def foo():
    logger.info('foo starting')
    await asyncio.sleep(.1)
    logger.info('foo finishing')


async def bar():
    logger.info('bar starting')
    await asyncio.sleep(.11)
    logger.info('bar finishing')


async def main_async():
    await foo()
    await bar()


def main():
    logger.info('Starting main')

    # run_sync()
    # logger.info(main_async())

    coros = [
        foo(),
        bar(),
    ]

    fut = asyncio.wait(coros)

    loop = asyncio.get_event_loop()

    # loop.run_until_complete(main_async())
    loop.run_until_complete(fut)

    loop.close()

    logger.info('Finishing main')



if __name__ == '__main__':
    main()
