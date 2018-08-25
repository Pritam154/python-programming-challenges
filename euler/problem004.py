a = sorted(range(1, 1001), reverse=True)
b = sorted(range(1, 1001), reverse=True)

palindrome_list = []

for i_a in a:
    for i_b in b:
        if str(i_a * i_b) == str(i_a * i_b)[::-1]:
            palindrome_list.append(i_a * i_b)

print(max(palindrome_list))