'''
Problem #26: Greatest Common Divisor
'''


def gcd(a, b):
    '''Returns the greatest common divisor between "a" and "b".'''
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a-b, b)
        elif a < b:
            return gcd(a, b-a)


def lcm(a, b):
    '''Returns the least common multiple between "a" and "b".'''
    return a * b / gcd(a, b)


NUMBER_CASES = int(input())

for i in range(NUMBER_CASES):
    a, b = [int(x) for x in input().split()]
    gcd_i = int(gcd(a, b))
    lcm_i = int(lcm(a, b))
    print('({} {})'.format(gcd_i, lcm_i), end=' ')
