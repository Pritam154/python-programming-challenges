# FIXME: This works, but it is way too slow.


def is_square(number):
    base_num = str(number**0.5)
    return True if base_num.endswith('.0') else False


def num_of_squares(starting_num, ending_num):
    total_squares = 0
    for i in range(starting_num, ending_num + 1):
        if is_square(i):
            total_squares += 1
    return total_squares


if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        first_num, second_num = [int(x) for x in input().split()]
        print(num_of_squares(first_num, second_num))
