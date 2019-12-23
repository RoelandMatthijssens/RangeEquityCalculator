import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="parse a texas hold'em hand range and return a list of possible hands")
    parser.add_argument("range", type=str, help="Range of hands to parse.")
    args = parser.parse_args()
    return args.range
