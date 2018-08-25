# Fn = Fn−1 + Fn−2
# What is the index of the first term in the Fibonacci sequence
# to contain 1000 digits?

def fibonacci():
    list_fibonacci = [1, 1]
    i = 2
    while len(str(list_fibonacci[i-1])) < 1000:
        list_fibonacci.append(list_fibonacci[i-1] + list_fibonacci[i-2])
        i += 1
    print(len(list_fibonacci))
fibonacci()
