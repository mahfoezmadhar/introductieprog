def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.
    """
    if old_type.upper() == "C":
        return int((18 * old_temp + 320) / 10)
    else:
        return int((10 * old_temp - 320) / 18)
    

def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.
    """
    if old_type.upper() == "C":
        print(f"{'C':>10}")
    else:
        print(f"{'F':>10}")

    
    if end_temp > old_temp:
        for temperatuur in range(begin_temp, end_temp + 1, step_size):
            omgerekend = convert_temperature(old_type, temperatuur)
                print(f"{temperatuur:>10}{omgerekend:>10}")

if __name__ == '__main__':
    <Hoofdprogramma>        