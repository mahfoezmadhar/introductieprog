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
    minimale_waarde = max(l)
    pos = 0
    index = 0
    gesorteerd = []
    while index < len(l):
        if l[index] <= minimale_waarde and l[index] < l[index + 1] and l[index] not in gesorteerd:
            minimale_waarde = l[index]
            index += 1
        else: 
    if minimale_waarde:
        l.insert(pos, minimale_waarde)
        pos += 1
        gesorteerd.append(minimale_waarde)
        minimale_waarde = ""
        
    l.insert(pos, max(l))
    return l
    
            
        