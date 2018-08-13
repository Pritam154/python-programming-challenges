from collections import OrderedDict

ordered_dict = OrderedDict()
num_words = int(input())
for _ in range(num_words):
    word = input()
    if word in ordered_dict:
        ordered_dict[word] += 1
    else:
        ordered_dict[word] = 1

print(len(ordered_dict))
for value in ordered_dict.values():
    print(value, end=" ")