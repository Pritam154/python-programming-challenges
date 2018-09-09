"""
Problem #57: Smoothing the Weather
"""


def get_input() -> tuple:
    number_items = int(input())
    list_numbers = [float(x) for x in input().split()]
    return number_items, list_numbers


def smoothing_function(items_num: int, lnums: list) -> list:
    """`items_num`: number of items in list `lnums`
       `lnums`: list of the items"""
    final_list = []
    for index, number in enumerate(lnums):
        if index in [0, items_num - 1]:
            final_list.append(number)  # do not change first and last element
            continue
        average_value = (lnums[index - 1] + number + lnums[index + 1]) / 3
        final_list.append(average_value)
    return final_list


if __name__ == '__main__':
    number_items, list_numbers = get_input()
    answer_list = smoothing_function(number_items, list_numbers)
    for number in answer_list:
        print(number, end=" ")
