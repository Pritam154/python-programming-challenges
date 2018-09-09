import re


def is_valid_regex(regex_expr):
    try:
        re.search(regex_expr, 'string')
        return True
    except re.error:
        return False


def main():
    num_cases = int(input())

    for case in range(num_cases):
        print(is_valid_regex(input()))


if __name__ == '__main__':
    main()
