def merge_lists(lst1: list[int], lst2: list[int]) -> list:
    """
    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    >>> merge_lists([2], [1, 4, 7])
    [1, 2, 4, 7]
    >>> merge_lists([-5, -1, 3], [-3, 0, 2])
    [-5, -3, -1, 0, 2, 3]
    >>> merge_lists([2, 2], [2, 2])
    [2, 2, 2, 2]
    >>> merge_lists([], [1, 2])
    [1, 2]
    >>> merge_lists([1, 2], [])
    [1, 2]
    
    """
    nieuwe_lijst = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            nieuwe_lijst.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            nieuwe_lijst.append(lst2[j])
            j += 1 
        else:
            nieuwe_lijst.append(lst1[i])
            nieuwe_lijst.append(lst2[j])
            i += 1 
            j += 1
    for 
        
    return nieuwe_lijst
            
            
            
    