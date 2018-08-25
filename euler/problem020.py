# Find the sum of the digits in the number 100!

import math

number = str(math.factorial(100))
list_number = []

for char in number:
    list_number.append(char)

list_number = map(int, list_number)
sum_number = sum(list_number)

print(sum_number)
