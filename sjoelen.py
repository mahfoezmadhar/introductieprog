import random
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
        e = (board[3] - a) * 1
        return ab + b + c + d + e
        
        
def shuffle_round(board: list[int], discs: int) -> int:
    """
    >>> board = [0, 0, 0, 0]
    >>> shuffle_round(board, 0)
    0
    >>> board
    [0, 0, 0, 0]

    >>> board = [0, 0, 0, 0]
    >>> over = shuffle_round(board, 1)
        >>> 0 <= over <= 1 and sum(board) + over == 1
    True

    >>> board = [0, 0, 0, 0]
    >>> over = shuffle_round(board, 30)
    >>> 0 <= over <= 30 and sum(board) + over == 30
    True

    >>> board = [2, 1, 0, 3]
    >>> over = shuffle_round(board, 10)
    >>> 0 <= over <= 10 and sum(board) + over == 16
    True
    """












if __name__ == '__main__':
    <Zet het bord klaar, simuleer drie rondes en
     bereken aan het eind het aantal punten op basis van
     de staat van het sjoelbord>
    
        
        
        
            
        
            
            
            
        
    
    
    
    
    