def aVeryBigSum(n, ar):
    # Complete this function
    answer = sum(ar)
    return answer


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = aVeryBigSum(n, ar)
    print(result)
