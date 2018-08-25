# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def square_of_sum(n):
    list_square_of_sum = []
    for i in range(n + 1):
        list_square_of_sum.append(i)
    return sum(list_square_of_sum) ** 2

def sum_of_square(n):
    list_sum_of_square = []
    for i in range(n + 1):
        list_sum_of_square.append(i ** 2)
    return sum(list_sum_of_square)

def difference_sum_square(n):
    print(square_of_sum(n) - sum_of_square(n))

difference_sum_square(100)
