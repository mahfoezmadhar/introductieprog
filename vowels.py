def remove_vowels(text: str) -> str:
    """
    >>> remove_vowels()
    
    """
    vowel = "aeiou"
    result = ""
    for letter in text:
        if letter not in vowel:
            result += letter
    return result
    
if __name__ == '__main__':
    text = input()
    print(remove_vowels(text))
        