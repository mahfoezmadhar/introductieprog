def calculate_points(board: list[int]) -> int:
    """
    >>> calculate_points([0, 0, 0, 0])
    0
    >>> calculate_points([1, 2, 3, 0])
    20
    >>> calculate_points([1, 1, 1, 1])
    20
    >>> calculate_points([3, 4, 3, 5])
    65
    """

    count = 0
    for teken in board:
        if teken == 0:
            count += 1
    if count >= 1:
        a = board[0] * 2
        b = board[1] * 3
        c = board[2] * 4
        d = board[3] * 1
        return a + b + c + d
    else:
        a = min(board)
        ab = min(board) * 20
        b = (board[0] - a) * 2
        c = (board[1] - a) * 3
        d = (board[2] - a) * 4
        e = (board_kwartet[3] - a) * 1
        return ab + b + c + d + e
    
        
        
        
            
        
            
            
            
        
    
    
    
    
    