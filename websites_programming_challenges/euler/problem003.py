"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
big_factors = []


def evaluate_factors(number):
    i = 5
    while i * i <= number:
        if number % i == 0:
            big_factors.append(number // i)
        elif number % (i + 2) == 0:
            big_factors.append(number // (i + 2))
        i += 6


evaluate_factors(number)

while len(big_factors) > 0:
    biggest_factor = big_factors.pop(0)
    big_factors = []
    evaluate_factors(biggest_factor)
    if len(big_factors) == 0:
        print(biggest_factor)
