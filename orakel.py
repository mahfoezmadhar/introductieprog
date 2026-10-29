def check_answer(answer: str) -> bool:
    """
    >>> check_answer(42)
    True
    >>> check_answer(100)
    False
    """
    if answer == 42 or answer == tweeenveertig or answer == tweeënveertig:
        return True
    else:
        return False

if __name__ == '__main__':
    answer = str(input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?: "))
    if check_answer(answer) == 42 or check_answer(answer) == tweeenveertig or check_answer(answer) == tweeënveertig:
        print("ja")
    else:
        print("")
    