# What is the 10 001st prime number?

total_number_of_primes = 10001

list_primes = []

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        list_primes.append(n)
        return True
    if n == 3:
        list_primes.append(n)
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    list_primes.append(n)
    return True

number_to_test = 2

while len(list_primes) < total_number_of_primes:
    isprime(number_to_test)
    number_to_test += 1

print(f"Prime # {total_number_of_primes} = {list_primes[-1]}")
