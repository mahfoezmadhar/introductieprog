def select_not_lower(strs: list[str]) ->:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['roep', 'HALLO']
    
    
    """
    nieuwe_lijst = []
    for teken in strs:
        if teken.isupper() in strs:
            nieuwe_lijst.append()