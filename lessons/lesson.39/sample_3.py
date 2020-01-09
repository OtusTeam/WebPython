import asyncio
from asyncio import CancelledError
from dataclasses import dataclass
from time import time
from typing import Union

from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    ip_field: str


SERVICES = [
    Service('ipify', 'https://api.ipify.org/?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
]


async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    """
    :param service:
    :return:
    """
    my_ip = 'not found'
    logger.info('Starting with {}', service.name)
    start = time()

    try:
        async with ClientSession() as session:
            result = await fetch(session, service.url)
    except OSError:
        logger.exception('Failed fetchin {}', service.name)
        return 'error'
    except CancelledError:
        logger.debug('Cancelled {}', service.name)
        raise

    end = time()
    logger.info('Fetched {} from {} in {:.3f}s', result, service.name, end - start)

    try:
        my_ip = result[service.ip_field]
    except KeyError:
        logger.exception('Could not get ip by field {!r} from {}', service.ip_field, result)

    return my_ip


async def fetch_ip_fastest(timeout: Union[int, float] = 1) -> str:
    """
    :param timeout:
    :return:
    """

    my_ip = 'no result'

    futures = [fetch_ip(s) for s in SERVICES]
    done, pending = await asyncio.wait(
        futures,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )

    for fut in pending:
        fut.cancel()

    for fut in done:
        my_ip = fut.result()
        break
    else:
        logger.warning('Could not fetch any results in {}s', timeout)

    return my_ip


def fetch_my_ip():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(fetch_ip_fastest(0.9))
    loop.close()
    return res


def main():
    res = fetch_my_ip()
    logger.info('Got result: {!r}', res)


if __name__ == '__main__':
    main()
