from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    listA = a.splitlines()
    listB = b.splitlines()
    similarLines = []

    for line in range(len(listA)):
        if listA[line] == listB[line]:
            similarLines.append(listA[line])

    return similarLines


def sentences(a, b):
    """Return sentences in both a and b"""
    tokenizedListA = sent_tokenize(a)
    tokenizedListB = sent_tokenize(b)
    similarSentences = []

    for sentence in range(len(tokenizedListA)):
        currentSentence = tokenizedListA[sentence]
        if currentSentence in tokenizedListB and not currentSentence in similarSentences:
            similarSentences.append(currentSentence)


    return similarSentences


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    similarSubstrings = []
    position = 0
    stringLength = len(a)

    while position + n <= stringLength:
        end = position + n
        currentSubstring = a[position:end]
        if currentSubstring in b and currentSubstring not in similarSubstrings:
            similarSubstrings.append(currentSubstring)
        position + 1

    return similarSubstrings
