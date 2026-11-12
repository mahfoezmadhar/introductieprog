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
        totale_waarde += letter
    return totale_waarde
        
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
    letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            return POINTS[i]
    return 0

if __name__ == '__main__':
    word = input("speler 1: ")
    speler1 = compute_score(word)
    word = input("speler 2: ")
    speler2 = compute_score(word)
    if speler1 > speler2:
        print("Speler 1 wint!")
    elif speler2 > speler1:
        print("Speler 2 wint!")
    else:
        print