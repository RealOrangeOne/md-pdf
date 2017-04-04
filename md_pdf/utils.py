import shutil
import os
import logging

logger = logging.getLogger(__file__)


def remove_dir(dir):
    logger.debug("Removing directory {}.".format(dir))
    try:
        shutil.rmtree(dir)
        os.rmdir(dir)
    except FileNotFoundError:
        pass


def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default
