import string

with open('problem17_output.txt', 'r') as outputfile:
    data = outputfile.read()

data_len = 0
for char in data:
    if char in string.ascii_lowercase:
        data_len += 1
print(data_len)
