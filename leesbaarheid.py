def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    
    """
    letters = 0
    words = 0
    sentences = 0
    for letter in text:
        if letter.isalpha() == True:
            letters += 1
    for woorden in text:
        if woorden == " ":
            words += 1
    for zinnen in text:
        if zinnen == "." or zinnen == "?" or zinnen == "!":
            sentences += 1
    return round(coleman_liau(words, sentences, letters) + 0.5)
            
            
        

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    """
    L = 100 * (letters / words)
    S = 100 * (sentences / words)
    CLI = 0.0588 * L - 0.296 * S - 15.8
    return CLI
    
if __name__ == '__main__':
    text = input()
    if calculate_grade(text) >= 16:
        print("Grade 16+")
    elif calculate_grade(text) < 1:
        print("Below Grade 1")
    else:
        print(f"Grade {calculate_grade(text)}")
    
    