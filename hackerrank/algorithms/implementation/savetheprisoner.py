'''
Save the Prisoner!
'''


def get_poisoned_id(n, m, s) -> int:
    '''Returns the ID of the prisoner that will be poisoned.'''
    if m == 1:
        return s

    final_position = s + m - 1
    if final_position <= n:
        return final_position
    else:
        big_final_position = final_position % n
        if big_final_position == 0:
            return n
        else:
            return big_final_position


def set_jail():
    '''Evaluate the input and for each test case, return the prisoner ID
       who will be poisoned.'''
    num_tests = int(input())

    for test in range(num_tests):
        n, m, s = [int(x) for x in input().split()]
        print(get_poisoned_id(n, m, s))


if __name__ == '__main__':
    set_jail()
