def wrapper(f):
    def fun(l):
        for i, phone_num in enumerate(l):
            last_5d = phone_num[-5:]
            first_5d = phone_num[-10:-5]

            l[i] = '+91 {} {}'.format(first_5d, last_5d)
        f(l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    phone_list = [input() for _ in range(int(input()))]
    sort_phone(phone_list)
