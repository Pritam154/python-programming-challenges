from itertools import combinations_with_replacement


def get_input():
    word_string, num_combinations = input().split()
    num_combinations = int(num_combinations)
    word_string = sorted(word_string)
    return word_string, num_combinations


def find_combinations(word, num_combinations):
    list_comb = list(combinations_with_replacement(word, num_combinations))
    return list_comb


def main():
    word_string, num_combinations = get_input()
    list_comb = find_combinations(word_string, num_combinations)

    for elem in list_comb:
        print(''.join(elem))


if __name__ == '__main__':
    main()
