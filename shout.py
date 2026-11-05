def shout(text: str) -> str:
    """
    >>> shout("hallo hoe gaat het met je?")
    'HALLO HOE GAAT HET MET JE?'
    >>> SHOUT()
    
    
    """
    return text.upper()
    
if __name__ == '__main__':
    text = input()
    print(shout(text))