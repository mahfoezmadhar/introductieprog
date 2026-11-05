remove_vowels(text: str) -> str:
    """
    
    """
    vowel = "aeiou"
    for letter in text:
        if letter not in text:
            result += letter
    
        