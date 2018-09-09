def find_256th_day(year: int, is_leap: bool) -> str:
    year_mod = 1 if is_leap else 0
    total_to_september = 243 + year_mod
    if year == 1918:
        total_to_september -= 13
    day = 256 - total_to_september
    month = '09'
    return '{day}.{month}.{year}'.format(day=day, month=month, year=year)


def is_julian_leap(year: int) -> bool:
    return year % 4 == 0


def is_gregorian_leap(year: int) -> bool:
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def day_of_programmer() -> str:
    '''Returns the date in the format dd.mm.yyyy of the Day of the Programmer
    based on Russia's calendar rules.'''
    input_year = int(input())

    if 1700 <= input_year <= 1917:
        is_leap = is_julian_leap(input_year)
    if input_year >= 1918:
        is_leap = is_gregorian_leap(input_year)
    return find_256th_day(input_year, is_leap)


if __name__ == '__main__':
    print(day_of_programmer())
