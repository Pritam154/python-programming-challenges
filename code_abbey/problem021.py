m, n = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]

value_dict = {}

for array in values:
    if array in value_dict:
        value_dict[array] += 1
    if array not in value_dict:
        value_dict[array] = 1

for key in sorted(value_dict):
    print(value_dict[key], end=' ')
