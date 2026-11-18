def select_not_lower(strs: list[str]) ->:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['roep', 'HALLO']
    
    
    """
    nieuwe_lijst = []
    for woord in strs:
        for teken in woord:
            if teken.isupper():
                nieuwe_lijst.append(woord)
    