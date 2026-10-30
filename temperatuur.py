def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.
    """
    if convert_temperature.upper() == "C":
        return int((10 * old_temp - 320) / 18)
    else:
        return int((18 * old_temp + 320) / 10)
    

def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.
    """
    
    for temperatuur in range(begin_temp, end_temp + 1, step_size):
        while temperatuur < end_temp:
            convert_temperature()

if __name__ == '__main__':
    <Hoofdprogramma>        