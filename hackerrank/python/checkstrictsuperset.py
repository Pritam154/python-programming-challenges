def is_strict_superset(superset, subset):
    len_a = len(superset)
    len_n = len(subset)
    if len_a <= len_n:
        return False
    else:
        return subset.issubset(superset)


def main_execution():
    set_a = {int(x) for x in input().split()}
    num_sets = int(input())

    for set_number in range(num_sets):
        set_n = {int(x) for x in input().split()}
        result_set_n = is_strict_superset(set_a, set_n)
        if not result_set_n:
            return False
    return result_set_n


print(main_execution())
