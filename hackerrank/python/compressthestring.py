from itertools import groupby


def compress_string():
    input_string = input()
    groups = []
    for k, g in groupby(input_string):
        groups.append(list(g))

    for group in groups:
        print("({}, {})".format(len(group), group[0]), end=' ')


if __name__ == '__main__':
    compress_string()
