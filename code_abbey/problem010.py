'''
Problem #10: Linear Function
'''


def find_slope(int_a, int_b, int_c, int_d):
    '''Returns the slope of a linear function.'''
    return int((int_d - int_b) / (int_c - int_a))


def find_intercept(int_a, int_b, int_m):
    '''Returns the intercept of a linear function.'''
    return int(int_b - (int_m * int_a))


def linear_function():
    '''Returns the slope and intercept in the format (slope, intercept).'''
    result = []
    number_cases = int(input())
    for _ in range(number_cases):
        int_a, int_b, int_c, int_d = [int(x) for x in input().split()]
        int_m = find_slope(int_a, int_b, int_c, int_d)
        int_g = find_intercept(int_a, int_b, int_m)
        result.append('({} {})'.format(int_m, int_g))
    print(' '.join(result))


if __name__ == '__main__':
    linear_function()
