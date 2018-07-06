'''
Problem #11: Sum of digits
'''


def sum_of_digits():
    '''Returns a string of all answers in the following manner:
       for each case, multiply A by B and add C - then calculate
       sum of digits of the result.'''

    number_cases = int(input())
    final_answer = []

    for _ in range(number_cases):
        int_a, int_b, int_c = [int(x) for x in input().split()]
        result = int_a * int_b + int_c
        case = 0
        while result:
            case += result % 10
            result //= 10
        final_answer.append(case)

    result_string = ' '.join(str(answer) for answer in final_answer)
    return result_string


if __name__ == '__main__':
    print(sum_of_digits())
