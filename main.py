from decorators import timeit
import logging.config
import logging
import yaml
import os

logger = logging.getLogger(__name__)


# @timeit logs start and end and stores exec time for the function.
@timeit
def func_new():
    """new way of logging function in main"""
    # doc string is compulsory. Last keyword gets used to identify the parent file from where function is defined.
    import time
    time.sleep(5)


def func_old():
    import datetime
    import time
    start = datetime.datetime.now()
    logger.info('func_old started')
    logger.info('I hail from the stone age')
    logger.warning('This is how you would have done logging normally!')
    time.sleep(3)
    end = datetime.datetime.now()
    logger.critical('Not anymore.')
    logger.info('func_old ended')
    logger.info('Exec took: {}'.format(end-start))


def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO
):
    """Setup logging configuration in anomaly_detection"""
    path = default_path
    print(default_path)
    fopen = open(default_path)
    fopen.close()
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        raise SystemExit(0)


if __name__ == "__main__":
    setup_logging()
    func_old()
    func_new()
    print('Check logs/')
