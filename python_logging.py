import logging

def get_custom_logger(name = 'app_logger'):
    logger = logging.getLogger(name)

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('test.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)  # use logging.error('Exception error msg', exc_info=True) to log stack trace

    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.warning('This is a warning logger check')
    logger.error('This is an error logger check')

    return logger
