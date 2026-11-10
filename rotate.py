def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    
    """
    for cijfer in range(len(lst)):
        if cijfer < len(lst) - 1:
            lst[cijfer] = lst[cijfer + 1]
    lst[cijfer] = lst[0] + 1
    
    
    