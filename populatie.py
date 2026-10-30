def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.
    """
    jaar = 0
    while start_size < end_size:
        start_size = start_size + int(start_size // 3) - int(start_size // 4)
        jaar += 1

if __name__ == '__main__':
    <Hoofdprogramma>