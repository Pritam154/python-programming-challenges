from collections import OrderedDict

item_num = int(input())
ordered_dict = OrderedDict()

for item in range(item_num):
    item_details = input().rsplit(" ", 1)  # splits the price from the name
    item_name = item_details[0]
    item_price = int(item_details[1])
    if item_name in ordered_dict:
        ordered_dict[item_name] += item_price
    else:
        ordered_dict[item_name] = item_price

for item, price in ordered_dict.items():
    print(item, price)