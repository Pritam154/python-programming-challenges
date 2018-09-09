def split_and_join() -> str:
    ''' Split a string on a space delimiter (" ") and join back with hyphen.'''
    input_string = input()
    output_string = input_string.split()
    output_string = '-'.join(output_string)

    return output_string


if __name__ == '__main__':
    print(split_and_join())
