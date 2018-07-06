from problem017 import array_checksum


def read_input():
    list_ints = [int(x) for x in input().split()]
    list_ints.pop()  # removes last integer which is "-1"
    return list_ints


def count_swaps(array_ints):
    """Returns number of swaps made and the actual array after making the
       different swaps."""
    length_without_last = len(array_ints) - 1
    swap_array = array_ints[:]
    swap_count = 0

    for index in range(length_without_last):
        first_value = swap_array[index]
        second_value = swap_array[index+1]
        if first_value > second_value:
            # Every time this is true, swaps values in array and check again
            # for next index in array, which now corresponds to first_value.
            swap_array[index] = second_value
            swap_array[index+1] = first_value
            swap_count += 1

    return swap_count, swap_array


if __name__ == '__main__':
    array_ints = read_input()
    swap_count, swap_array = count_swaps(array_ints)

    # Get the checksum for swapped array, not the checksum of the array
    # initially given in the problem.
    checksum_answer = array_checksum(swap_array)
    print(swap_count, checksum_answer)
