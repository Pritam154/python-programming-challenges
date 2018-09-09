def read_and_print_name() -> str:
    first_name = input()
    last_name = input()

    output_string = ('Hello {} {}! You just delved into python.'
                     .format(first_name, last_name))

    return output_string


if __name__ == '__main__':
    print(read_and_print_name())
