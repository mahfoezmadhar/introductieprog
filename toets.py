def select_not_lower(strs: list[str]) -> str:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['roep', 'HALLO']
    
    
    """
    nieuwe_lijst = []
    teller = 0
    for woord in strs:
        for teken in woord:
            if teken.islower == False:
                teller += 1
        if teller >= 1:
            
    return nieuwe_lijst