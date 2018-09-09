'''
Super Reduced String
'''

import string


def reduce_string():
    input_string = input()
    alphabet = string.ascii_lowercase

    while True:
        for letter in alphabet:
            if input_string.find('{0}{0}'.format(letter)) != -1:
                output_string = input_string.replace(
                                                '{0}{0}'.format(letter), '')
        if input_string == output_string:
            break
        else:
            input_string = output_string

    if input_string == '':
        return 'Empty String'
    else:
        return input_string


if __name__ == '__main__':
    print(reduce_string())
