def select_containing(words: list[str], letters: str) -> list[str]:
    """
    geef alleen de words terug die de letters bevatten
    >>> select_containing(['kaas', 'appel', 'vla'], 'la')
    ['appel', 'vla']
    >>> select_containing(['hallo', 'morgen', 'vroeg'], 'go')
    ['morgen', 'vroeg']
    >>> select_containing([], 'la')
    []
    >>> select_containing(['banaan', 'vriend', 'vla'], '')
    ['banaan', 'vriend', 'vla']
    
    """
    nieuwe_lijst = []
    for woord in words:
        for teken in woord:
            i = 0
            if teken in letters:
                i += 1
            if i = len(letters):
                nieuwe_lijst.append(woord)
                
    return nieuwe_lijst