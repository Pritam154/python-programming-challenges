def maximize_spending():
    money, nb_keyboards, nb_usbs = [int(x) for x in input().split()]
    keyboards = [int(x) for x in input().split()]
    usbs = [int(x) for x in input().split()]
    max_spending = -1

    for keyboard in keyboards:
        for usb in usbs:
            amount = keyboard + usb
            if amount > max_spending and amount <= money:
                max_spending = amount

    return max_spending


if __name__ == '__main__':
    print(maximize_spending())
