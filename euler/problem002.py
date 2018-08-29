"""
By considering the terms in the Fibonacci sequence whose values do not
EXCEED four million, find the sum of the even-valued terms.
"""

FIB_DICT = {1: 1, 2: 2}  # first two elements of the sequence
MAX_VALUE = 4000000  # stop looking for more values when this one is exceeded
FIB_NUMBER = 3  # starts at third element in the sequence


def fibonacci_seq(number=FIB_NUMBER, fib_dict=FIB_DICT):
    """Recursive implementation of the Fibonacci sequence using a dictionary.
    NUMBER is the position in the sequence of the element we are looking for.
    The function returns the value of the element at that position (integer)."""
    if number in fib_dict:
        return fib_dict[number]
    else:
        number1 = number - 1
        number2 = number - 2
        result = (fibonacci_seq(number=number1) +
                  fibonacci_seq(number=number2))
        fib_dict[number] = result
        return result


def clear_fib_dict(max_value=MAX_VALUE, fib_dict=FIB_DICT):
    """This will remove from FIB_DICT the key which has the largest value."""
    fib_dict_copy = fib_dict.copy()
    # iterates over a copy since dictionary size cannot change during loop
    for item, value in fib_dict_copy.items():
        if value > max_value:
            fib_dict.pop(item)  # removes key of largest value in original dict
            break  # no need to keep looking, there's only one biggest value!


def build_fib_dict(fib_number=FIB_NUMBER, max_value=MAX_VALUE,
                   fib_dict=FIB_DICT):
    """Adds key:value pairs to FIB_DICT until we exceed MAX_VALUE, starting at
    FIB_NUMBER."""
    while max(fib_dict.values()) <= max_value:
        fibonacci_seq(number=fib_number)
        fib_number += 1


def retrieve_even_values(fib_dict=FIB_DICT):
    """This will retrieve only even integers in a dictionary and store them as a
    list, returning that list."""
    fib_list = []
    for value in fib_dict.values():
        if value % 2 == 0:
            fib_list.append(value)
    return fib_list


if __name__ == '__main__':
    build_fib_dict()
    clear_fib_dict()  # removes largest number as it is greater than 4 million
    list_even_values = retrieve_even_values()
    solution = sum(list_even_values)
    print('The solution is:', solution)
