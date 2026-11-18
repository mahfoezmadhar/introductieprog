def select_not_lower(strs: list[str]) -> str:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['Roep', 'HALLO']
    >>> select_not_lower(['niks', 'mooi', 'winkel'])
    []
    >>> select_not_lower(['Hoi', 'Hallo', 'HALLO'])
    ['Hoi', 'Hallo', 'HALLO']
    >>>
    
    """
    nieuwe_lijst = []
    for woord in strs:
        teller = 0
        for teken in woord:
            if not teken.islower():
                teller += 1
        if teller >= 1:
            nieuwe_lijst.append(woord)
    return nieuwe_lijst