import calendar


def get_input() -> tuple:
    month, day, year = [int(x) for x in input().split()]
    return (month, day, year)


def find_day_of_week(date: tuple) -> str:
    w_dict = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY',
              4: 'FRIDAY', 5: 'SATURDAY', 6: 'SUNDAY'}
    month, day, year = date
    weekday_num = calendar.weekday(year, month, day)
    return w_dict[weekday_num]


def main():
    date_to_use = get_input()
    day_of_week = find_day_of_week(date_to_use)
    print(day_of_week)


if __name__ == '__main__':
    main()
