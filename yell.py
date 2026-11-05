def yell_verdubbel(text: str) -> str:
    """
    
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
    print(yell_verdubbel(text))