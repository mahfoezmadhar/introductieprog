def select_not_lower(strs: list[str]) -> str:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['roep', 'HALLO']
    
    
    """
    nieuwe_lijst = []
    for woord in strs:
        for teken in woord:
            if teken.islower
                nieuwe_lijst.append(woord)
    return nieuwe_lijst