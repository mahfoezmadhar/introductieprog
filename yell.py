def yell_verdubbel(text: str) -> str:
    """
    
    """
    for teken in text:
        if teken == "?":
            return teken + "?"
        elif teken == "!":
            return t + "!"
    
if __name__ == '__main__':
    text = input("input: ")
    print(yell_verdubbel(text))