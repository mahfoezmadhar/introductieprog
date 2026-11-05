def yell_verdubbel(text: str) -> str:
    """
    
    """
    for teken in text:
        if teken == "?":
            return text + "?"
        elif teken == "!":
            return text + "!"
    return text  
    
if __name__ == '__main__':
    text = input("input: ")
    print(yell_verdubbel(text))