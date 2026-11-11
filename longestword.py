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
    if woord_lijs

    return nieuwe_lijst
            
        



###def longest_word_from_list(lst: list[object]) -> str:


###def print_banner(s: list[object]) -> str: