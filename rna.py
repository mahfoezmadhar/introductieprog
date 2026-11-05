def check_input(dna: str) -> bool:
    """
    >>> check_input("ACTG")
    True
    >>> check_input("aCtG")
    True
    >>> check_input("XCTG")
    False
    >>> check_input("ACXG")
    False
    """
    for letter in dna.upper():
        if letter not in "ACTG":
            return False
    return True

def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).
    """
    result = ""
    for reeks in dna.upper():
        if reeks == "A":
            result += "U"
        elif reeks == "C":
            result += "G"
        elif reeks == "T":
            result += "A"
        else:
            result += "C"
    return result

if __name__ == '__main__':
    dna = input("DNA: ")
    if check_input(dna) == True:
        print(f"RNA: {transcribe_dna_to_rna(dna)}")
    else:
        print("That is not a valid DNA string")