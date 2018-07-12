from collections import defaultdict


def get_input():
    dico = defaultdict(list)
    n, m = [int(x) for x in input().split()]

    for i in range(n):
        word = input()
        dico['n'].append(word)
    for i in range(m):
        word = input()
        dico['m'].append(word)

    return dico


def find_indexes(list_dict):
    for word in list_dict['m']:
        if word not in list_dict['n']:
            print("-1")
        else:
            for index, value in enumerate(list_dict['n']):
                if value == word:
                    print(index + 1, end=' ')
            print()


def main():
    dict_list = get_input()
    find_indexes(dict_list)


if __name__ == '__main__':
    main()
