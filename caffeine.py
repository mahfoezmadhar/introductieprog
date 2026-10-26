def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeine op basis van de hoeveelheid gedronken
      drankjes van het type koffie, thee, energie, en cola.
    >>> calculate_cafeine(2, 4, 0, 0)
    360
    >>> calculate_cafeine(1, 0, 0, 0)
    90 
    """
    result= coffee * 90 + tea * 45 + energy * 80 + cola * 40
    return result

if __name__ == '__main__':
  coffee= int(input("hoeveel koppen coffee?: "))
    tea= int(input("hoeveel koppen thee?: ")) 
    energy= int(input("hoeveel energiedrankjes?: "))
    cola= int(input("hoeveel glazen cola?: "))
    result= coffee * 90 + tea * 45 + energy * 80 + cola * 40
    print(f"je krijgt {result} mg cafeïne binnen.")