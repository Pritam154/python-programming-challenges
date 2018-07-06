'''
Problem #22: Two Printers
'''


def min_time(speed1, speed2, pages) -> int:  # FIXME: Way too slow. It works :)
    remaining_pages = pages
    current_time = 1

    while remaining_pages > 0:
        if current_time % speed1 == 0:
            remaining_pages -= 1
        if current_time % speed2 == 0:
            remaining_pages -= 1
        current_time += 1
    return current_time - 1


if __name__ == '__main__':
    num_cases = int(input())

    for case in range(num_cases):
        speed1, speed2, pages = [int(x) for x in input().split()]
        print(min_time(speed1, speed2, pages), end=' ')
