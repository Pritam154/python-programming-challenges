"""
Problem #31: Rotate String
"""


def rotate_string(position_to_cut, string_to_rotate):
    beginning = string_to_rotate[position_to_cut:]
    end = string_to_rotate[:position_to_cut]
    new_string = beginning + end
    return new_string


if __name__ == '__main__':
    cases = int(input())
    for case in range(cases):
        input_data = [x for x in input().split()]
        position_to_cut, string_to_rotate = int(input_data[0]), input_data[1]
        print(rotate_string(position_to_cut, string_to_rotate), end=" ")
