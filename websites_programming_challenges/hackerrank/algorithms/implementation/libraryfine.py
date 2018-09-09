'''
Library Fine
'''


def get_fine():
    from datetime import date

    day_return, month_return, year_return = [int(x) for x in input().split()]
    day_expect, month_expect, year_expect = [int(x) for x in input().split()]

    date_return = date(year_return, month_return, day_return)
    date_expect = date(year_expect, month_expect, day_expect)
    date_differ = (date_return - date_expect).days

    if date_differ <= 0:
        return 0
    elif year_return != year_expect:
        return 10000
    elif month_return != month_expect:
        return (month_return - month_expect) * 500
    elif day_return != day_expect:
        return (day_return - day_expect) * 15
    else:
        return 'something went wrong'


if __name__ == '__main__':
    print(get_fine())
