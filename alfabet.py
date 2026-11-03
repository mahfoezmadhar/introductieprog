def compare(word1: str, word2: str) -> int:
    """
    >>> compare("shark", "sword")
    -1
    >>> compare("taylor", "lana")
    1
    """
    for i < len(word1) and i < len(word2)

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
        