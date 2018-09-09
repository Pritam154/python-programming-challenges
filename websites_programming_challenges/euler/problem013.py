# Work out the first ten digits of the sum of the following
# one-hundred 50-digit numbers.

big_data = []
with open("problem13_data.py", "r") as problem_data:
    for line in problem_data:
        big_data.append(line.rstrip('\n'))
big_data = str(sum(map(int, big_data)))
big_data = big_data[0:10]
print(big_data)
