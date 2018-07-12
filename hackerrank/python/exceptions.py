def zero_division():
    test_cases = int(input())

    for i in range(test_cases):
        try:
            a, b = [int(x) for x in input().split()]
            print(a//b)
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)


if __name__ == '__main__':
    zero_division()
