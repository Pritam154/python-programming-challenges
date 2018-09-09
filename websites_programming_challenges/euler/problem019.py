def count_sundays():
    '''Counts how many times Sunday fell on the first of the month from
       01/01/1901 to 12/31/2000.'''
    import calendar

    count_sundays = 0

    for year in range(1901, 2001):
        for month in range(1,13):
            if calendar.weekday(year, month, 1) == 6:  # 6 for Sunday
                count_sundays += 1

    return count_sundays
