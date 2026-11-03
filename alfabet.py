def compare(word1: str, word2: str) -> int:
    """
    >>> compare(shark, sword)
    -1
    >>> compare()
    """
    for letter1, letter2 in zip(word1, word2):
        letter1 = letter1.lower()
        letter2 = letter2.lower()
        if letter1 > letter2:
            return 1 
        elif letter1 < letter2:
            return -1 
        if len(word1) > len(word2):
            return 1
        elif len(word2) > len(word1):
            return -1
        return 0

if __name__ == '__main__':
    word1 = input("Woord 1: ")
    word2 = input("Woord 2: ")
    if compare(word1, word2) == 1:
        print(f"{word2} first")
    if compare(word1, word2) == -1:
        print(f"{word1} first")
    if compare(word1, word2) == 0:
        print("No need to decide!")
        