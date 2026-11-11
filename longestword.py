def string_to_list(s: str) -> none:
    """
    >>> string_to_list("Margherita Tutta la Vita")
    ['Margherita', 'Tutta', 'la', 'Vita']
    >>> string_to_list("Hoi")
    ['Hoi']    
    
    """
    nieuwe_lijst = []
    for woord in s:
        if woord not in " ":
            nieuwe_lijst.append(s)
    return nieuwe_lijst



def longest_word_from_list(lst: list[object]) -> str:


def print_banner(s: list[object]) -> str: