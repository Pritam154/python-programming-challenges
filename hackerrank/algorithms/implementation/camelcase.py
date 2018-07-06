'''
CamelCase
'''

import string


def words_in_camel_case() -> int:
    '''Return number of words in a string written in CamelCase.'''
    input_string = input()
    words_count = 1
    alphabet_upper = string.ascii_uppercase

    for letter in input_string:
        if letter in alphabet_upper:
            words_count += 1

    return words_count


if __name__ == '__main__':
    print(words_in_camel_case())
