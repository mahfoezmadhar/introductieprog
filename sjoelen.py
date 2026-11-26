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
    nieuw_board = []
    board_kwartet = []
    board_normaal = []
    count = 0
    for teken in board:
        if teken == 0:
            count += 1
    if count >= 1:
        board_normaal.append(board)
    else:
        board_kwartet.append(board)
    
    if board_normaal:
        a = board_normaal[0] * 2
        b = board_normaal[1] * 3
        c = board_normaal[2] * 4
        d = board_normaal[3] * 1
        return a + b + c + d
    
    if board_kwartet:
        
        a = min(board_kwartet)
        ab = min(board_kwartet) * 20
        b = (board_kwartet[0] - a) * 2
        c = (board_kwartet[1] - a) * 3
        d = (board_kwartet[2] - a) * 4
           e = (board_kwartet[3] - a) * 1
        return ab + b + c + d + e
        
        
        
            
        
            
            
            
        
    
    
    
    
    