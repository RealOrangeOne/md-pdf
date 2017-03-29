import logging
from md_pdf.args import parse_args
from md_pdf.exceptions import PrematureExit
from md_pdf.build import build
from md_pdf.config.read import load_config


FORMAT = "[%(levelname)s]: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)


def cli():
    args = parse_args()
    try:
        config = load_config()
        build(args, config)
    except PrematureExit:
        return 0
    except Exception as e:
        logging.error(str(e))
        return 1
    return 0
