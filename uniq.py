def uniq(lst: list[object]) -> none:
    """
    
    
    """
    nieuwe_lijst = []
    for letter in range(len(lst) - 1):
        if lst[letter] == lst[letter + 1]:
            