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
    for letters in range(min(len(lst1), len(lst2))):
        nieuwe_lijst.append(lst1[letters])
        nieuwe_lijst

        
    