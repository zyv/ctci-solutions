def candidates(seq1, seq2):
    """
    >>> list(candidates((1, 3, 15, 11, 2), (23, 127, 235, 19, 8)))
    [(1, 8), (2, 8), (3, 8), (11, 8), (11, 19), (15, 19)]
    """
    i1, i2 = map(iter, map(sorted, (seq1, seq2)))
    v1, v2 = map(next, (i1, i2))
    while True:
        yield v1, v2
        if v1 < v2:
            v1 = next(i1)
        else:
            v2 = next(i2)


def smallest_difference(seq1, seq2):
    """
    >>> smallest_difference((1, 3, 15, 11, 2), (23, 127, 235, 19, 8))
    (3, (11, 8))
    """
    return min((abs(b - a), (a, b)) for a, b in candidates(seq1, seq2))
