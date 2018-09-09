from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)

    # The following commented code is equivalent to the above line
    # result = 1
    # for fraction in fracs:
    #     result = result * fraction
    # return result.numerator, result.denominator

    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
