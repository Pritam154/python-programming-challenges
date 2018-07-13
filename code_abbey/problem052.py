"""
Problem #52: Pythagorean Theorem
"""
from math import sqrt


def triangle_type(side_a, side_b, side_c) -> str:
    theoretical_hypotenuse = sqrt(side_a ** 2 + side_b ** 2)
    if side_c == theoretical_hypotenuse:
        return 'R'  # if Pythagorean Theorem works, it is a right triangle
    elif side_c < theoretical_hypotenuse:
        return 'A'  # acute triangle
    else:
        return 'O'  # obtuse triangle


if __name__ == '__main__':
    num_cases = int(input())
    for case in range(num_cases):
        side_a, side_b, side_c = [int(x) for x in input().split()]
        print(triangle_type(side_a, side_b, side_c), end=" ")
