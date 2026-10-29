def get_positive_int() -> int:
    """
    
    """
    result = int(input("enter a positive integer number: "))
    while result < 0:
        result = int(input("enter a positive integer number: "))
    return result
    
def get_any_int_but_0() -> int:
    """
    
    """
    result= int(input("enter a number except zero: "))
    while result == 0:
        result= int(input("enter a number except zero: "))
    return result

    
def get_min_int(minimum: int) -> int:
    """
    
    """
    result = int(input("enter a number: "))
    while result < minimum:
        result = int(input("enter a number: "))
    return result
    
    
def get_two_different_ints() -> tuple[int, int]:
    a = int(input("kies een getal uit: "))
    b = int(input("kies nog een getal uit: "))
    while a == b:
        a = int(input("kies een getal uit: "))
        b = int(input("kies nog een getal uit: "))
    return a, b
        
        
    
        


if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()