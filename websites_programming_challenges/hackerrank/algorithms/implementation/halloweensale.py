def number_games():
    (initial_price, discount,
     minimum_price, money) = [int(x) for x in input().split()]

    if initial_price > money:
        return 0

    buying_list = [initial_price]
    while sum(buying_list) < money:
        game = buying_list[-1] - discount
        if game < minimum_price:
            game = minimum_price
        if sum(buying_list) + game > money:
            break
        else:
            buying_list.append(game)

    return len(buying_list)


if __name__ == '__main__':
    print(number_games())
