'''
Problem #6: Rounding
'''


def round_division():
    '''Returns a string of divisions rounded to the nearest integer.'''
    number_cases = int(input())
    result_list = []

    for _ in range(number_cases):
        int_a, int_b = [int(x) for x in input().split()]
        result = round(int_a / int_b)
        result_list.append(result)

    result_string = ' '.join(str(result) for result in result_list)
    return result_string


if __name__ == '__main__':
    print(round_division())
