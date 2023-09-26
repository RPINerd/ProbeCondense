"""
    Probe Coverage Mapping | RPINerd, 09/26/23

    A python translation of the mapping functionality found in the Sequence Manipulation Suites' Primer Map tool. Original code is available under the GNU Public License v3.0 at https://github.com/paulstothard/sequence_manipulation_suite/
"""

from fuzzysearch import find_near_matches

import classes
import utils


def findMatches(primers: list[classes.Primer], sequence, isReverseStrand) -> classes.MatchCollection:
    matchList = []
    matchCollection = classes.MatchCollection()

    for primer in primers:
        matchList = find_near_matches(primer.sequence, sequence, max_insertions=0, max_deletions=0, max_substitutions=3)

        for hit in matchList:
            matchCollection.addMatch(classes.Match(primer.name, hit.matched, hit.start))
            if isReverseStrand:
                primer.hasReverseMatch = True
            else:
                primer.hasForwardMatch = True
    return matchCollection


def main(primers, targets) -> None:
    sequence = ""
    newPrimers = []
    for i in range(0, len(primers)):
        newPrimers.append(classes.Primer(primers[i], i))

    for sequence in targets:
        # Create match collections
        forwardMatches = findMatches(newPrimers, sequence, False)
        reverseMatches = findMatches(newPrimers, utils.reverse(sequence), True)

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
            if reverseMatches.matches[j].end > len(sequence.length):
                reverseMatches.matches[j].end = reverseMatches.matches[j].end - len(sequence)

        # sort forwardMatches and reverseMatches.
        forwardMatches.sortMatches()
        reverseMatches.sortMatches()

        # layoutPrimerMap(sequence, forwardMatches, reverseMatches, basesPerLine)

        # write summary of primers
        # writePrimerSites(newPrimers)

        # set primers hasMatch to false
        for primer in newPrimers:
            primer.hasForwardMatch = False
            primer.hasReverseMatch = False

    return
