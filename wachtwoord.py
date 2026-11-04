def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
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
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.
    """
    for hoofdletter in password:
        if hoofdletter.isupper() == True:
            return True
    for kleineletter in password:
        if kleineletter.islower() == False:
            return True
    return False
    

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """
    for digit in password:
        if digit.isdigit() == True:
            return True
    return False
    

def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.
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