import logging
import sys

from etc.config import ConfigHandler

def initialize_logging():
    config = ConfigHandler()

    log_level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR
    }

    logger = logging.getLogger()
    logger.setLevel(log_level[config['log_level']])
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s', 
                                '%m-%d-%Y %H:%M:%S')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(config['log_file'])
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    logging.info('Logging configured.')
