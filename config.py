import logging
import os
from logging import basicConfig, StreamHandler

import dotenv
from python_logging import get_custom_logger
from datetime import datetime

log = get_custom_logger()

dotenv.load_dotenv(dotenv_path='.env')
APP_FOLDER = os.path.expanduser(os.getenv('APP_FOLDER'))
LOG_PATH = os.getenv('LOG_PATH', 'logs/')

#Generate unique log name with timestamp
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join(LOG_PATH, f'app_tests_{current_datetime}.log')

basicConfig(level=logging.INFO,
             hadlers=[StreamHandler(), StreamHandler(LOG_FILE)],
             format='%(levelname)s: %(message)s - logged at: {%Y-%m-%d_%H-%M-%S}')
