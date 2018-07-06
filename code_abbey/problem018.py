number_of_lines = int(input())
squares_list = []

for line in range(number_of_lines):
    r = 1
    x, n = input().split()
    x, n = (int(x), int(n))

    for i in range(n):
        r = (r + x / r) / 2

    squares_list.append(r)

for square in squares_list:
    print(square, end=' ')
