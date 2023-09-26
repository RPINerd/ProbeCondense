"""
    Probe Coverage Mapping | RPINerd, 09/26/23

    A python translation of the mapping functionality found in the Sequence Manipulation Suites' Primer Map tool.
    Original code is available under the GNU Public License v3.0 at:
        https://github.com/paulstothard/sequence_manipulation_suite/

    The translation process strips out the restriction enzyme and circular genome options and drops all the protein
    translation functionality as none of these are relevant to the probe coverage needs. Fuzzysearch is added to
    allow for mismatches in the oligo sequences and the output is modified to be more easily parsed
    by the probecondense.py script.
"""

from fuzzysearch import find_near_matches

import classes


def findMatches(probes: list[classes.Probe], sequence, isReverseStrand) -> classes.MatchCollection:
    matchList = []
    matchCollection = classes.MatchCollection()

    for probe in probes:
        matchList = find_near_matches(probe.sequence, sequence, max_insertions=0, max_deletions=0, max_substitutions=3)

        for hit in matchList:
            matchCollection.addMatch(classes.Match(probe.name, hit.matched, hit.start))
    return matchCollection


def layoutProbeMap(sequence, probeBindings) -> None:
    basesPerLine = 60
    spaceString = " " * 130

    return


def main(probes, targets) -> None:
    """"""
    newProbes = []
    for i in range(0, len(probes)):
        newProbes.append(classes.Probe(probes[i], i))

    for sequence in targets:
        # Create match collections
        probeBindings = findMatches(newProbes, sequence, False)

        print(probeBindings.matches)

        # Adjust probeBindings for the figure
        for j in range(0, len(probeBindings.matches)):
            probeBindings.matches[j].position = probeBindings.matches[j].position - len(
                probeBindings.matches[j].matchingText
            )
            probeBindings.matches[j].end = probeBindings.matches[j].position + len(
                probeBindings.matches[j].matchingText
            )
            if probeBindings.matches[j].position < 0:
                probeBindings.matches[j].position = probeBindings.matches[j].position + len(sequence)
            if probeBindings.matches[j].end > len(sequence):
                probeBindings.matches[j].end = probeBindings.matches[j].end - len(sequence)

        # Sort probeBindings
        probeBindings.sortMatches()

        layoutProbeMap(sequence, probeBindings)

        # Write summary of probes
        # writeprobesites(newProbes)

    return
