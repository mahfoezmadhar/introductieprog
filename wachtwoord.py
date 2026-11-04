def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
    """
    count = 0
    for char in password:
        count += 1
    if char >= 8:
        return True
    else:
        return False

def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.
    """
    i = 0
    while i < len(password):
        letter = password[i]
        if letter.isupper == True:
            return True
        else: 
            return False
        elif letter.islower == True:
            return True
        else:
            return False
        i += 1

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """
    i = 0
    while i < len(password):
        letter = password[i]
        if letter.isdigit == True:
            return True
        else:
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
    <Hoofdprogramma mag maar één functie aanroepen>
    input("Geef een wachtwoord: ")
    if 