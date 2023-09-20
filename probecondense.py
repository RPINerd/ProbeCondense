"""
    Probe Condensing Tool | RPINerd, 09/19/23

    A script that takes in a set of oligos and target sequences and condenses the oligos so
    that there are as few possible overlaps when mapping them against the target sequences.
"""

import argparse
import os
import sys


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


def main(args) -> None:
    return


if __name__ == "__main__":
    args = parse_args()
    main(args)
