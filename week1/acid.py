def is_acidic(ph : float) -> bool:
  
    """
    >>> is_acidic(7.5)
    False
    >>> is_acidic(2)
    True
    
    """
    if ph < 7.0:
     return True
    else:
     return False 
    
    
    

if __name__ == '__main__':
    ph = float(input("geef een pH-waarde: "))
    if is_acidic(ph) == True:
        print("Het is een zuur")
    else:
        print("Het is een base")
    