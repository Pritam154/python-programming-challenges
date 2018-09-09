'''
Problem #2: Sum in Loop
'''


def sum_all_ints():
    '''Sum all numbers from input using a loop'''
    _ = int(input())  # Captures number of test cases. Not used.
    list_values = [int(x) for x in input().split()]
    total_sum = 0

    for integer in list_values:
        total_sum += integer

    return total_sum


if __name__ == '__main__':
    print(sum_all_ints())
