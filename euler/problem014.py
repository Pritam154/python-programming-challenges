'''
Problem #14: Longest Collatz sequence
'''

STORE_CHAINS = {}


def even_integer(n):
    return int(n/2)


def odd_integer(n):
    return int(3*n + 1)


def solve_chain(n):
    count_chain = 1
    while n != 1:
        if n % 2 == 0:
            n = even_integer(n)
        else:
            n = odd_integer(n)
        count_chain += 1
    return count_chain


def store_chains(n):
    STORE_CHAINS[n] = solve_chain(n)


def retrieve_max_value(dictionary):
    return max(dictionary, key=dictionary.get)


def execute_program():
    for i in range(1, 1000001):
        store_chains(i)
    return retrieve_max_value(STORE_CHAINS)


print(execute_program())
