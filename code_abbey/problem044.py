"""
Problem #44: Double Dice Roll
"""

def to_dice_roll(int_num1, int_num2):
    return (int_num1 % 6) + (int_num2 % 6) + 2


if __name__ == '__main__':
    cases = range(int(input()))
    for case in cases:
        int1, int2 = [int(x) for x in input().split()]
        print(to_dice_roll(int1, int2), end=" ")