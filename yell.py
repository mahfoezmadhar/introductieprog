def yell_verdubbel(text: str) -> str:
    """
    
    """
    leesteken = "!, ?"
    result = ""
    for teken in text:
        if teken not in leesteken:
            result += teken
    return result
    
if __name__ == '__main__':
    text = input("input: ")
    print(yell_verdubbel(text))