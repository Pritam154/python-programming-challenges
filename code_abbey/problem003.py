'''
Problem #3: Sums in Loop
'''


def sums_in_loop():
    '''Returns a string of pairs of sums.'''
    number_pairs = int(input())
    list_sums = []

    for _ in range(number_pairs):
        int_a, int_b = [int(x) for x in input().split()]
        list_sums.append(int_a+int_b)

    result_string = ' '.join(str(result) for result in list_sums)
    return result_string


if __name__ == '__main__':
    print(sums_in_loop())
