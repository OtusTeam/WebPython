import math
from time import time
import multiprocessing

from loguru import logger


if __name__ == '__main__':
    logger.info('Starting main')

    factorials_args = range(9700, 9900)

    start = time()

    # factorials = list(map(math.factorial, factorials_args))
    # factorials_lengths = list(map(lambda x: len(str(x)), factorials))
    # print(factorials_lengths)

    pool = multiprocessing.Pool(processes=32)

    factorials = pool.map(math.factorial, factorials_args)
    factorials_lengths = list(map(lambda x: len(str(x)), factorials))
    print(factorials_lengths)

    end = time()

    logger.info('Finished in {:.3f}', end - start)

    logger.info('Finished main')
