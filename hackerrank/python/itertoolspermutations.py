def get_all_permutations():
    from itertools import permutations

    user_input = input()
    input_string = user_input.split()[0]
    permutation_len = int(user_input.split()[1])
    all_permutations = permutations(input_string, permutation_len)
    permutations_lst = []

    for permutation in all_permutations:
        permutations_lst.append(''.join(permutation))

    permutations_lst.sort()
    for permutation in permutations_lst:
        print(permutation)
    return True


if __name__ == '__main__':
    get_all_permutations()
