"""
The famous Bubble Sort.
"""


def read_input():
    array_length = int(input())
    array_list = [int(x) for x in input().split()]
    return array_length, array_list


def bubble_sort(array_list):
    """Returns the number of passes made through the list and the total number
       of swaps made using "Bubble Sort" sorting algorithm."""
    swap_array = array_list[:]
    pass_count = 0
    swap_count = 0

    swaps_in_pass = True
    while swaps_in_pass:  # while change is made in list
        current_swaps = 0  # will check if swaps are made in current for loop
        pass_count += 1  # we must loop through array, so that's a forced pass
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
        else:
            # adds number of swaps for current pass to total number of swaps
            swap_count += current_swaps

    return pass_count, swap_count


if __name__ == '__main__':
    array_length, array_list = read_input()
    pass_count, swap_count = bubble_sort(array_list)
    print(pass_count, swap_count)
