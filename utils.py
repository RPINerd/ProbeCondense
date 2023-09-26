def reverse(sequence):
    return sequence[::-1]

function findMatches(primers, sequence, isReverseStrand) {
    var matchArray;
    var matchPosition;
    var matchCollection = new MatchCollection();
    var re;
  
    for (var i = 0; i < primers.length; i++) {
        re = primers[i].re;
        while ((matchArray = re.exec(sequence))) {
            matchPosition = re.lastIndex;
            matchCollection.addMatch(
            new Match(primers[i].name, matchArray[0], matchPosition)
            );
            if (isReverseStrand) {
            primers[i].hasReverseMatch = true;
            } else {
            primers[i].hasForwardMatch = true;
            }
            re.lastIndex = re.lastIndex - RegExp.lastMatch.length + 1;
        }
    }
    
    return matchCollection;
  }


def convertDegenerates(sequence):
    sequence = sequence.toLowerCase();
    sequence = sequence.replace(/t/g, "[TU]");
    sequence = sequence.replace(/r/g, "[AGR]");
    sequence = sequence.replace(/y/g, "[CTUY]");
    sequence = sequence.replace(/s/g, "[GCS]");
    sequence = sequence.replace(/w/g, "[ATUW]");
    sequence = sequence.replace(/k/g, "[GTUK]");
    sequence = sequence.replace(/m/g, "[ACM]");
    sequence = sequence.replace(/b/g, "[CGTUBSKY]")
    sequence = sequence.replace(/d/g, "[AGTUDRKW]")
    sequence = sequence.replace(/h/g, "[ACTUHMYW]")
    sequence = sequence.replace(/v/g, "[ACGVSMR]")
    sequence = sequence.replace(/n/g, "[ACGTURYSWKMBDHVN]")
    return sequence