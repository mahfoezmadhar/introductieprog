def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    """
    uur, minuut = time.split(":")
    while int(uur) >= 7 and uur <= 8:
        return ontbijt
    while int(uur >= 12 and uur <= 13:
        return lunch
    while uur >= 18 and uur <= 19:
        return avondeten
    return None
    
        

if __name__ == '__main__':
    time = input("Hoe laat is het?: ")
    if meal(time) == ontbijt:
        print("Het is tijd voor ontbijt")
    if meal(time) == lunch:
        print("Het is tijd voor lunch")
    if meal(time) == avondeten:
        print("Het is tijd voor avondeten")
    print(" ")