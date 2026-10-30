def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.
    """
    jaren = 0
    while start_size < end_size:
        start_size = start_size + int(start_size // 3) - int(start_size // 4)
        jaren += 1
    return jaren

if __name__ == '__main__':
    start_size = int(input("Startgrootte: "))
    end_size = int(input("Eindgrootte: "))
    while start_size <= 9:
        start_size = int(input("Startgrootte: "))
    while end_size < start_size:
        start_size = int(input("Startgrootte: "))
        end_size = int(input("Eindgrootte: "))
    print(jaren)   
        