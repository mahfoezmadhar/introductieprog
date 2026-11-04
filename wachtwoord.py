def check_length(password: str) -> bool:
    """
    >>> check_length("1234567")
    False
    >>> check_length("12345678")
    True
    >>> check_length("")
    False
    """
    count = 0
    for char in password:
        count += 1
    if count >= 8:
        return True
    else:
        return False

def check_letter(password: str) -> bool:
    """
    >>> check_letter("Abc")
    True
    >>> check_letter("abc")
    False
    """
    bevathoofdletter = False
    bevatkleineletter = True
    for hoofdletter in password:
        if hoofdletter.isupper() == True:
            return bevathoofdletter
    for kleineletter in password:
        if kleineletter.islower() == False:
            return bevatkleineletter
    return bevathoofdletter and bevatkleineletter
    

def check_number(password: str) -> bool:
    """
    >>> check_number("abc1")
    True
    >>> check_number("abcdef")
    False
    """
    for digit in password:
        if digit.isdigit() == True:
            return True
    return False
    

def check_password(password: str) -> bool:
    """
    >>> check_password("Abcdefg1")
    True
    >>> check_password("Abcdef1")
    False
    """
    if (
        check_length(password) == True and check_letter(password) == True
        and check_number(password) == True
    ):
        return True
    else:
        return False
        
        
        

if __name__ == '__main__':
    password = input("Geef een wachtwoord: ")
    if check_password(password) == True:
        print("Het gegeven wachtwoord is valide.")
    else:
        print("Het gegeven wachtwoord is niet valide.")