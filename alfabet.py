def compare(word1: str, word2: str) -> int:
    """

    """
    for letter1, letter2 in zip(word1, word2):
        letter1 = letter1.lower()
        letter2 = letter2.lower()
        if letter1 > letter2:
            return letter

if __name__ == '__main__':
    <Hoofdprogramma>