def chunk(lst: list[int], n: int) -> none:
    """
    >>> chunk([1, 2, 3, 4, 5, 6], 2)
    [[1, 2], [3, 4], [5, 6]]
    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk([8, 9], 1)
    [[8], [9]]
    
    """
    nieuwe_lijst = []

    for i in range(0, len(lst), n):
        groepje = []
        j = i

        while j < i + n and j < len(lst):
            groepje.append(lst[j])
            j += 1

        nieuwe_lijst.append(groepje)

    return nieuwe_lijst
    
    
    