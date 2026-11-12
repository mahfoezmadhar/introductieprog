def special_sort(l: list[int]) -> list[int]:    
    
    """
    >>> special_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> special_sort([1, 2, 3])
    [1, 2, 3]
    >>> special_sort([3, -2, 0, 3, -2])
    [-2, -2, 0, 3, 3]
    >>> special_sort([7])
    [7]

    """
        for pos in range(len(l) - 1):
        kleinste_index = pos

        for index in range(pos + 1, len(l)):
            if l[index] < l[kleinste_index]:
                kleinste_index = index

        l[pos], l[kleinste_index] = l[kleinste_index], l[pos]
    return l