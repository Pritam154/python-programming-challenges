import string


def swap_dictionary() -> dict:
    '''Returns a dict where all letters in the alphabet are matched to their
       equivalent swapped case (i.e., a to A, A to a, b to B, B to b, etc.)'''
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    swap_dict = {}

    for letter in range(26):
        swap_dict[alpha_lower[letter]] = alpha_upper[letter]
        swap_dict[alpha_upper[letter]] = alpha_lower[letter]

    return swap_dict


def solve_swap_case() -> str:
    string_to_format = input()
    string_formatted = ''
    swap_dict = swap_dictionary()

    for letter in string_to_format:
        if letter in swap_dict:
            string_formatted += swap_dict[letter]
        else:
            string_formatted += letter

    return string_formatted


if __name__ == '__main__':
    print(solve_swap_case())
