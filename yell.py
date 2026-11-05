def yell_verdubbel(text: str) -> str:
    """"
    
    """"
    for teken in text:
        if teken == "?":
            return teken + "?"
        elif teken == "!":
            return teken + "!"
    
    if __name__ == '__main__':
        text = input()