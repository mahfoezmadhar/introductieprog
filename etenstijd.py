def meal(time: str) -> int | None:
    """
    >>> meal("18:53")
    3
    >>> meal("07:00")
    1
    """
    uur, minuut = time.split(":")
    if int(uur) == 7 or (int(uur) == 8 and int(minuut) == 0):
        return "ontbijt"
    if int(uur) == 12 or (int(uur) == 13 and int(minuut) == 0): 
        return "lunch"
    if int(uur) == 18 or (int(uur) == 19 and int(minuut) == 0):
        return 3
    return None
    
        

if __name__ == '__main__':
    time = input("Hoe laat is het?: ")
    if meal(time) == 1:
        print("Het is tijd voor ontbijt")
    if meal(time) == 2:
        print("Het is tijd voor lunch")
    if meal(time) == 3:
        print("Het is tijd voor avondeten")
    else:
        print(" ")