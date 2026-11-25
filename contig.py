def contig(lst: list[int]) -> list[int]:


    """
    >>> contig([1, 2, 3, 5, 6, 9])
    [[1, 2, 3], [5, 6], [9]]
    >>> contig([1, 2, 3])
    [[1, 2, 3]]
    >>> contig([1, 3, 5])
    [[1], [3], [5]]
    >>> contig([])
    []
    """
    nieuwe_lijst = []
    deel_lijst = []
    for index in range(len(lst)):
        if index == len(lst)
        if lst[index + 1] - lst[index] == 1:
            deel_lijst.append(lst[index])
        else:
            deel_lijst.append(lst[index])
            nieuwe_lijst.append(deel_lijst)
            deel_lijst = []
    return nieuwe_lijst
            
        
        
    
    
