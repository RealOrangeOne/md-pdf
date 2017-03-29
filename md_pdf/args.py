import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Display verbose output", action="store_true")
    return parser.parse_args()
