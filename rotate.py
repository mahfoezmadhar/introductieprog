def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    >>> t_lst = [2, 3, 1]
    >>> rotate(t_lst)
    >>> t_lst
    [3, 1, 2]
    
    """
    eerste = 
    for cijfer in range(len(lst)):
        lst[cijfer] = lst[0]
        if cijfer < len(lst) - 1:
            lst[cijfer] = lst[cijfer + 1]
    
    
    