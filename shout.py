def shout(text: str) -> str:
    """
    shout()
    
    """
    return text.upper()
    
if __name__ == '__main__':
    text = input()
    print(shout(text))