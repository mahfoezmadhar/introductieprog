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
    for letter in lst:
        is letter not in nieuwe_lijst:
            nieuwe_lijst.append(letter)