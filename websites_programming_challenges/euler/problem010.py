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

for number in range(2,2000001):
    isprime(number)

print(sum(list_primes))
