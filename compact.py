def compact(lst: list[object]) -> none:
    """
    
    """
    nieuwe_lijst = []
    x = []
    for letter in lst:
        if not x:
            nieuwe_lijst.append(letter)
    return nieuwe_lijst
            
            
            