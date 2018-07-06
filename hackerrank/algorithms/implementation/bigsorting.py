'''
Big Sorting
'''


def read_input() -> list:
    arr_list = []
    n = int(input())

    for value in range(n):
        arr_list.append(input())

    return arr_list


def sort_and_solve():
    arr_list = read_input()

    # The following step turns out to be a lot faster than converting the above
    # list to integers in the 'for' loop in function read_input, sorting it
    # and then converting back to strings in order to print.
    arr_list.sort(key=int)

    for value in arr_list:
        print(value)


if __name__ == '__main__':
    sort_and_solve()
