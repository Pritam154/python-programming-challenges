'''
Problem #4: Minimum of Two
'''


def minimum_of_two():
    '''Returns a string of the smallest value in pairs of two integers.'''
    quantity = int(input())
    minimum_values = []

    for _ in range(quantity):
        integers = [int(x) for x in input().split()]
        minimum_value = min(integers)
        minimum_values.append(minimum_value)

    result_string = ' '.join(str(result) for result in minimum_values)
    return result_string


if __name__ == '__main__':
    print(minimum_of_two())
