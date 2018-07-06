if __name__ == '__main__':
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)

    left_diagonal = []
    right_diagonal = []

    for i in range(n):
        left_diagonal.append(a[i][i])
        right_diagonal.append(a[i][n - 1 - i])

    sum_left = sum(left_diagonal)
    sum_right = sum(right_diagonal)
    result = abs(sum_left - sum_right)

    print(result)
