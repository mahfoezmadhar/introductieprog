def shout(text: str) -> str:
    """
    >>> shout("hallo hoe gaat het met je?")
    'HALLO HOE GAAT HET MET JE?'
    >>> shout("ik studeer ki")
    'IK STUDEER KI'
    
    """
    for letter in text:
        result += letter.upper()
    return result
    
if __name__ == '__main__':
    text = input()
    print(shout(text))