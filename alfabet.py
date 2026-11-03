def compare(word1: str, word2: str) -> int:
    """

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
    input("Woord 1: ")
    