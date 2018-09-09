'''
Fibonnaci Modified

Relation to follow:
t(3) = t(1) + ( t(2) ) ** 2
t(4) = t(2) + ( t(3) ) ** 2   ... and so on
'''


def execute():
    t1, t2, n = [int(x) for x in input().split()]
    terms_dict = {1: t1, 2: t2}

    def fib_modif(element_n, dict_fib):
        if element_n in dict_fib:
            return dict_fib[element_n]
        else:
            fib_n = fib_modif(element_n-1,
                              dict_fib)**2 + fib_modif(element_n-2, dict_fib)
            dict_fib[element_n] = fib_n
            return fib_n

    return fib_modif(n, terms_dict)


if __name__ == '__main__':
    print(execute())
