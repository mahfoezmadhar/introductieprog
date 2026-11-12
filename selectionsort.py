def selection_sort(l: list[int]) -> list[int]:
    """
    >>> selection_sort([6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6]
    >>> selection_sort([1, 2, 3])
    [1, 2, 3]
    >>> selection_sort([3, 1, 3, 2, 1])
    [1, 1, 2, 3, 3]
    >>> selection_sort([0, -2, 5, -4])
    [-4, -2, 0, 5]
    >>> selection_sort([7])
    [7]
    
    """
    minimale_waarde = max(i)
    pos = 0
    gesorteerd = ""
    for index in range(len(l)):
        if l[index] < minimale_waarde and l[index] < l[index + 1 and not in gesorteerd:
            minimale_waarde = index
            i += 1
    if minimale_waarde:
        l.insert(pos, minimale_waarde)
        pos += 1
    l.insert(pos, max(l))
    return l
    
            
        