def yell_verdubbel(text: str) -> str:
    """dtttteqq
    
    """
    for teken in text:
        if teken == "?":
            return teken + "?"
        elif teken == "!":
            return teken + "!"
    
    if __name__ == '__main__':
        text = input()
        print(yell_verdubbel(text))