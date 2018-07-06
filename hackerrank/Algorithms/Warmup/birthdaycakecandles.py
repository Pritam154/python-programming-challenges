def birthdayCakeCandles(n, ar):
    ar = sorted(ar, reverse=True)
    ar_max = max(ar)
    return ar.count(ar_max)


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = birthdayCakeCandles(n, ar)
    print(result)
