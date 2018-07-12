from collections import Counter


def get_store_inventory():
    num_shoes = int(input())
    shoe_sizes = [int(x) for x in input().split()]
    shoe_count = Counter(shoe_sizes)

    return shoe_count


def pass_orders(shoe_list):
    num_customers = int(input())
    money_earned = 0

    for customer in range(num_customers):
        shoe_size, shoe_price = [int(x) for x in input().split()]
        if shoe_size in shoe_list and shoe_list[shoe_size] > 0:
            shoe_list[shoe_size] -= 1
            money_earned += shoe_price

    return money_earned


def main():
    shoe_availability = get_store_inventory()
    money_earned = pass_orders(shoe_availability)
    print(money_earned)


if __name__ == '__main__':
    main()
