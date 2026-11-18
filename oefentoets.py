# Veel succes! Schrijf hieronder je functies
# en gebruik de knoppen voor checks!

def split_by_parity(ints: list[int]) -> list[list[int]]:
    """
    >>> split_by_parity([1, 2, 3, 4, 5])
    [[2, 4], [1, 3, 5]]
    >>> split_by_parity([-2, -1, 0 , 1, 2, 3])
    [[0, 2], [1, 3]]
    >>> split_by_parity([-5, -4, -3, -2, 2])
    [[2], []]
    >>> split_by_parity([1, 2, 5, 6, 7])
    [[2, 6], [1, 5, 7]]
    
    """
    even = []
    oneven = []
    for teken in ints:
        if teken % 2 == 0 and teken >= 0:
            even.append(teken)
        elif teken % 2 != 0 and teken >= 0:
            oneven.append(teken)
    return [even, oneven]
    
    
def reading_level(s: str) -> float:
    """
    >>> reading_level("mijn naam is pim")
    9.75
    
    
    """
    
    aantal_medeklinkers = 0
    aantal_klinkers = 0
    aantal_woorden = 1
    
    for teken in s:
        if teken.lower() in "aeiou":
            aantal_klinkers += 1
        elif teken.lower() in " ":
            aantal_woorden += 1
        else:
            aantal_medeklinkers += 1
        
    gemiddelde_woordlengte= (aantal_medeklinkers + aantal_klinkers) / (aantal_woorden)
            
    return round((aantal_medeklinkers - aantal_klinkers) * gemiddelde_woordlengte, 2)
        
        
        


def longest_word_length(s: str) -> str:
    """
    >>> longest_word_length("ik ga naar de winkels")
    7
    
    """
    teller_langstewoord = 0
    teller = 0
    for teken in s:
        if s not in " ":
            teller += 1
        else:
            if teller > teller_langstewoord:
                teller_langstewoord = teller
                teller = 0
        
    
    
    
    
    
    
def vowely_words(words: list[str]) -> list[str]:
    """
    >>> vowely_words(['aap', 'noot', 'mies'])
    ['aap', 'noot', 'mies']
    
    """
    aantal_klinkers = 0
    nieuwe_lijst = []
    
    for woord in words:
        for teken in woord:
            if teken in "AEIOUaeiou":
                aantal_klinkers += 1
        if aantal_klinkers >= 2:
            nieuwe_lijst.append(woord)
    return nieuwe_lijst
    
    
    
def encrypt(s: str) -> str:
    """
    >>> encrypt("abc")
    'zyx'
    >>> encrypt("abcdefghijklmnopqrstuvwxyz")
    'zyxwvutsrqponmlkjihgfedcba'
    >>> encrypt("")
    ''
    >>> encrypt("hallo")
    'szool'
    
    
    
    """
    beveiligd = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for teken in range(len(s)):
        for letter in range(len(alphabet)):
            if s[teken] == alphabet[letter]:
                nieuwe_letter = alphabet[25 - letter]
                beveiligd += nieuwe_letter
    return beveiligd
            
            
        
            
            
        
        
        
        
            
        
            
        
