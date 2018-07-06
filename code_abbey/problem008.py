'''
Problem #8: Arithmetic Progression
'''


def arithmetic_progression():
    '''Returns a string of all calculated triplets.'''
    number_cases = int(input())
    result_list = []

    for _ in range(number_cases):
        int_a, int_b, int_n = [int(x) for x in input().split()]
        case_calculation = 1 / 2 * int_n * (2 * int_a + (int_n - 1) * int_b)
        case_result = int(case_calculation)
        result_list.append(case_result)

    result_string = ' '.join(str(result) for result in result_list)
    return result_string


if __name__ == '__main__':
    print(arithmetic_progression())
