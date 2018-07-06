'''
Problem #1: Sum "A+B"

Simply calculate the sum of two integers without using the
built-in "sum" function directly: sum(iterable)
'''


def sum_two_integers():
    '''Sums two integers'''
    int_a, int_b = [int(x) for x in input().split()]
    return int_a + int_b


if __name__ == '__main__':
    print(sum_two_integers())
