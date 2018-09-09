'''
Find Digits
'''


def test_digit_division(number: int) -> dict:
    '''Test divisibility of number from 2 to 9.'''
    digit_division = {}
    for digit in range(2, 10):
        if number % digit == 0:
            digit_division[digit] = True
        else:
            digit_division[digit] = False
    return digit_division


def count_of_digits(number: int) -> dict:
    '''Return a dictionary with digits from 1 to 9 as keys and indicate the
       number of times each digit appear for each key in number.'''
    number_string = str(number)
    digit_dict = {}
    for digit in range(1, 10):
        count_digit = number_string.count(str(digit))
        digit_dict[digit] = count_digit
    return digit_dict


def count_digit_divisibility(number: int) -> int:
    '''Return the number of divisions that can be made in number with a
       remainder of zero for all individial digits of number (repeating or
       not), excluding division by zero.'''
    digit_counts = count_of_digits(number)
    digit_divisible = test_digit_division(number)
    total_count = digit_counts[1]

    for digit in range(2, 10):
        if digit_divisible[digit]:
            total_count += digit_counts[digit]

    return total_count


def find_all_divisions():
    number_of_cases = int(input())

    for case_number in range(number_of_cases):
        print(count_digit_divisibility(int(input())))


if __name__ == '__main__':
    find_all_divisions()
