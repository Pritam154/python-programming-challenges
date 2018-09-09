def get_all_combinations():
    from itertools import combinations

    user_input = input()
    input_string = user_input.split()[0]
    input_string = ''.join(sorted(input_string))  # Sorts string alphabetically
    combination_len = int(user_input.split()[1])
    combinations_lst = []

    for comb_len in range(1, combination_len + 1):
        all_combinations = list(combinations(input_string, comb_len))

        for combination in all_combinations:
            combinations_lst.append(''.join(combination))

    for combination in combinations_lst:
        print(combination)
    return True


if __name__ == '__main__':
    get_all_combinations()
