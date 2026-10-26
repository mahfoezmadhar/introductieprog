def travel_costs(km: int) -> float:
    """
    >>> travel_costs(1250)
    325
    >>> travel_costs(800)
    208
    """
    return km * 0.13 * 2

def overnight_costs(nights: int) -> float:
    """
    >>> overnight_costs(5)
    300
    >>> overnight_costs(7)
    420
    """
    return nights * 60

def total_costs(km: int, nights: int) -> int:
    """
    >>>total_costs(1250, 5)
    625
    >>> total_costs(800, 10)
    
    """
    result = (overnight_costs(nights) + travel_costs(km))
    return round(result)

if __name__ == '__main__':
 km = int(input("hoever ga je weg in kilometers?: "))
 nights= int(input("hoeveel nachten is je verblijf?: "))
 result= total_costs(km, nights)
 print(f"jouw vakantie kost: {result}")