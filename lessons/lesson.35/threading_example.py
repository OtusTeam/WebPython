# import logging
import math
import threading
from time import sleep, time
from multiprocessing.pool import ThreadPool

import requests
from loguru import logger
#
# logging.basicConfig(level=logging.WARNING)
# logger = logging.getLogger(__name__)


def process_google_results(query: str) -> int:
    logger.info('Starting searching for {!r}', query)
    response = requests.get(
        'https://www.google.com/search',
        params={'q': query},
    )
    logger.info('Got answer for {}', query)
    text = response.text
    # result = parse_search_results_for_query(query, text)
    # save_result_to_db(result)
    sleep(1)
    response_len = len(text)
    logger.info('Finished processing query {!r} with result len {}', query, response_len)
    # if response_len > 200_000:
    #     try:
    #         1/0
    #     except ZeroDivisionError:
    #         logger.exception('Eororor!')
    #         return None
    return response_len


def process_factorial(item: int) -> int:
    factorial = math.factorial(item)
    factorial_length = len(str(factorial))
    return factorial_length


if __name__ == '__main__':
    logger.info('Starting main')

    # query = 'python'
    # process_google_results(query)
    #
    # queries = (
    #     'iphone',
    #     'galaxy',
    #     'huawei',
    # )
    # for query in queries:
    #     logger.info('query {!r} start', query)
    #     process_google_results(query)
    #     logger.info('query {!r} finish', query)

    # thread = threading.Thread(
    #     target=process_google_results,
    #     args=('python', ),
    #     daemon=True,
    # )
    # thread.start()
    #
    # thread.join()
    #
    # threads = []
    # for query in queries:
    #     thread = threading.Thread(
    #         target=process_google_results,
    #         args=(query, ),
    #     )
    #     logger.info('before start {}', query)
    #     thread.start()
    #     logger.info('after start {}', query)
    #     # threads.append(thread)
    #     threads.append((thread, query))
    #
    # # for thread in threads:
    # #     thread.join()
    #
    # for thread, query in threads:
    #     logger.info('Joining thread {}', query)
    #     thread.join()
    #     logger.info('Finished thread {}', query)

    queries = (
        'iphone',
        'galaxy',
        'huawei',
        'xiaomi',
        'pycharm',
        'jetbrains',
        'vscode',
        'yandex',
        'google',
    )

    queries *= 2


    factorials_args = range(9500, 9900)

    start = time()

    pool = ThreadPool(9)
    # results = pool.map(process_google_results, queries)
    results = pool.map(process_factorial, factorials_args)
    print(results)
    end = time()

    logger.info('pool took {:.3f} seconds', end - start)
    logger.info('results: {}', results)

    logger.info('Finished main')
