'''
Beautiful Days at the Movies
'''


def reverse_digits(number: int) -> int:
    '''Takes an int and return all digits in reversed order without leading
       zeros.'''
    string_num = str(number)[::-1]  # converts to string and reverse
    string_num.lstrip('0')  # remove leading '0'
    int_reversed = int(string_num)
    return int_reversed


def is_beautiful(day, k) -> bool:
    '''Returns True if day is beautiful, False otherwise.'''
    reversed_day = reverse_digits(day)
    calculation = abs(day - reversed_day) / k
    is_int = str(calculation).endswith('.0')
    return is_int


def beautiful_days() -> int:
    '''Evaluates if a range of days is beautiful and returns the number of
       days that are beautiful in that range.'''
    i, j, k = [int(x) for x in input().split()]

    beautiful_days_count = 0
    for day in range(i, j + 1):
        if is_beautiful(day, k):
            beautiful_days_count += 1
    return beautiful_days_count


if __name__ == '__main__':
    print(beautiful_days())
