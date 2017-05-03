import logging
from md_pdf.args import parse_args
from md_pdf.exceptions import PrematureExit, BaseException
from md_pdf.logging import set_verbosity
from md_pdf.build import build
from md_pdf.config.read import load_config
from md_pdf.config.validate import validate_config
from md_pdf.csl import check_csl, download_csl


def cli():
    args = parse_args()
    set_verbosity(args)
    try:
        if args.update_csl:
            download_csl()
            return 0
        check_csl()
        config = load_config()
        validate_config(config)
        build(config)
    except BaseException as e:
        logging.error(str(e))
        return 1
    except KeyboardInterrupt:
        logging.error("Aborted.")
        return 1
    return 0
