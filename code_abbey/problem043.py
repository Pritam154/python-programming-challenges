import math


def convert_roll_dice(value: float) -> int:
    return math.floor(float(value) * 6) + 1


if __name__ == '__main__':
    n_times = int(input())

    for value in range(n_times):
        print(convert_roll_dice(input()), end=' ')
