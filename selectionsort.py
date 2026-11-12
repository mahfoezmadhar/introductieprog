def selection_sort(l: list[int]) -> list[int]:
    """
    >>> selection_sort([6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6]
    
    """
    minimale_waarde = max(i)
    pos = 0
    gesorteerd = ""
    for index in range(len(l)):
        if index < minimale_waarde and index < index + 1 and not in gesorteerd:
            minimale_waarde = index
            i += 1
    if minimale_waarde:
        l.insert(pos, minimale_waarde)
        pos += 1
    return l
    
            
        