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
    aantal_letters = 0
    aantal_woorden = 0
    aantal_zinnen = 0
    for letter in text:
        if letter.isalpha() == True or letter == "'":
            aantal_letters += 1
            return aantal_letters
    for woorden in text:
        if woorden == " ":
            aantal_woorden += 1
            return aantal_woorden
    for zinnen in text:
        if zinnen == "." or zinnen == "?" or zinnen == "!":
            aantal_zinnen += 1
            return aantal_zinnen
    return round(coleman_liau(words, sentences, letters) + 0.5)
            
            
        

def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    """
    words = aantal_woorden
    sentences = aantal_zinnen
    letters = aantal_letters
    L = 100 * (letters / words)
    S = 100 * (sentences / words)
    CLI = 0.0588 * L - 0.296 * S - 15.8
    return CLI
    
if __name__ == '__main__':
    text = input()
    print(f"Grade ")
    
    