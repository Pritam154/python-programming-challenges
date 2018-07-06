'''
Problem #5: Minimum of Three

This will be solved without using the built-in function "min".
'''


def minimum_of_three():
    '''Returns a string of the minimum values in given triplets.'''
    quantity = int(input())
    minimum_values = []

    for _ in range(quantity):
        int_a, int_b, int_c = [int(x) for x in input().split()]
        if int_a < int_b:
            int_b = int_a
        if int_b < int_c:
            int_c = int_b
        minimum_values.append(int_c)

    result_string = ' '.join(str(result) for result in minimum_values)
    return result_string


if __name__ == '__main__':
    print(minimum_of_three())
