def meal(time: str) -> int | None:
    """
    >>> meal("18:53")
    3
    >>> meal("07:00")
    1
    """
    uur, minuut = time.split(":")
    if int(uur) == 7 or (int(uur:)
        return 1
    if int(uur) >= 12 and int(uur, minuut) <= 13: 
        return 2
    if int(uur) >= 18 and int(uur, minuut) <= 19:
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