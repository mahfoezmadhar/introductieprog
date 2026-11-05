def convert_snakecase(text: str):
    """
    >>> convert_snakecase("winkelWagen")
    
    
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
    print(f"snake_case: {convert_snakecase(text)}")
            