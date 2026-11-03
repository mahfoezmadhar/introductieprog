def meal(time: str) -> str | None:
    """
    >>> meal("18:53")
    "avondeten"
    >>> meal("07:00")
    "ontbijt"
    """
    uur, minuut = time.split(":")
    if int(uur) == 7 or (int(uur) == 8 and int(minuut) == 0):
        return "ontbijt"
    if int(uur) == 12 or (int(uur) == 13 and int(minuut) == 0): 
        return "lunch"
    if int(uur) == 18 or (int(uur) == 19 and int(minuut) == 0):
        return "avondeten"
    return None
    
        

if __name__ == '__main__':
    time = input("Hoe laat is het?: ")
    if meal(time) == 1:
        print("Het is tijd voor ontbijt")
    elif meal(time) == 2:
        print("Het is tijd voor lunch")
    if meal(time) == 3:
        print("Het is tijd voor avondeten")
    else:
        print(" ")