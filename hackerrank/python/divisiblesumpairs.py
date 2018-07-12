def run_program() -> int:
    n, k = [int(x) for x in input().split()]
    nvalues = [int(x) for x in input().split()]
    pair_count = 0
    for indexi, i in enumerate(nvalues):
        for indexj, j in enumerate(nvalues):
            if indexi < indexj and (i+j) % k == 0:
                pair_count += 1
    return pair_count


if __name__ == '__main__':
    print(run_program())
