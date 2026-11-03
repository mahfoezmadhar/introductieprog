def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    """
    uur, minuut = timer.split(":")
    while uur >= 7 and uur <= 8:
        return ontbijt
    while uur >= 12 and uur <= 13:
        return lunch
    while uur >= 18 and uur <= 19:
        return avondeten
    return None
    
        

if __name__ == '__main__':
    time = int(input("Hoe laat is het?: "))
    