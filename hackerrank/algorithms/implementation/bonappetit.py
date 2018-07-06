if __name__ == '__main__':
    # n : number of items ordered
    # k : item not eaten by Anna
    n, k = map(int, input().split())

    # cost of items
    cost = list(map(int, input().split()))

    # Amount charged by Brian
    b_charged = int(input())

    b_actual = (sum(cost) - cost[k]) / 2

    overcharge = int(b_charged - b_actual)

    if overcharge == 0:
        print('Bon Appetit')
    else:
        print(overcharge)
