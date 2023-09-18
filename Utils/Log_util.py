import logging
import logging.handlers
import time
from Utils.Global_var import *


# Initialize log configuration
def log_config_init():
    # Initialize a log object
    logger = logging.getLogger('logger')

    # Setting log level
    logger.setLevel(logging.INFO)

    # Create a console log handler
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)

    # Create a file log handler and daily log file
    """
    1、when: Time unit, optional parameter
    2、interval: Time interval
    3、backupCount: Number of log file backups. If backupCount is greater than 0, then when a new log file is generated,
     only backupCount files will be retained and the oldest file will be deleted.
    """
    filename_day = PROJECT_ROOT_DIR + "/Log/" + "interface_auto_test.{}.log".format(time.strftime("%Y-%m-%d"))
    fh_day = logging.handlers.TimedRotatingFileHandler(filename_day, when='MIDNIGHT', interval=1, backupCount=3,
                                                       encoding='utf-8')

    # Create summary log files
    fh_all = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='MIDNIGHT', interval=1, backupCount=3,
                                                       encoding='utf-8')

    # Set log format and create formatter
    fmt = '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # Set formatter into logger
    sh.setFormatter(formatter)
    fh_day.setFormatter(formatter)
    fh_all.setFormatter(formatter)

    # Add a log handler to the log object
    # Determine whether the log handler is empty to avoid repeated log entry
    if not logger.handlers:
        logger.addHandler(sh)
        logger.addHandler(fh_all)
        logger.addHandler(fh_day)
    else:
        logger.handlers.clear()
        logger.addHandler(sh)
        logger.addHandler(fh_all)
        logger.addHandler(fh_day)

    return logger
