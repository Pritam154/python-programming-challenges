def between_sets():
    n, m = [int(x) for x in input().split()]
    set_a = {int(x) for x in input().split()}
    set_b = {int(x) for x in input().split()}
    list_x = 0

    for num in range(1, 101):
        num_between = True
        for num_a in set_a:
            if num % num_a != 0:
                num_between = False
                break
        if num_between:
            for num_b in set_b:
                if num_b % num != 0:
                    num_between = False
                    break
        if num_between:
            list_x += 1

    print(list_x)


if __name__ == '__main__':
    between_sets()
