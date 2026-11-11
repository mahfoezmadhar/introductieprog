def string_to_list(s: str) -> none:
    """
    >>> string_to_list("Margherita Tutta la Vita")
    ['Margherita', 'Tutta', 'la', 'Vita']
    >>> string_to_list("Hoi")
    ['Hoi']
    
    """
    nieuwe_lijst = []
    woord_lijst = ""
    for i in range(len(s)):
        if s[i] not in " ":
            woord_lijst += s[i]
        else:
            nieuwe_lijst.append(woord_lijst)
            woord_lijst = ""
    if woord_lijst:
        nieuwe_lijst.append(woord_lijst)

    return nieuwe_lijst
            
        



def longest_word_from_list(nieuwe_lijst: list[object]) -> str:
    """
    >>> longest_word_from_list(["la", "Margherita", "Vita"])
    'Margherita'
    >>> longest_word_from_list(["kat"])
    'kat'   
    
    """
    langste_woord = ""
    for i in nieuwe_lijst:
        if len(i) > len(langste_woord):
            langste_woord = i
    return langste_woord
            


###def print_banner(s: list[object]) -> str: