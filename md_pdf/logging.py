import logging
from md_pdf.utils import safe_list_get


FORMAT = "[%(levelname)s]: %(message)s"
LOG_LEVELS = [
    logging.WARN,
    logging.INFO,
    logging.DEBUG,
    logging.NOTSET
]


def set_verbosity(args):
    level = min(args.verbose, len(LOG_LEVELS) - 1)
    verbosity = safe_list_get(LOG_LEVELS, level, logging.NOTSET)
    logging.basicConfig(format=FORMAT, level=verbosity)
