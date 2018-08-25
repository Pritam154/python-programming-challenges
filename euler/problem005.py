# Find smallest number divisible by all numbers from 1 to 20

number_to_find = 230000000
counter = 0


def division_test(n):
    result = True
    for i in range(20):
        if n % (20 - i) != 0:
            result = False
            break
    return result


def program_execution():
    global number_to_find
    while number_to_find < 1000000000:  # empirical guess :)
        if division_test(number_to_find):
            print(number_to_find)
            break
        else:
            number_to_find += 1


if __name__ == '__main__':
    program_execution()
