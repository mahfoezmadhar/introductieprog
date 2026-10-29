def is_acidic(ph : float) -> bool:
  
    """
    >>>is_acidic(7.5)
    true
    >>>is_acidic(2)
    false
    
    """
    if ph < 7.0:
     return True
    else:
     return False 
    
    
    

if __name__ == '__main__':
    ph = float(input("geef een pH-waarde: "))
    if is_acidic == True:
        print("het is een zuur")
    else:
        print("het is een base")
    