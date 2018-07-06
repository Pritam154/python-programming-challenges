'''
Problem #13: Weighted sum of digits
'''


def wsd(number):
    '''Calculate the weigthed sum of digits of argument "number".'''
    number = str(number)
    total_sum = 0
    for index, digit in enumerate(number):
        total_sum += (index + 1) * int(digit)
    return total_sum


def execution():
    _ = int(input())  # Not used
    list_sums = [int(x) for x in input().split()]
    res_sums = []
    for wsum in list_sums:
        res_sums.append(wsd(wsum))
    for value in res_sums:
        print(value, end=' ')


execution()
