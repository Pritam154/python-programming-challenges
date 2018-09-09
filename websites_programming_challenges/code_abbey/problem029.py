"""
Bubble Sort with indexes.
"""


def read_input():
    array_length = int(input())
    array_list = [int(x) for x in input().split()]
    return array_list


def store_indexes(array_list: list) -> dict:
    """Returns dict with items in array as keys and their index as value."""
    array_dict = {}
    for index, item in enumerate(array_list):
        array_dict[item] = index + 1  # we consider first value to be 1, not 0
    return array_dict


def retrieve_indexes(array_list: list, array_dict: dict) -> list:
    sorted_indexes = []
    for item in array_list:
        sorted_indexes.append(array_dict[item])
    return sorted_indexes


def bubble_sort(array_list):
    """Returns a list of indexes of sorted values in 'array_list'.
       For example:
       Initial array: 50 98 17 79   Sorted array: 17 50 79 98
       17 was at 3-rd place initially, 50 was at 1-st place initially
       79 was at 4-th place initially, 98 was at 2-nd place initially
       Result: 3 1 4 2"""

    swap_array = array_list[:]

    while True:  # while change is made in list
        current_swaps = 0
        for index in range(len(array_list) - 1):
            first_value = swap_array[index]
            second_value = swap_array[index+1]
            if first_value > second_value:
                swap_array[index] = second_value
                swap_array[index+1] = first_value
                current_swaps += 1
        if current_swaps == 0:  # No swaps made from first to last element
            # pass_count and swap_count are already updated by this point
            break

    return swap_array


if __name__ == '__main__':
    array_list = read_input()
    array_dict = store_indexes(array_list)
    sorted_array = bubble_sort(array_list)
    sorted_indexes = retrieve_indexes(sorted_array, array_dict)
    for index in sorted_indexes:
        print(index, end=" ")
