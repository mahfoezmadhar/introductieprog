def weeks_elapsed(day1: int, day2: int) -> int:
    """
    Berekent het aantal volle weken dat verstreken is tussen twee dagen
    in hetzelfde jaar. De dagen zijn gegeven als dagnummer (day1 en day2).

    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    >>> weeks_elapsed(10, 10)
    0
    >>> weeks_elapsed(1, 27)
    3

    """

    day1 = int(input("Dagnummer 1: "))
    day2 = int(input("Dagnummer 2: "))
    result = abs(day1-day2)//7
    print(f"Er zijn {result} volle weken verstreken.")