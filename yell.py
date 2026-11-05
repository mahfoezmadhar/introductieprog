def yell_verdubbel(text: str) -> str:
    """
    
    """
    for teken in text:
        if teken == "?":
            print(teken + "?")
        elif teken == "!":
            print(teken + "!")
    return text  
    
if __name__ == '__main__':
    text = input("input: ")
    print(yell_verdubbel(text))