import math
import multiprocessing
from time import time

from loguru import logger


if __name__ == '__main__':
    logger.info('Starting main')

    factorials_args = range(9500, 9900)

    start = time()

    # factorials = list(map(math.factorial, factorials_args))
    # factorials_lengths = list(map(lambda x: len(str(x)), factorials))
    # print('factorials_lengths', factorials_lengths)

    pool = multiprocessing.Pool(processes=32)

    factorials = pool.map(math.factorial, factorials_args)
    factorials_lengths = list(map(lambda x: len(str(x)), factorials))
    print('factorials_lengths', factorials_lengths)

    end = time()

    logger.info('it took {:.3f} seconds', end - start)

    logger.info('Finished main')
