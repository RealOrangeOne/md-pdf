import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Display verbose output", action="count", default=0)
    parser.add_argument("--update-csl", help="Update CSL files", action="store_true")
    parser.add_help = True
    return parser.parse_args()
