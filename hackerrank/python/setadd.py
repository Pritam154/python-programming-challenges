def solve_problem():
    n = int(input())
    set_stamps = set()
    for stamp in range(n):
        set_stamps.add(input())
    return len(set_stamps)


if __name__ == '__main__':
    print(solve_problem())
