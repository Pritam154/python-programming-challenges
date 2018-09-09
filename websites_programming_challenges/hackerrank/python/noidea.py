def find_happiness():
    n, m = [int(x) for x in input().split()]
    array_n = {int(x) for x in input().split()}
    a = {int(x) for x in input().split()}
    b = {int(x) for x in input().split()}

    total_happiness = 0

    for num in a:
        if num in array_n:
            total_happiness += 1
    for num in b:
        if num in array_n:
            total_happiness -= 1

    return total_happiness


if __name__ == '__main__':
    print(find_happiness())
