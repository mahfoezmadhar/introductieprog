def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    
    """
    for cijfer in range(len(lst)):
        if cijfer >= len(lst):
            lst[cijfer] = lst[cijfer + 1]
        else:
            lst[cijfer] = lst[0]
    
    
    