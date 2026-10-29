def is_schrikkeljaar(jaar: int) -> bool
"""


"""
if (jaar % 4 == 0 and jaar % 100 !=0) or jaar % 400 = 0:
  return True
else:
  return False
  
if __name__ == '__main__':
int(input("Voer jaartal in: "))
if is_schrikkeljaar(jaar) == True:
    print('D')