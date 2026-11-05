def convert(text: str) -> str:
    """
    >>> convert("winkelWagen")
    'winkel_wagen'
    >>> convert("intInput")
    'int_input'
    
    """
    result = ""
    for letter in text:
        if letter.isupper() == True:
            result += "_" + letter.lower()
        else:
            result += letter
    return result
    
if __name__ == '__main__':
    text = input("camelCase: ")
    print(f"snake_case: {convert(text)}")
            