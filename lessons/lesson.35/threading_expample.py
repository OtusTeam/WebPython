import math
from time import sleep, time
from threading import Thread
from multiprocessing.pool import ThreadPool

import requests
from loguru import logger


def process_search_results(query: str, *args) -> int:
    logger.info('Starting query {!r}, args {}', query, args)
    response = requests.get(
        'https://www.google.com/search',
        params={'q': query},
    )
    response_len = len(response.text)
    logger.info('Finished fetching query {!r} with len {}', query, response_len)
    sleep(1)

    logger.info('Finished processing query {!r}', query)
    return response_len


if __name__ == '__main__':
    # logger.info('Result {}', process_search_results('python'))
    # process_search_results('python')

    logger.info('Starting main')

    # thread = Thread(
    #     target=process_search_results,
    #     args=('python', 1, 2, None, object()),
    #     daemon=True,
    # )
    # thread.start()
    # thread.join()

    queries = (
        'iphone',
        'galaxy',
        'honor',
        'pycharm',
        'goland',
        'jetbrains',
        'otus',
        'google',
        'yandex',
        'yahoo',
    )
    # for query in queries:
    #     process_search_results(query)
    factorials_args = range(9300, 9900)

    queries *= 10
    start = time()

    # threads = []
    # for query in queries:
    #     thread = Thread(
    #         target=process_search_results,
    #         args=(query, ),
    #     )
    #     thread.start()
    #     threads.append(thread)
    #
    # for thread in threads:
    #     thread.join()


    # pool = ThreadPool(len(queries))
    # results = pool.map(process_search_results, queries)

    pool = ThreadPool(processes=1)
    factorials_lengths = pool.map(math.factorial, factorials_args)
    end = time()

    print(factorials_lengths)
    # print(results)

    logger.info('Finished in {:.3f}', end - start)

    # logger.info('running here')
    # sleep(2)
    logger.info('Finished main')
