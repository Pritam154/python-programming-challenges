'''
Problem #48: Collatz Sequence
'''


def collatz_steps(number):
    '''Find the number of steps required to go back to number 1.'''
    step_count = 0
    if number == 0:  # let's avoid an infinite loop later just in case
        return step_count
    while True:
        if number == 1:  # this is the end of the sequence
            return step_count
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        step_count += 1


if __name__ == '__main__':
    num_cases = int(input())
    cases = [int(x) for x in input().split()]
    for case in cases:
        print(collatz_steps(case), end=' ')
