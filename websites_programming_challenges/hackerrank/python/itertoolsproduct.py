def cartesian_product():
    from itertools import product

    lst_a = [int(a) for a in input().split()]
    lst_b = [int(b) for b in input().split()]

    answer = list(product(lst_a, lst_b))

    for item in answer:
        print(item, end=' ')


if __name__ == '__main__':
    cartesian_product()
