class Probe:
    def __init__(self, probe, id):
        self.name = id
        self.sequence = probe


class Match:
    def __init__(self, id, matchingText, position):
        self.id = id
        self.matchingText = matchingText
        self.position = position
        self.end = 0


class MatchCollection:
    def __init__(self):
        self.matches = []

    def addMatch(self, match) -> None:
        self.matches.append(match)

    def sortMatches(self) -> None:
        """AI interpreted from:

        function matchSorter(a, b) {
            if (a.position < b.position) {
                return 1;
            }
            if (a.position > b.position) {
                return -1;
            } else {
                return 0;
            }
        }
        """
        self.matches.sort(key=lambda x: x.position)

    def getMatchesInRange(self, start, stop) -> list:
        matchesInRange = []
        i = len(self.matches) - 1
        while i >= 0:
            if self.matches[i].position >= start and self.matches[i].position < stop:
                matchesInRange.append(self.matches[i])
                self.matches.pop(i)
            else:
                break
            i -= 1
        return matchesInRange
