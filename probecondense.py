"""
    Probe Condensing Tool | RPINerd, 09/19/23

    A script that takes in a set of oligos and target sequences and condenses the oligos so
    that there are as few possible overlaps when mapping them against the target sequences.
"""

import argparse

import probemap


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--probes", help="Path to the probes file", required=True)
    parser.add_argument("-t", "--targets", help="Path to the targets file", required=True)
    args = parser.parse_args()
    return args


def main(args) -> None:
    probes = []
    targets = []
    with open(args.probes, "r") as probesFile:
        probes.append(probesFile.readlines())
    print(probes)
    with open(args.targets, "r") as targetsFile:
        targets.append(targetsFile.readlines())
    print(targets)
    probemap.main(probes, targets)
    return


if __name__ == "__main__":
    args = parse_args()
    main(args)
