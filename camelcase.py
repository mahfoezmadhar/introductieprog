def convert_snakecase(text: str):
    """
    
    """
    result = ""
    for letter in text:
        result += letter
        if letter.isupper() == True:
            result += "_" + letter
    return result
    
if __name__ == '__main__':
    text = input()
            