'''
Problem #25: Linear Congruential Generator
'''

# Xnext = (A * Xcur + C) % M
# input: A, C, M, X0, N  -> where X0 = Xcurrent and N = n th member


def find_member_n() -> int:
    A, C, M, x_cur, N = [int(x) for x in input().split()]
    current_member = 1

    while current_member <= N:
        x_next = (A * x_cur + C) % M
        x_cur = x_next
        current_member += 1

    return x_cur


if __name__ == '__main__':
    num_cases = int(input())

    for case in range(num_cases):
        print(find_member_n(), end=' ')
