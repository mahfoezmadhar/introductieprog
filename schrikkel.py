def is_schrikkel(jaar: int) -> bool:
  """
>>> is_schrikkeljaar(2025)
False
>>> is_schrikkeljaar(2000)
True


  """
  if (jaar % 4 == 0 and jaar % 100 !=0) or jaar % 400 == 0:
    return True
  else:
    return False
  
if __name__ == '__main__':
 jaar = int(input("Voer jaartal in: "))
 if is_schrikkel(jaar) == True:
    print(f"{jaar} is een schrikkeljaar")
 else:
    print(f"{jaar} is geen schrikkeljaar")
    