def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    """
    while cents >= 25:
        cents -= 25 
        aantal25 += 1
    while cents >= 10:
        cents -= 10 
        aantal10 += 1 
    while cents >= 5:
        cents -= 5 
        aantal5
    while cents >= 1:
        aantal1 = cents // 1
    return aantal25 + aantal10 + aantal5 + aantal1
    

if __name__ == '__main__':
    cents = round(float(input("Hoeveel wisselgeld? ")) * 100)
    while cents <= 0:
      cents = round(float(input("Hoeveel wisselgeld? ")) * 100)
    print(count_coins(cents))
      
        
        