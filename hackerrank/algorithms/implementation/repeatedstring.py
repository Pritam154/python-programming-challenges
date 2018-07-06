def repeated_string():
    input_string = input()
    string_length = len(input_string)
    n = int(input())
    count_a = input_string.count('a')

    if count_a == 0:
        return 0
    else:
        count_a = n // string_length * count_a
        extra_a = input_string[:(n % string_length)].count('a')

        return count_a + extra_a


if __name__ == '__main__':
    print(repeated_string())
