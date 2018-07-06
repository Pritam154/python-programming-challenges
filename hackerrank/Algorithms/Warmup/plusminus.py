if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    list_positive, list_negative, list_zero = [], [], []

    for number in arr:
        if number < 0:
            list_negative.append(number)
        elif number == 0:
            list_zero.append(number)
        else:
            list_positive.append(number)

    print(len(list_positive) / n)
    print(len(list_negative) / n)
    print(len(list_zero) / n)
