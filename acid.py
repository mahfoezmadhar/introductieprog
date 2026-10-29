def is_acidic(ph : float) -> bool:
   if ph < 7.0: 
    return true
    else:
     return false 
    

if __name__ == '__main__':
    ph = float(input("geef een pH-waarde: "))
    