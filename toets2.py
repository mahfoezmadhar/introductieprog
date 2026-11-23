#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    Veel succes met de tussentoets!  Jij kunt dit. :)
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#        ____
#       / . .\
#       \  ---<     "Sssssuccces!"
#        \  /
#      __/ /
#     (___/
#
# Even rustig ademhalen, begin bij de vraag die je het
# makkelijkst vindt (vraag 1), en druk vaak op de knoppen
# om te checken.
#
# Let op: bij vraag 5 mag je `in` wel gebruiken.





def split_capitalized(strs: list[str]) -> list[list[str]]:
    """
    geeft eerst de list met hoofdletter dan de list met kleine letter
    
    >>> split_capitalized(['Amsterdam', 'fiets', 'Utrecht', ''])
    [['Amsterdam', 'Utrecht'], ['fiets', '']]
    >>> split_capitalized(['hallo', 'fiets', 'niks', ''])
    [[], ['hallo', 'fiets', 'niks', '']]
    >>> split_capitalized([''])
    [[], ['']]
    >>> split_capitalized(['Johan', 'Ruud', 'Almere', 'Amstelveen'])
    [['Johan', 'Ruud', 'Almere', 'Amstelveen'], []]
    >>> split_capitalized(['ABC', 'aBC'])
    [['ABC'], ['aBC']]
    
    
    
    """
    
    hoofdletter = []
    kleine = []
    teller = 0
    for letter in strs:
        if letter not strs.lower():
            teller += 1
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

is_hoofdletter = []
    is_geen = []
    for woord in strs:
        aantal = 0
        for letter in woord:
            if letter.isupper():
                aantal += 1
        if aantal >= 1:
            is_hoofdletter.append(woord)
        else:
            is_geen.append(woord)
    return [is_hoofdletter, is_geen]
    
    
    
def peak_positions(values: list[int]) -> list[int]:
    """
    geeft een list met de posities van de toppenn
    
    >>> peak_positions([120, 135, -31, 49])
    [1, 3]
    >>> peak_positions([120, 120, 150, 151])
    [151]
    >>> peak_positions([2])
    2
    >>> peak_positions([2, 2])
    []
    
    
    
    """
    nieuwe_lijst = []
    if values[0] > values[1] or values[len(values) - 1] > values[ - 2]:
        nieuwe_lijst.append(0)
        nieuwe_lijst.append(len(values) - 1)
    
    for pos in range(1, len(values) - 1):
        for index in range(pos - 1, pos + 2):
            if(
                values[pos] > values[pos - 1] 
                and values[pos] > values[pos + 1]
            ):
                nieuwe_lijst.append(pos)
    return nieuwe_lijst
    
    
    
    
def repeat_chars(s: str, counts: list[int]) -> str:
    """
    nieuwe string met teken herhaald met de factor counts uit die list
    >>> repeat_chars('abcde', [2, 0, 3])
    'aacccde'
    >>> repeat_chars('', [2, 0, 3])
    ''
    >>> repeat_chars('waner', [1, 1, 2, 2])
    'wanneer'
    >>> repeat_chars('hallo', [])
    'hallo'
    
    
    
    
    """
    nieuw_woord = ''
    if s == '':
        return nieuw_woord
    for index in range(len(counts)):
        i = 0
        while i < counts[index]:
            nieuw_woord = nieuw_woord + s[index]
            i += 1
    for index in range(len(counts), len(s)):
        nieuw_woord += s[index]
    return nieuw_woord
    


def reverse_long_words(sentence: str, n: int) -> str:
    """
    draait worden om als langer dan n letters
    
    >>> reverse_long_words('dit is een lange zin.', 3)
    'dit is een egnal zin'
    >>> reverse_long_words('hoe gaat het.', 0)
    'eoh taag teh'
    >>> reverse_long_words('', 2)
    ''
    >>> reverse_long_words('dit.', 2)
    'tid'
    
    
    """
    
    teller = 0
    nieuw_woordrev = ''
    nieuw_woord = ''
    nieuw_zin = ''
    for index in range(len(sentence)):
        if sentence[index] not in " .":
            teller += 1
            nieuw_woordrev = sentence[index] + nieuw_woordrev
            nieuw_woord += sentence[index]
            
        else:
            if teller > n:
                if index == 0:
                    nieuw_zin += nieuw_woordrev
                    
                else:
                    nieuw_zin += ' ' + nieuw_woordrev
            else:
                if index == 0:
                    nieuw_zin += nieuw_woord
                    
                else:
                    nieuw_zin += ' ' + nieuw_woord
                
            nieuw_woord = ''
            nieuw_woordrev = ''
            teller = 0
            
    return nieuw_zin
    
    
    
def select_containing(words: list[str], letters: str) -> list[str]:
    """
    geef alleen de words terug die de letters bevatten
    >>> select_containing(['kaas', 'appel', 'vla'], 'la')
    ['appel', 'vla']
    >>> select_containing(['hallo', 'morgen', 'vroeg'], 'go')
    ['morgen', 'vroeg']
    >>> select_containing([], 'la')
    []
    >>> select_containing(['banaan', 'vriend', 'vla'], '')
    ['banaan', 'vriend', 'vla']
    
    """
    nieuwe_lijst = []
    for woord in words:
        for teken in range(len(letters)):
            if letters[teken] in woord:
                nieuwe_lijst.append(woord)
    return nieuwe_lijst