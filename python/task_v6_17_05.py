def longest_subarray(s):
    """
    >>> longest_subarray('')
    ''
    >>> longest_subarray('AA')
    ''
    >>> longest_subarray('A1')
    'A1'
    >>> longest_subarray('AAA7BB88')
    'A7BB88'
    """
    levels = {0: (0, 0)}
    current_level = 0
    for index, increment in enumerate((+1 if c.isdigit() else -1 for c in s), start=1):
        current_level += increment
        levels[current_level] = (
            index if current_level not in levels else levels[current_level][0],
            index
        )

    left, right = max(levels.values(), key=lambda indices: indices[1] - indices[0])

    return s[left:right]
