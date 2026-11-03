def meal(time: str) -> str | None:
    """
    >>> meal(time) 
    
    """
    uur, minuut = time.split(":")
    uur = int(uur)
    minuut = int(minuut)
    while uur >= 7 and uur <= 8:
        return 1
    while uur >= 12 and uur <= 13:
        return 2
    while uur >= 18 and uur <= 19:
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