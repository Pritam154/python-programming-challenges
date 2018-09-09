from math import floor


def chocolateFeast(n, c, m):
    spending_money = n
    cost_chocolate = c
    wrapper_num = m

    num_chocolates = floor(spending_money / cost_chocolate)
    if num_chocolates >= wrapper_num:
        wrapper_num = num_chocolates - wrapper_num
        pass


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolateFeast(n, c, m)
        print(result)
