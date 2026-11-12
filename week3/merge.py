def merge_lists(lst1: lst[int], lst2: lst[int]) -> lst:
    """
    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    
    """
    nieuwe_lijst = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            nieuwe_lijst.append(lst1[i])
            i += 1
        elif lst[i]
            
            
    