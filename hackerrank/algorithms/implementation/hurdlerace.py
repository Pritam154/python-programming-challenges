if __name__ == '__main__':
    n, k = [int(x) for x in input().split()]

    hurdles = [int(hurdle_temp) for hurdle_temp in input().strip().split(' ')]
    hurdle_max = max(hurdles)

    calculation = hurdle_max - k

    if calculation <= 0:
        drinks = 0
    else:
        drinks = calculation

    print(drinks)
