def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.
    """
    for letter in dna.upper():
        if letter not in "ACTG":
            return False
        else:
            return True

def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).
    """
    for reeks in dna.upper():
        if reeks == "A":
            return "u"
        elif reeks == "c":
            return "g"
        elif reeks == ""

if __name__ == '__main__':
    <Hoofdprogramma>