import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("autoguardian")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        "autoguardian.log", maxBytes=500*1024, backupCount=3
    )

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)


    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger
logger = setup_logger()