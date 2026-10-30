def print_piramide(aantal: int) -> None:
    """
    >>> print_piramide(1)
    ##
    >>> print_piramide(2)
     ##
    ###
    """
    for rij in range(1, aantal + 1):
        for spatie in range(aantal - rij):
            print(' ', end='')

        for hekje in range(rij + 1):
            print('#', end='')

        print()


if __name__ == '__main__':
    aantal = int(input("Hoe hoog moet de piramide zijn? "))
    print_piramide(aantal)


    
    
    