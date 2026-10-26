def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
      
    """
    result= coffee * 90 + tea * 45 + energy * 80 + cola * 40
    return result

if __name__ == '__main__':
    int(input(hoeveel koppen coffee?: ))
    int(input(hoeveel koppen thee?: )) 
    int(input(hoeveel energiedrankjes?: ))
    int(input(hoeveel glazen cola?: ))
    result= coffee * 90 + tea * 45 + energy * 80 + cola * 40
    print(f"je krijgt {result} mg cafeïne binnen.")