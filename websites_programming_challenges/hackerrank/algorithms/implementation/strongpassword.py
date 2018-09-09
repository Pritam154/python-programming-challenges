"""
    Its length is at least 6.
    It contains at least one digit.
    It contains at least one lowercase English character.
    It contains at least one uppercase English character.
    It contains at least one special character.
        The special characters are: !@#$%^&*()-+
"""


def minimumNumber(n, password):
    required_length = 6
    chars_to_add = 0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    original_length = len(password)
    iterate_over = [numbers, lower_case, upper_case, special_characters]

    for string in iterate_over:
        count_in_string = False
        for char in string:
            if char in password:
                count_in_string = True
                break
        if not count_in_string:
            chars_to_add += 1

    new_length = original_length + chars_to_add
    if new_length < required_length:
        chars_to_add = chars_to_add + (required_length - new_length)
    return chars_to_add


if __name__ == '__main__':
    n = int(input())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)
