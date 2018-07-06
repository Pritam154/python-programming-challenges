if __name__ == '__main__':
    t = int(input())

    for case in range(t):
        n, k = [int(x) for x in input().split()]
        arrival_times = [int(x) for x in input().split()]
        on_time = 0
        for arrival in arrival_times:
            if arrival <= 0:
                on_time += 1
        if on_time >= k:
            print('NO')
        else:
            print('YES')
