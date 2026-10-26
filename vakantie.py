def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten op basis van de te rijden afstand
    naar de accomodatie (tel `km` twee keer voor heen en terug).
    """
    return km * 0.13

def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten op basis van het aantal nachten
    dat je op vakantie gaat.
    """
    return nights * 0.60

def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale kosten op basis van de afstand en het aantal
    nachten en rondt af naar hele euro's.
    Deze functie delegeert zoveel mogelijk werk naar de andere
    twee functies (roep die dus hier aan).
    """
    result = int(overnight_costs * 0.60 + travel_costs * 0.13)
    return result

if __name__ == '__main__':
 travel_costs= int(input("hoever ga je weg in kilometers?: "))
 overnight_costs= int(input("hoeveel nachten is je verblijf?: "))
 result= int(overnight_costs * 0.60 + travel_costs)
 print(f"jouw vakantie kost: {result}")