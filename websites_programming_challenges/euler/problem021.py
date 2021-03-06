# Evaluate the sum of all the amicable numbers under 10000.

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.


def divisors_of_number(n):
    list_divisors = [1]
    for i in range(2, n):
        if n % i == 0:
            list_divisors.append(int(n // i))
    return sum(list_divisors)


def list_amicable_numbers():
    amicable_numbers = []
    for i in range(10001):
        number2 = divisors_of_number(divisors_of_number(i))
        if i == number2 and divisors_of_number(i) != i:
            amicable_numbers.append(i)
    sum_of_list = sum(amicable_numbers)
    return sum_of_list


print(list_amicable_numbers())
