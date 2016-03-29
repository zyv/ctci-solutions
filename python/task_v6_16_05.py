def count_zeros(n):
    """
    >>> count_zeros(1)
    0
    >>> count_zeros(5)
    1
    >>> count_zeros(10)
    2
    >>> count_zeros(25)
    6
    """
    res = 0
    while n >= 5:
        res += n // 5
        n //= 5
    return res
