def remove_vowels(text: str) -> str:
    """
    
    """
    vowel = "aeiou"
    result = ""
    for letter in text:
        if letter not in text:
            result += letter
    return result
    
    if __name__ == '__main__':
        text = input("input: ")
        print(remove_vowels(text))
        