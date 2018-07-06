if __name__ == '__main__':
    arr = sorted(list(map(int, input().strip().split(' '))))

    minimum_sum = sum(arr[0:4])
    maximum_sum = sum(arr[1:5])

    print(minimum_sum, maximum_sum)
