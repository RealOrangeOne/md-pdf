import argparse
from md_pdf import __version__


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Set verbosity level (repeat argument)", action="count", default=0)
    parser.add_argument("--update-csl", help="Update CSL files", action="store_true")
    parser.add_argument("--version", action="version", version="%(prog)s {}".format(__version__))
    parser.add_help = True
    return parser.parse_args(args=args)
