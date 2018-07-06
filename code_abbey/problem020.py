list_vowels = 'aeiouy'

total_lines = int(input())
total_per_line = []

for line in range(total_lines):
    line_string = list(input())
    count_line = 0
    for char in line_string:
        if char in list_vowels:
            count_line += 1
    total_per_line.append(count_line)

for value in total_per_line:
    print(value, end=' ')