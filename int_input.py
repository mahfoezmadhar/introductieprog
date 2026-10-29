def get_positive_int(n: int) -> int:
    """
    
    """
    result = int(input("enter a positive integer number: "))
    while result < 0:
        result = int(input("enter a positive integer number: "))
    return result
    
def get_any_int_but_0(n: int) -> int:
    """
    
    """
    result= int(input("enter a number except : "))















if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()