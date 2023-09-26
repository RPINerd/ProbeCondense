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
import utils


def findMatches(probes: list[classes.Probe], sequence, isReverseStrand) -> classes.MatchCollection:
    matchList = []
    matchCollection = classes.MatchCollection()

    for probe in probes:
        matchList = find_near_matches(probe.sequence, sequence, max_insertions=0, max_deletions=0, max_substitutions=3)

        for hit in matchList:
            matchCollection.addMatch(classes.Match(probe.name, hit.matched, hit.start))
            if isReverseStrand:
                probe.hasReverseMatch = True
            else:
                probe.hasForwardMatch = True
    return matchCollection


def layoutProbeMap(sequence, forwardMatches, reverseMatches) -> None:
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
        forwardMatches = findMatches(newProbes, sequence, False)
        reverseMatches = findMatches(newProbes, utils.reverse(sequence), True)

        print(forwardMatches.matches)
        print(reverseMatches.matches)

        # Adjust forwardMatches for the figure
        for j in range(0, len(forwardMatches.matches)):
            forwardMatches.matches[j].position = forwardMatches.matches[j].position - len(
                forwardMatches.matches[j].matchingText
            )
            forwardMatches.matches[j].end = forwardMatches.matches[j].position + len(
                forwardMatches.matches[j].matchingText
            )
            if forwardMatches.matches[j].position < 0:
                forwardMatches.matches[j].position = forwardMatches.matches[j].position + len(sequence)
            if forwardMatches.matches[j].end > len(sequence):
                forwardMatches.matches[j].end = forwardMatches.matches[j].end - len(sequence)

        # now adjust reverseMatches for the figure
        for j in range(0, len(reverseMatches.matches)):
            reverseMatches.matches[j].position = len(sequence) - reverseMatches.matches[j].position
            reverseMatches.matches[j].end = reverseMatches.matches[j].position + len(
                reverseMatches.matches[j].matchingText
            )
            if reverseMatches.matches[j].position < 0:
                reverseMatches.matches[j].position = reverseMatches.matches[j].position + len(sequence)
            if reverseMatches.matches[j].end > len(sequence):
                reverseMatches.matches[j].end = reverseMatches.matches[j].end - len(sequence)

        # sort forwardMatches and reverseMatches.
        forwardMatches.sortMatches()
        reverseMatches.sortMatches()

        layoutProbeMap(sequence, forwardMatches, reverseMatches)

        # write summary of probes
        # writeprobesites(newProbes)

        # set probes hasMatch to false
        for primer in newProbes:
            primer.hasForwardMatch = False
            primer.hasReverseMatch = False

    return
