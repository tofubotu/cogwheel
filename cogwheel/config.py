import logging
import sys

def getLogger(name='Generic', file="core.log"):
    format='%(asctime)s %(name)s %(levelname)s: %(message)s'
    formatter = logging.Formatter(format)
    fh = logging.FileHandler(file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
