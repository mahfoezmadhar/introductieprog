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
        board_kwartet.append()
            
            
            
        
    
    
    
    
    
    
    
    

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
    Trueaantal schijven dat nog over is om nog eens mee te schuiven.
    """

if __name__ == '__main__':
    <Zet het bord klaar, simuleer drie rondes en
     bereken aan het eind het aantal punten op basis van
     de staat van het sjoelbord>