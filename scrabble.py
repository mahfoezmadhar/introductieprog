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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, len(alphabet) + 1):
        if letter.lower() == alphabet[i]:
            letter = i 
    return letter.lower()

if __name__ == '__main__':
    <Hoofdprogramma>