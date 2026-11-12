def merge_lists(lst1: list[int], lst2: list[int]) -> list:
    """
    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    
    """
    nieuwe_lijst = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            nieuwe_lijst.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            nieuwe_lijst.append(lst2[j])
            j += 1 
        elif lst1[i + 1] == "" and lst1[i] > lst2[j]:
            nieuwe_lijst.append(lst1[i])
        elif lst2[j + 1] == "" and lst2[j] > lst1[i]:
            nieuwe_lijst.append
                
        else:
            nieuwe_lijst.append(lst1[i])
            nieuwe_lijst.append(lst2[j])
            i += 1 
            j += 1
        
    return nieuwe_lijst
            
            
            
    