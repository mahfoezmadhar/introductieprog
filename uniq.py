def uniq(lst: list[object]) -> none:
    """
        >>> origineel = [3, 1, 3, 2, 1]
    >>> uniq(origineel)
    [3, 1, 2]
    >>> origineel
    [3, 1, 3, 2, 1]

    >>> uniq(["kat", "hond", "kat", "vis"])
    ['kat', 'hond', 'vis']
    >>> uniq([0, 0, 0])
    [0]
    >>> uniq([])
    []
    
    """
    nieuwe_lijst = []
    for letter in range(len(lst) - 1):
        nieuwe_lijst.append(letter)
        if lst[letter] == lst[letter + 1]:
            nieuwe_lijst.append(letter)
            nieuwe_lijst.remove(letter + 1)
    return nieuwe_lijst