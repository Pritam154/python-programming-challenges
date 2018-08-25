# What is the sum of the digits of the number 2^1000?

number_exponent = str(2 ** 1000)
list_number_exponent = []

for char in number_exponent:
    list_number_exponent.append(int(char))

print(sum(list_number_exponent))
