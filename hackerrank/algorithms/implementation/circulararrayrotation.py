'''
Circular Array Rotation
'''


def read_input() -> tuple:
    '''Simply reads the input and returns a tuple to make use of it.'''
    n, k, q = [int(x) for x in input().split()]
    array_a = [int(x) for x in input().split()]
    list_queries = []
    for _ in range(q):
        query = int(input())
        list_queries.append(query)
    return (n, k, q, array_a, list_queries)


def solve_rotation() -> int:
    '''Rotates all elements in list a fixed number of times
       from left to right and returns index for each query.'''
    n, k, q, ar, lq = read_input()

    for i in range(k):
        last_value = ar.pop()
        ar.insert(0, last_value)

    for query in lq:
        print(ar[query])


if __name__ == '__main__':
    solve_rotation()
