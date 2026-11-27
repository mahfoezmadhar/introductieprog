# 1 januari 1800 is een woensdag
START_DAY = 3

def is_leap_year(year: int) -> bool:
    """
    >>> is_leap_year(2010)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(1901)
    False
    >>> is_leap_year(1940)
    True
    """
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        return True
    else:
        return False

def days_from_1800(month: int, year: int) -> int:
    """
    Telt de dagen vanaf 1800 tot aan `month` of `year`.
    De eerste dag van `month` zit hier dus niet bij.
    Gebruikt `days_from_1800_until_year` en `days_until_month`.
    """

def days_from_1800_until_year(year: int) -> int:
    """

    """
    if is_leap_year:
        aantal_dagen = 366
    else:
        aantal_dagen = 365
    return abs(year - 1800) * aantal_dagen

def days_until_month(month: int, year: int) -> int:
    """
    Telt het aantal dagen van 1 januari van `year` tot aan `month` van `year`.
    De dagen van `month` zitten hier dus niet bij.
    Gebruikt `days_in_month`.
    """

def days_in_month(month: int, year: int) -> int:
    """
    Bepaalt het aantal dagen in `month` van `year`.
    Gebruikt `is_leap_year`.
    """

def display_calendar(month: int, year: int) -> None:
    """
    Print de kalender.
    Gebruikt `display_header` en `display_grid`.
    """

def display_header(month: int, year: int) -> None:
    """
    Print de koptekst van de kalender.
    """

def display_grid(month: int, year: int) -> None:
    """
    Print het grid van de kalender.
    Gebruikt `first_weekday_month` en `days_in_month`.
    """

def first_weekday_month(month: int, year: int) -> int:
    """
    Bepaalt de eerste weekdag van de maand.
    Gebruikt `days_from_1800`.
    """

if __name__ == '__main__':
    year = int(input("Jaar: "))
    month = int(input("Maand: "))
    display_calendar(month, year)