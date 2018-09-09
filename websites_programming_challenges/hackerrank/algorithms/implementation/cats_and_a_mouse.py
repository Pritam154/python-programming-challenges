#!/bin/python3

import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    distance_cat_a = abs(z-x)
    distance_cat_b = abs(z-y)
    if distance_cat_a < distance_cat_b:
        return 'Cat A'
    elif distance_cat_b < distance_cat_a:
        return 'Cat B'
    else:
        return 'Mouse C'


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + '\n')

    f.close()
