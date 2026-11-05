def yell(text: str) -> str:
    """
    >>> yell("hallo! wereld?")
    'hallo!! wereld??'
    >>> yell("hallo wereld")
    'hallo wereld'
    >>> yell_verdubbel("")
    ''
    """
    leesteken = "!?"
    result = ""
    for teken in text:
        result += teken
        if teken in leesteken:
            result += teken
    return result
    
if __name__ == '__main__':
    text = input()
    print(yell(text))