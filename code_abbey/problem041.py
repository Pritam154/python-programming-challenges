'''
Problem #41: Median of Three
'''


def sort_median(list_values):
    '''Sorts through a list and return the median value.'''
    list_values.sort()
    return list_values[1]


NUMBER_CASES = int(input())

for i in range(NUMBER_CASES):
    list_to_pass = [int(x) for x in input().split()]
    print(sort_median(list_to_pass), end=' ')
