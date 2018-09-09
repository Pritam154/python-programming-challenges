def is_palindrome(string) -> bool:
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])


def is_all_int(list_int: list) -> bool:
    return all([x >= 0 for x in list_int])


def evaluate_input():
    n = int(input())
    int_list = [int(x) for x in input().split()]
    str_list = [str(x) for x in int_list]

    if not is_all_int(int_list):
        return False

    return any([is_palindrome(x) for x in str_list])


if __name__ == '__main__':
    print(evaluate_input())
