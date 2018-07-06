"""
Find the average.
"""

line_number = int(input())
average_list = []

for i in range(line_number):
    line_list = list(map(int, input().split()))
    line_list.remove(0)
    length_list = len(line_list)
    sum_list = sum(line_list)

    average_list.append(round(sum_list / length_list))

[print(item, end=' ') for item in average_list]

"""
Better way:

for i in range(int(input())):
    array = list(map(int, input().split()))
    print(round(sum(array) / (len(array) - 1)), end=' ')

"""
