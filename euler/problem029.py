# How many distinct terms are in the sequence generated
# by a ** b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

list_numbers = []

for i_base in range(2, 101):
    for i_exp in range(2, 101):
        list_numbers.append(i_base ** i_exp)

print(len(set(list_numbers)))
