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

def shuffle_round(board: list[int], discs: int) -> int:
    """
    Simuleert een enkele ronde sjoelen. De variable `board` wordt
    aangepast als er een schijf in een gleuf terecht komt. Returnt
    het aantal schijven dat nog over is om nog eens mee te schuiven.
    """

if __name__ == '__main__':
    <Zet het bord klaar, simuleer drie rondes en
     bereken aan het eind het aantal punten op basis van
     de staat van het sjoelbord>