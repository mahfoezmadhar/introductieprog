def count_coins(cents: int) -> int:
  
    aantal = 0
    while cents >= 25:
        cents -= 25 
        aantal += 1
    while cents >= 10:
        cents -= 10 
        aantal += 1 
    while cents >= 5:
        cents -= 5 
        aantal += 1 
    while cents >= 1:
        cents -= 1 
        aantal += 1
    return aantal
    

if __name__ == '__main__':
    cents = round(float(input("Hoeveel wisselgeld? ")) * 100)
    while cents <= 0:
      cents = round(float(input("Hoeveel wisselgeld? ")) * 100)
    print(count_coins(cents))
      
        
        