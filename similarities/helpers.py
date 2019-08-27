from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    # TODO
    similar = set()

    read1 = set(a.split('\n'))
    read2 = set(b.split('\n'))

    similar = read1 & read2

    return similar


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    similar =[]
    # sentences1 = sent_tokenize(a)
    # sentences1 = sent_tokenize(b)
    c = list(set(sent_tokenize(a)))
    d = list(set(sent_tokenize(b)))

    for i in c:
        if i in d:
            similar.append(i)
    # print(similar)
    # print(c)
    # print(d)
    return similar


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
