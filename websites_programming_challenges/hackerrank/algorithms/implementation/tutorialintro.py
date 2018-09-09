'''
Tutorial Intro
'''


def find_value_in_array() -> int:
    '''Find a specific value in array and return its index.'''
    V = int(input())
    n = int(input())
    arr = [int(x) for x in input().split()]

    for index, value in enumerate(arr):
        if value == V:
            return index


if __name__ == '__main__':
    print(find_value_in_array())
