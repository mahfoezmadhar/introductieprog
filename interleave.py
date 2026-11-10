def interleave(lst1: list[object], lst2: list[object], keep: bool) -> none:
    """
    >>> interleave([1, 2, 3, 4], [10, 20], False)
    [1, 10, 2, 20]
    >>> interleave([1], [10, 20, 30], True)
    [1, 10, 20, 30]
    >>> interleave([1], [10, 20, 30], False)
    [1, 10]
    >>> interleave([], [10, 20], True)
    [10, 20]
    >>> interleave([], [10, 20], False)
    []
    >>> interleave([], [], True)
    []    
    
    """
    nieuwe_lijst = []
    for letter1 in list1:
        for letter2 in list2:
            nieuwe_lijst.append(letter1 + letter2)
            
        
    