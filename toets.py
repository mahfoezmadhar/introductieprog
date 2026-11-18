def select_not_lower(strs: list[str]) -> str:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['Roep', 'HALLO']
    >>> select_not_lower(['niks', 'mooi', 'winkel'])
    []
    >>> select_not_lower(['Hoi', 'Hallo', 'HALLO'])
    ['Hoi', 'Hallo', 'HALLO']
    >>> select_not_lower(['banaan', 'Cadeau', 'Mahfoez'])
    ['Cadeau', 'Mahfoez']
    
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
    
    
def string_picker(strs: list[str], picks: list[int]) -> str:
    """
    >>> string_picker(['a', 'dd'] , [0, 0, 1])
    'aadd'
    >>> string_picker(['h', 'a', 'l', 'o'], [0, 1, 2, 2, 3])
    'hallo'
    >>> string_picker(['w', 'ord'] , [0, 0, 1])
    'wword'
    >>> string_picker(['ge', 'vens'] , [0, 0, 1])
    'gegevens'
    
    """
    nieuwe_string = ""
    for teken in range(len(picks)):
        nieuwe_string += strs[picks[teken]]
        
    return nieuwe_string
    
def remove_prefix(s: str, prefix: str) -> str:
    """
    >>> remove_prefix('toedeloe', 'toe')
    'deloe'
    
    """
    verbeterd = ""
    for index in range(len(s))
    
    
