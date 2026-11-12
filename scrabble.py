POINTS = [1, 3, 3,  2, 1, 4, 2, 4, 1, 8, 5, 1,  3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def compute_score(word: str) -> int:
    """
    >>> compute_score("code")
    7
    >>> compute_score("CoDe")
    7
    >>> compute_score("pizza")
    25
    """
    totale_waarde = 0
    for letter in word:
        letter = compute_letter_score(letter)
        
       
       
       
       
       
       
        ##for letterwaarde in range(1, len(POINTS) + 1):
            ##letter = 
    
    
    
    
    
    
    
    

def compute_letter_score(letter: str) -> int:
    """
    >>> compute_letter_score("a")
    1
    >>> compute_letter_score("b")
    3
    >>> compute_letter_score("z")
    10
    >>> compute_letter_score("Z")
    10
    
    """
    letter = letter
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            letter = i 
    return letter

if __name__ == '__main__':
    <Hoofdprogramma>