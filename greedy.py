def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    """
    while cents => 25:
        aantal25 = cents // 25
    while cents => 10:
        aantal10 = cents // 10 
    while cents => 5:
        aantal5 = cents // 5 
    while cents => 1:
        aantal1 = cents // 1
    return aantal25 + aantal10 + aantal5 + aantal1
    

if __name__ == '__main__':
    <Vraag om het bedrag tot het geldig is, zet het om naar centen,
    roep de functie aan en print het aantal munten>
    