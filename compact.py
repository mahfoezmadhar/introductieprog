def compact(lst: list[object]) -> none:
    """
    >>> origineel = [0, 3, "", "hallo", False, None, [], -2, 3]
    >>> compact(origineel)
    [3, 'hallo', -2, 3]
    >>> origineel
    [0, 3, '', 'hallo', False, None, [], -2, 3]

    >>> compact([0, "", False, None, [], {}])
    []
    >>> compact([])
    []
    
    """
    nieuwe_lijst = []
    x = []
    for letter in lst:
        if letter:
            nieuwe_lijst.append(letter)
    return nieuwe_lijst
            
            
            